<template>
    <div :class="['badge', type]">
      {{ content }}
    </div>
</template>
<script>
export default {
  name: 'Badges',
  props: {
    type: {
      type: String,
      required: true,
      validator: value => ['Compra', 'Aluguel'].includes(value),
    },
  },
  computed: {
    content() {
      return this.type;
    },
  },
};
</script>