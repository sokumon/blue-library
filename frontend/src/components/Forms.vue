<template>
  <!-- Create/Update Form -->
  <div v-if="showForm" class="mb-8 p-6 bg-white rounded-lg shadow-md border-4 border-blue-300">
    <h2 class="text-xl font-semibold text-gray-800 mb-4">{{ isEdit ? `Update ${entityName}` : `Add New ${entityName}` }}</h2>
    <!-- Dynamic Form Fields -->
    <div v-for="(field, index) in fields" :key="index" class="mb-4">
      <label :for="field.model" class="block text-gray-700 font-semibold mb-2">{{ field.label }}</label>

      <!-- Dropdown Field -->
      <select
        v-if="field.type === 'dropdown'"
        v-model="localFormData[field.model]"
        :id="field.model"
        class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:border-blue-500"
        :required="field.required || true"
      >
        <option v-for="option in field.options" :key="option.value" :value="option.value">
          {{ option.label }}
        </option>
      </select>

      <!-- Other Input Fields -->
      <input
        v-else
        v-model="localFormData[field.model]"
        :type="field.type || 'text'"
        :id="field.model"
        :min="field.type === 'number' ? '1' : null"
        class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:border-blue-500"
        :required="field.required || true"
      />
    </div>

    <!-- Submission Button -->
    <button
      @click="handleFormSubmit"
      class="px-4 py-2 bg-red-600 text-white text-sm rounded hover:bg-green-500 focus:outline-none"
    >
      {{ isEdit ? `Update ${entityName}` : `Add ${entityName}` }}
    </button>
  </div>
</template>

<script>
export default {
  name: "GenericForm",
  props: {
    showForm: {
      type: Boolean,
      default: false,
    },
    isEdit: {
      type: Boolean,
      default: false,
    },
    entityName: {
      type: String,
      default: "Item",
    },
    fields: {
      type: Array,
      required: true,
    },
    formData: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      localFormData: { ...this.formData },
    };
  },
  watch: {
    formData: {
      handler(newValue) {
        this.localFormData = { ...newValue };
      },
    },
  },
  methods: {
    handleFormSubmit() {
    if (this.isFormEmpty()) {
      this.$swal({
        title: 'Error!',
        text: 'The form cannot be empty. Please fill in all the required fields.',
        icon: 'error',
        confirmButtonText: 'OK'
      });
      return;
    }
    this.$emit("submit", { ...this.localFormData });
  },
  isFormEmpty() {
    return Object.values(this.localFormData).some(value => !value);
  },
  },
};
</script>
