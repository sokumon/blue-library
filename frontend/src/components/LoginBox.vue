<template>
    <div class="flex justify-center items-center min-h-screen bg-blue-400">
      <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
        <h2 class="text-2xl font-bold text-center text-gray-800">Login</h2>
        <form @submit.prevent="login">
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
            <input 
              v-model="username" 
              id="username" 
              type="text" 
              required 
              class="w-full px-3 py-2 mt-1 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>
          <div class="mt-4">
            <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
            <input 
              v-model="password" 
              id="password" 
              type="password" 
              required 
              class="w-full px-3 py-2 mt-1 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>
          <button 
            type="submit"
            class="w-full px-4 py-2 mt-6 text-white bg-indigo-600 rounded-lg hover:bg-indigo-500 focus:outline-none focus:bg-indigo-700"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '', // Replace with your actual base URL
      };
    },
    methods: {
      async login() {
        console.log("Logging in with", this.username, this.password);
        
        let request_body = {
          username: this.username,
          password: this.password,
        };
        
        let request_options = {
          method: "POST",
          body: JSON.stringify(request_body),
          headers: {
            'Content-Type': 'application/json',
          },
        };
        
        try {
          const response = await fetch(this.base_url + '/login', request_options);
          const login = await response.json();
          if (login.code == 200){
            localStorage.setItem("login_status","In")
            this.$router.push('/dashboard')
          }
        } catch (error) {
          console.error("Error during login:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styles here if needed */
  </style>
  