<template>
  <div class="relative" v-if="!showForm">
    <input
      type="text"
      v-model="query"
      @input="handleInput"
      class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:border-blue-500"
      placeholder="Search..."
    />
    <div v-if="loading" class="absolute top-0 right-0 mt-2 mr-4">
      <svg class="animate-spin h-5 w-5 text-blue-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.964 7.964 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  props: {
    showForm: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      query: "",
      loading: false,
      debounceTimeout: null,
    };
  },
  methods: {
    handleInput() {
      clearTimeout(this.debounceTimeout);
      this.debounceTimeout = setTimeout(() => {
        this.search();
      }, 500); // Delay API call by 500ms
    },
    async search() {
      if (this.query.trim() === "") {
        this.$emit("results", []);
        return;
      }

      this.loading = true;

      try {
        const response = await fetch(`${this.base_url}/search?search=${this.query}`);
        const results = await response.json();
        this.$emit("results", results);
      } catch (error) {
        console.error("Search API call failed:", error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
