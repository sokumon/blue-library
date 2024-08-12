<template>
    <div class="flex h-screen">
      <aside class="w-64 bg-blue-800">
        <div class="px-6 py-4 text-2xl font-semibold text-white"> <router-link 
                to="/dashboard"
              >
                Dashboard
              </router-link></div>
        <nav class="mt-6">
          <ul>
            <li class="mb-4">
              <router-link 
                to="/books" 
                class="block px-6 py-2 text-lg text-white rounded hover:bg-blue-700"
                active-class="bg-blue-600"
              >
                Books
              </router-link>
            </li>
            <li class="mb-4">
              <router-link 
                to="/members" 
                class="block px-6 py-2 text-lg text-white rounded hover:bg-blue-700"
                active-class="bg-blue-600"
              >
                Members
              </router-link>
            </li>
            <li class="mb-4">
              <router-link 
                to="/transactions" 
                class="block px-6 py-2 text-lg text-white rounded hover:bg-blue-700"
                active-class="bg-blue-600"
              >
                Transactions
              </router-link>
            </li>
          </ul>
        </nav>
      </aside>
      <div class="flex-1 p-10">
        <router-view />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Sidebar",
  };
  </script>
  
  <style scoped>
  /* Add custom styles here if needed */
  </style>
  