<template>
    <div class="flex h-screen">
      <Sidebar />
      <div class="flex-1 p-10">
        Welcome to the library
      </div>
    </div>
  </template>
  
  <script>
  import Sidebar from '@/components/Sidebar.vue';
  
  export default {
    components: {
      Sidebar,
    },
    mounted() {
      let login_status = localStorage.getItem("login_status");
      if (login_status == "Out" || login_status == undefined) {
        this.$router.push("/");
      }
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles here if needed */
  </style>
  