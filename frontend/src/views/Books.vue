<template>
  <div class="flex h-screen">
    <Sidebar />
    <div class="flex-1 p-10">

      <HeaderSection
      :title="'List of Books'"
      :buttonText="'Create New Book'"
      @toggle-form="handleToggleForm"
        />


      <SearchBar class="my-4" :showForm="showForm" @results="handleSearchResults" />
      
      <GenericForm
      :showForm="showForm"
    :isEdit="isEdit"
    entityName="Book"
    :fields="bookFields"
    :formData="newBook"
    @submit="handleFormSubmit"
  />

      <!-- List of Books -->
      <Card
        :items="books"
        :fields="bookFields"
        titleField="name"
        :showForm="showForm"
        @edit="editBook"
        @delete="deleteBook"
      />

    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';
import HeaderSection from '@/components/Header.vue';
import GenericForm from '@/components/Forms.vue';
import Card from '@/components/Card.vue'
import SearchBar from '@/components/SearchBar.vue'

export default {
  components: {
    Sidebar,
    HeaderSection,
    GenericForm,
    Card,
    SearchBar
  },
  data() {
    return {
      books: null,
      newBook: {
        name: '',
        author: '',
        genre: '',
        isbn: '',
        quantity: 1,
      },
      showForm: false,
      isEdit: false,
      bookToEdit: null,
      bookFields: [
        { label: "Name", model: "name", type: "text", required: true },
        { label: "Author", model: "author", type: "text", required: true },
        { label: "Genre", model: "genre", type: "text", required: true },
        { label: "ISBN", model: "isbn", type: "text", required: true },
        { label: "Quantity", model: "quantity", type: "number", required: true },
      ],
    };
  },
  async mounted() {
    let login_status = localStorage.getItem("login_status");
    if (login_status == "Out" || login_status == undefined) {
      this.$router.push("/");
    }
    this.loadBooks();
  },
  methods: {
    async loadBooks() {
      const response = await fetch(this.base_url + '/read/books');
      const books = await response.json();
      this.books = books;
    },
    async deleteBook(id) {
      const request_body = { id: id };

      const request_options = {
        method: "POST",
        body: JSON.stringify(request_body),
        headers: {
          'Content-Type': 'application/json',
        },
      };

      const response = await fetch(this.base_url + '/delete/books', request_options);
      const result = await response.json();
      if (result.message == "Success") {
        this.loadBooks();
      }
    },
    handleToggleForm() {
      this.showForm = !this.showForm;
      if (!this.showForm) {
        this.resetForm();
      }
    },
    editBook(book) {
      this.newBook = { ...book };
      this.bookToEdit = book.id;
      this.isEdit = true;
      this.showForm = true;
    },
    resetForm() {
      this.newBook = { name: '', author: '', genre: '', isbn: '', quantity: 1 };
      this.isEdit = false;
      this.bookToEdit = null;
    },
    async handleFormSubmit(formData) {
      this.newBook = { ...formData };
      if (this.isEdit) {
        await this.updateBook();
      } else {
        await this.createBook();
      }
    },
    async createBook() {
      const request_options = {
        method: "POST",
        body: JSON.stringify(this.newBook),
        headers: {
          'Content-Type': 'application/json',
        },
      };

      const response = await fetch(this.base_url + '/create/books', request_options);
      const result = await response.json();
      if (result.message == "Success") {
        this.loadBooks();
        this.resetForm();
        this.showForm = false;
      }
    },
    async updateBook() {
      const request_body = { ...this.newBook, id: this.bookToEdit };

      const request_options = {
        method: "POST",
        body: JSON.stringify(request_body),
        headers: {
          'Content-Type': 'application/json',
        },
      };

      const response = await fetch(this.base_url + '/update/books', request_options);
      const result = await response.json();
      if (result.message == "Success") {
        this.loadBooks();
        this.resetForm();
        this.showForm = false;
      }
    },
    handleSearchResults(results){
      if (!results){
        this.loadBooks()
      }
      this.books = results.books
    }
  },
};
</script>
