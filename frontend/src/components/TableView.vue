<template>
    <div v-if="!showForm" class="overflow-x-auto">
      <table class="min-w-full bg-white border border-gray-300">
        <thead>
          <tr>
            <th v-for="(field, index) in fields" :key="index" class="py-2 px-4 bg-gray-200 border-b">
              {{ field.label }}
            </th>
            <th class="py-2 px-4 bg-gray-200 border-b">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in items" :key="item.id" class="border-b hover:bg-gray-100">
            <td v-for="(field, index) in fields" :key="index" class="py-2 px-4">
              {{ item[field.model] }}
            </td>
            <td class="py-2 px-4">
              <!-- Update Button -->
              <button
                @click="handleEdit(item)"
                class="px-3 py-1 bg-yellow-600 text-white text-sm rounded hover:bg-yellow-500 focus:outline-none mr-2"
              >
                Update
              </button>
              <!-- Delete Button -->
              <button
                @click="handleDelete(item.id)"
                class="px-3 py-1 bg-red-600 text-white text-sm rounded hover:bg-red-500 focus:outline-none"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: "TableView",
    props: {
      items: {
        type: Array,
        required: true,
      },
      fields: {
        type: Array,
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
  