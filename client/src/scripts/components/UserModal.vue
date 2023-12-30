<template>
      <div class="usermodal">
            <div class="modalarrow"></div>
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
  </template>
  
  <script>
  export default {
    name: 'UserModal',
    methods: {

    }
  }
  </script>
  