<template>
  <div v-if="!showForm" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <div
      v-for="item in items"
      :key="item.id"
      class="bg-white shadow-md rounded-lg p-6 border-4 border-blue-300"
    >
      <h2 class="text-xl font-semibold text-gray-800 mb-2">{{ item[titleField] }}</h2>
      <div v-for="(field, index) in fields" :key="index" class="text-gray-600">
        <strong>{{ field.label }}:</strong> {{ item[field.model] }}
      </div>
      <!-- Update Button -->
      <button
        @click="handleEdit(item)"
        class="px-3 py-1 mx-4 my-4 bg-yellow-600 text-white text-sm rounded hover:bg-yellow-500 focus:outline-none"
      >
        Update
      </button>
      <!-- Delete Button -->
      <button
        @click="handleDelete(item.id)"
        class="px-3 py-1 mx-4  my-4 bg-red-600 text-white text-sm rounded hover:bg-red-500 focus:outline-none"
      >
        Delete
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    items: {
      type: Array,
      required: true,
    },
    fields: {
      type: Array,
      required: true,
    },
    titleField: {
      type: String,
      required: true,
    },
    showForm: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    handleEdit(item) {
      this.$emit("edit", item);
    },
    handleDelete(itemId) {
      this.$emit("delete", itemId);
    },
  },
};
</script>