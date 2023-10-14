<template>
    <div class="interest-card">
      <div class="card-header" @click="toggleCollapse">
        <div class="grid grid-cols-3 gap-4 mt-3">
          <div>
            <p class="label-card mb-2">Tipo de Transação:</p>
            <p class="label-card mb-2">Código do anúncio:</p>
            <p class="label-card mb-2">Valor do imóvel: </p>
            <p class="label-card mb-2">Origem:</p>
            <p class="label-card mb-2">Entrada: </p>
          </div>
          <div class="col-span-2">
            <p class="content-card mb-2 ml-8">{{ tipoTransacao }}</p>
            <p class="content-card mb-2 ml-8">
              <a href="">
                {{ codigoAnuncio }}
                <svg class="inline" width="17" height="18" viewBox="0 0 17 18" fill="none"
                  xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M13.3 9.939V14.86C13.3 15.0754 13.2576 15.2886 13.1752 15.4876C13.0927 15.6866 12.9719 15.8674 12.8197 16.0197C12.6674 16.1719 12.4866 16.2927 12.2876 16.3752C12.0886 16.4576 11.8754 16.5 11.66 16.5H2.64C2.42455 16.5 2.21121 16.4575 2.01217 16.3751C1.81313 16.2926 1.63229 16.1717 1.47999 16.0193C1.32769 15.8669 1.20691 15.686 1.12455 15.4869C1.04219 15.2878 0.999869 15.0744 1 14.859V5.838C1 5.40304 1.17279 4.9859 1.48035 4.67834C1.7879 4.37078 2.20505 4.198 2.64 4.198H7.561"
                    stroke="#EC0000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                  <path d="M10.8398 1.73798H15.7608V6.65898" stroke="#EC0000" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round" />
                  <path d="M7 10.5L16 1.5" stroke="#EC0000" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round" />
                </svg>
              </a>
            </p>
            <p class="content-card mb-2 ml-8">{{ valorImovel }}</p>
            <p class="content-card mb-2 ml-8">{{ origem }}</p>
            <p class="content-card mb-2 ml-8">{{ entrada }}</p>
          </div>
        </div>
      </div>
      <hr class="mt-3 mb-3"/>


      <h3 class="font-bold mb-3 text-lg">Simulação de financiamento</h3>
      <div class="simulation" v-if="simulacaoFinanciamento">
        
        <button @click="solicitarCredito">Solicitar Crédito</button>
        <button @click="enviarWhatsapp">Enviar pelo WhatsApp</button>
      </div>
      <div v-else>
        <p class="label-card mt-4 mb-4">Nenhuma solicitação de crédito.</p>
        <button class="btn-red pl-3 pr-3 mb-4" @click="fazerSimulacao">Fazer Simulação</button>
      </div>
      <hr class="mt-3 mb-3">
      <div class="mt-4 mb-4">
        <button class="font-bold" @click="toggleCollapse">
        Sugestões de imóveis similares para o cliente
        <svg class="inline" width="12" height="7" viewBox="0 0 12 7" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12.0008 1.12L6.40078 7L0.800781 1.12L1.92078 0L6.40078 4.62L10.8808 0L12.0008 1.12Z" fill="#222222" />
        </svg>
      </button>
      </div>
      <transition name="fade">
        <div class="collapse__content" v-if="showCollapse">
          <div class="suggestions">
            <p></p>
          </div>
        </div>
      </transition>
    </div>
</template>
  
<script>
    export default {
      props: {
        tipoTransacao: String,
        codigoAnuncio: String,
        valorImovel: Number,
        origem: String,
        entrada: Number,
        simulacaoFinanciamento: Object,
      },
      data() {
        return {
          showCollapse: false,
        };
      },
      methods: {
        toggleCollapse() {
          this.showCollapse = !this.showCollapse;
        },
        fazerSimulacao() {
          this.$emit('fazer-simulacao');
        },
        solicitarCredito() {
          // Lógica para solicitar crédito aqui
        },
        enviarWhatsapp() {
          // Lógica para enviar pelo WhatsApp aqui
        },
      },
    };
</script>