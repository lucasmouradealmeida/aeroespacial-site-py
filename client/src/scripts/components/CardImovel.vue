<template>
    <div class="card-imovel">
      <div class="imagem">
        <img class="mr-3" :src="imovel.imagemUrl" alt="">
      </div>
      <div class="info">
        <div class="codigo">{{ imovel.codigo }}</div>
        <div class="endereco">{{ imovel.endereco }}</div>
        <div class="descricao">{{ imovel.descricao }}</div>
        <div class="preco">{{ imovel.preco }}</div>
      </div>
      <div class="delete-button" @click="apagarImovel">
        <svg class="inline" width="14" height="15" viewBox="0 0 14 15" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M13 1.5L1 13.5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
          <path d="M1 1.5L13 13.5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </div>
    </div>
</template>
<script>
export default {
  name: "CardImovel",
  props: {
    imovel: {
      type: Object,
      required: true,
    },
  },
  methods: {
    apagarImovel() {
      this.$emit('apagar-imovel', this.imovel);
    },
  },
};
</script>