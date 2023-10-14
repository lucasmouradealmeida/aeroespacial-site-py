<template>
  <div>
    <div class="card-component mt-2" v-for="(interest, index) in interessesLead" :key="index">
      <h3 class="font-bold mb-3 text-lg">Interesse #{{ index + 1 }}</h3>
      <CardInteresse :tipoTransacao="interest.tipoTransacao" :codigoAnuncio="interest.codigoAnuncio"
        :valorImovel="interest.valorImovel" :origem="interest.origem" :entrada="interest.entrada"
        :simulacaoFinanciamento="interest.simulacaoFinanciamento" @fazer-simulacao="iniciarSimulacao(index)" />
    </div>
    <button class="btn-adicionarInteresse mt-2" @click="modalInteresse = true">
      <svg class="inline" width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M17 1.5H3C1.89543 1.5 1 2.39543 1 3.5V17.5C1 18.6046 1.89543 19.5 3 19.5H17C18.1046 19.5 19 18.6046 19 17.5V3.5C19 2.39543 18.1046 1.5 17 1.5Z"
          stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        <path d="M10 6.5V14.5" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        <path d="M6 10.5H14" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
      </svg>
      Adicionar Interesse
    </button>

    <Modal v-show="modalInteresse" @close="modalInteresse = false">
      <template v-slot:header>
        <div class="modal-close">
            <button :class="'fecharModal mt-4'" @click="modalInteresse = false">
                <svg width="14" height="15" viewBox="0 0 14 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M13 1.5L1 13.5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M1 1.5L13 13.5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
            </button>
        </div>

        <h2 class="modal-title">Adicionar Imóvel de Interesse</h2>
      </template>

      <template v-slot:body>
        <form>
          <div class="mt-8">
            <label class="label-default" for="codImovel">Código do Imóvel</label>
            <input class="w-full mt-3" type="text" name="codigoImovel" id="codImovel">
          </div>
        </form>

        <CardImovel :imovel="imovel" @apagar-imovel="handleApagarImovel" />
      </template>

      <template v-slot:footer>
        <div class="btn-block w-full">
          <button class="btn-red w-full" @click="adicionarInteresse">Adicionar</button>
        </div>
      </template>

    </Modal>

  </div>
</template>
  
<script>
  import CardInteresse from '@/components/CardInteresse.vue';
  import Modal from '@/components/Modal';
  import CardImovel from '@/components/CardImovel';
  
  export default {
    components: {
      CardInteresse,
      Modal,
      CardImovel,
    },
    data() {
      return {
        interessesLead: [],
        modalInteresse: false,
        imovel: {
          codigo: 'Cod.123456',
          endereco: 'Rua Américo Brasiliense, 123 - Chácara Santo Antônio, São Paulo',
          descricao: 'Lindo imóvel com vista para o mar',
          preco: 'R$ 500.000,00',
          imagemUrl: '/static/img/thumb.png',
        }
      };
    },
    methods: {
      adicionarInteresse() {
        this.interessesLead.push({
          tipoTransacao: 'Venda',
          codigoAnuncio: '12345',
          valorImovel: 200000,
          origem: 'Online',
          entrada: 40000,
          simulacaoFinanciamento: null,
        });
      },
      iniciarSimulacao(index) {
        // Função para calculo de simulação
      },
      handleApagarImovel(imovel) {
        // Função para apagar o imóvel selecionado.
      },
    },
  };
</script>
<style lang="scss" scoped>
@import "../../../styles/pages/perfilLead";

.btn-red{
    display: flex;
    width: 100%;
    padding: 20px;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}

</style>