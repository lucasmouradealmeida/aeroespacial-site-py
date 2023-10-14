<template>
    <div></div>
</template>
  
<script>
  export default {
    props: {
      type: { type: String, default: 'info' },
      title: { type: String, default: '' },
      message: { type: String, default: '' },
    },
    watch: {
      type: 'displayNotification',
      title: 'displayNotification',
      message: 'displayNotification',
    },
    mounted() {
      this.displayNotification();
    },
    methods: {
      displayNotification() {
        this.$notify({
          group: 'alerts',
          title: this.title,
          text: this.message,
          type: this.type,
        });
      },
    },
  };
</script>

<style lang="scss">
.vue-notification {
  padding: 10px;
  margin: 0 5px 5px;
 
  font-size: 12px;
 
  color: #ffffff;
  background: #44A4FC;
  border-left: 5px solid #187FE7;
 
  &.warn {
    background: #ffb648;
    border-left-color: #f48a06;
  }
 
  &.error {
    background: #E54D42;
    border-left-color: #B82E24;
  }
 
  &.success {
    background: #68CD86;
    border-left-color: #42A85F;
  }
}
</style>