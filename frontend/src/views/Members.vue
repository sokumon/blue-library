<template>
  <div class="flex h-screen">
    <Sidebar />
    <div class="flex-1 p-10">
      <!-- Heading and Create New Button -->
      <HeaderSection
        :title="'List of Members'"
        :buttonText="'Add New Member'"
        @toggle-form="handleToggleForm"
      />
      
      <!-- Create/Update Member Form -->
      <GenericForm
        :showForm="showForm"
        :isEdit="isEdit"
        entityName="Member"
        :fields="memberFields"
        :formData="newMember"
        @submit="handleFormSubmit"
      />

      <!-- List of Members -->
      <TableView
        :items="members"
        :fields="memberFields"
        titleField="name"
        :showForm="showForm"
        @edit="editMember"
        @delete="deleteMember"
      />
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';
import HeaderSection from '@/components/Header.vue';
import GenericForm from '@/components/Forms.vue';
import Card from '@/components/Card.vue';
import SearchBar from '@/components/SearchBar.vue';
import TableView from '@/components/TableView.vue'

export default {
  components: {
    Sidebar,
    HeaderSection,
    GenericForm,
    Card,
    SearchBar,
    TableView
  },
  data() {
    return {
      members: null,
      newMember: {
        name: '',
        phoneno: '',
        active: 'Up',
        due: 0,
      },
      showForm: false,
      isEdit: false,
      memberToEdit: null,
      memberFields: [
        { label: "Name", model: "name", type: "text", required: true },
        { label: "Phone Number", model: "phoneno", type: "text", required: true },
        { label: "Active", model: "active", type: "text", required: true },
        { label: "Due Amount", model: "due", type: "number", required: false },
      ],
    };
  },
  async mounted() {
    let login_status = localStorage.getItem("login_status");
    if (login_status == "Out" || login_status == undefined) {
      this.$router.push("/");
    }
    this.loadMembers();
  },
  methods: {
    async loadMembers() {
      const response = await fetch(this.base_url + '/read/members');
      const members = await response.json();
      this.members = members;
    },
    async deleteMember(id) {
      const request_body = { id: id };

      const request_options = {
        method: "POST",
        body: JSON.stringify(request_body),
        headers: {
          'Content-Type': 'application/json',
        },
      };

      const response = await fetch(this.base_url + '/delete/members', request_options);
      const result = await response.json();
      if (result.message == "Success") {
        this.loadMembers();
      }
    },
    handleToggleForm() {
      this.showForm = !this.showForm;
      if (!this.showForm) {
        this.resetForm();
      }
    },
    editMember(member) {
      this.newMember = { ...member };
      this.memberToEdit = member.id;
      this.isEdit = true;
      this.showForm = true;
    },
    resetForm() {
      this.newMember = { name: '', phoneno: '', active: '', due: 0 };
      this.isEdit = false;
      this.memberToEdit = null;
    },
    async handleFormSubmit(formData) {
      this.newMember = { ...formData };
      if (this.isEdit) {
        await this.updateMember();
      } else {
        await this.createMember();
      }
    },
    async createMember() {
      const request_options = {
        method: "POST",
        body: JSON.stringify(this.newMember),
        headers: {
          'Content-Type': 'application/json',
        },
      };

      const response = await fetch(this.base_url + '/create/members', request_options);
      const result = await response.json();
      if (result.message == "Success") {
        this.loadMembers();
        this.resetForm();
        this.showForm = false;
      }
    },
    async updateMember() {
      const request_body = { ...this.newMember, id: this.memberToEdit };

      const request_options = {
        method: "POST",
        body: JSON.stringify(request_body),
        headers: {
          'Content-Type': 'application/json',
        },
      };

      const response = await fetch(this.base_url + '/update/members', request_options);
      const result = await response.json();
      if (result.message == "Success") {
        this.loadMembers();
        this.resetForm();
        this.showForm = false;
      }
    },
    handleSearchResults(items) {
      this.members = items;
    }
  },
};
</script>
