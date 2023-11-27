<template>
  <div class="modal-backdrop">
    <div class="modal-back">
      <header class="modal-header">
        <slot name="header">This is the default title!</slot>
      </header>

      <section class="modal-body">
        <slot name="body">This is the default body!</slot>
      </section>

      <footer class="modal-footer">
        <slot name="footer">This is the default footer!</slot>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  methods: {
    close() {
      this.$emit('close')
    }
  }
}
</script>
