<template>
    <div class="breadcrumb">
       <h1 class="titulo-breadcrumb">{{ title }}</h1>
    </div>
</template>
<script>
export default {
  name: 'Breadcrumb',
  props: {
    title: {
      type: String,
      required: true
    }
  }
};
</script>
<style>
    
</style>

<!-- 
Para realizar a inclusão do template de breadcrumbs, importe para o componente pai e insira no seguinte formato: <Breadcrumb title="Dashboard" /> 
-->