<template>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold">{{ title }}</h1>
      <button
        @click="toggleForm()"
        class="px-4 py-2 bg-blue-600 text-white text-sm rounded hover:bg-blue-500 focus:outline-none"
      >
        {{ buttonText }}
      </button>
    </div>
</template>
  
<script>
  export default {
    name: "HeaderSection",
    props: {
      title: {
        type: String,
        default: "List of Books",
      },
      buttonText: {
        type: String,
        default: "Create New",
      },
    },
    methods: {
      toggleForm() {
        this.$emit("toggle-form");
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add any additional styling here if needed */
  </style>