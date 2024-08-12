<template>
  <div class="flex h-screen">
    <Sidebar />
    <div class="flex-1 p-10">
      <!-- Heading and Create New Button -->
      <HeaderSection
        :title="'List of Transactions'"
        :buttonText="'Add New Transaction'"
        @toggle-form="handleToggleForm"
      />

      <!-- Create/Update Transaction Form -->
      <GenericForm
        :showForm="showForm"
        :isEdit="isEdit"
        entityName="Transaction"
        :fields="transactionFields"
        :formData="newTransaction"
        @submit="handleFormSubmit"
      />

      <!-- List of Transactions -->
      <TableView
        :items="transactions"
        :fields="transactionDisplayFields"
        titleField="transaction_type"
        :showForm="showForm"
        @edit="editTransaction"
        @delete="deleteTransaction"
      />
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';
import HeaderSection from '@/components/Header.vue';
import GenericForm from '@/components/Forms.vue';
import TableView from '@/components/TableView.vue';

export default {
  components: {
    Sidebar,
    HeaderSection,
    GenericForm,
    TableView,
  },
  data() {
    return {
      transactions: null,
      books: [],
      members: [],
      newTransaction: {
        book_id: '',
        member_id: '',
        transaction_type: '',
      },
      showForm: false,
      isEdit: false,
      transactionToEdit: null,
      transactionFields: [
        {
          label: "Book",
          model: "book_id",
          type: "dropdown",
          options: [], // options to be populated dynamically
          required: true,
        },
        {
          label: "Member",
          model: "member_id",
          type: "dropdown",
          options: [], // options to be populated dynamically
          required: true,
        },
        {
          label: "Transaction Type",
          model: "transaction_type",
          type: "dropdown",
          options: [
            { value: "Issue", label: "Issue" },
            { value: "Return", label: "Return" },
          ],
          required: true,
        },
      ],
      transactionDisplayFields: [
        { label: "Book Name", model: "book_name" },
        { label: "Member Name", model: "member_name" },
        { label: "Transaction Type", model: "transaction_type" },
        { label: "Date", model: "date" },
      ],
    };
  },
  async mounted() {
    let login_status = localStorage.getItem("login_status");
    if (login_status == "Out" || login_status == undefined) {
      this.$router.push("/");
    }
    this.loadBooksAndMembers();
    this.loadTransactions();
  },
  methods: {
    async loadBooksAndMembers() {
      try {
        const [booksResponse, membersResponse] = await Promise.all([
          fetch(this.base_url + '/read/books'),
          fetch(this.base_url + '/read/members'),
        ]);

        const books = await booksResponse.json();
        const members = await membersResponse.json();

        this.books = books;
        this.members = members;

        // Populate the options in the form fields
        this.transactionFields.find(field => field.model === 'book_id').options = books.map(book => ({
          value: book.id,
          label: book.name,
        }));
        this.transactionFields.find(field => field.model === 'member_id').options = members.map(member => ({
          value: member.id,
          label: member.name,
        }));

      } catch (error) {
        console.error("Error fetching books and members:", error);
      }
    },
    async loadTransactions() {
      try {
        const response = await fetch(this.base_url + '/read/transactions');
        const transactions = await response.json();


        this.transactions = transactions.map(transaction => {
          const book = this.books.find(book => book.id === transaction.book_id);
          const member = this.members.find(member => member.id === transaction.member_id);

          return {
            ...transaction,
            book_name: book ? book.name : 'Unknown Book',
            member_name: member ? member.name : 'Unknown Member',
          };
        });

      } catch (error) {
        console.error("Error fetching transactions:", error);
      }
    },
    async deleteTransaction(id) {
      const request_body = { id: id };

      const request_options = {
        method: "POST",
        body: JSON.stringify(request_body),
        headers: {
          'Content-Type': 'application/json',
        },
      };

      const response = await fetch(this.base_url + '/delete/transactions', request_options);
      const result = await response.json();
      if (result.message == "Success") {
        this.loadTransactions();
      }
    },
    handleToggleForm() {
      this.showForm = !this.showForm;
      if (!this.showForm) {
        this.resetForm();
      }
    },
    editTransaction(transaction) {
      this.newTransaction = { ...transaction };
      this.transactionToEdit = transaction.id;
      this.isEdit = true;
      this.showForm = true;
    },
    resetForm() {
      this.newTransaction = { book_id: '', member_id: '', transaction_type: '' };
      this.isEdit = false;
      this.transactionToEdit = null;
    },
    async handleFormSubmit(formData) {
      this.newTransaction = { ...formData };
      if (this.isEdit) {
        await this.updateTransaction();
      } else {
        await this.createTransaction();
      }
    },
    async createTransaction() {
      const request_options = {
        method: "POST",
        body: JSON.stringify(this.newTransaction),
        headers: {
          'Content-Type': 'application/json',
        },
      };

      const response = await fetch(this.base_url + '/create/transactions', request_options);
      const result = await response.json();
      if (result.message == "Success") {
        this.loadTransactions();
        this.resetForm();
        this.showForm = false;
      }
    },
    async updateTransaction() {
      const request_body = { ...this.newTransaction, id: this.transactionToEdit };

      const request_options = {
        method: "POST",
        body: JSON.stringify(request_body),
        headers: {
          'Content-Type': 'application/json',
        },
      };

      const response = await fetch(this.base_url + '/update/transactions', request_options);
      const result = await response.json();
      if (result.message == "Success") {
        this.loadTransactions();
        this.resetForm();
        this.showForm = false;
      }
    },
    handleSearchResults(items) {
      this.transactions = items;
    }
  },
};
</script>
