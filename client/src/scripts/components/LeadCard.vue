<template>
    <div class="lead-card card">
        <div class="lead-detalhes">
            <p class="nome-lead">
                <svg xmlns="http://www.w3.org/2000/svg" width="15" height="17" viewBox="0 0 15 17" fill="none">
                    <path
                        d="M13.444 15.5V13.944C13.444 13.1189 13.1162 12.3276 12.5328 11.7442C11.9494 11.1608 11.1581 10.833 10.333 10.833H4.111C3.28591 10.833 2.49462 11.1608 1.91119 11.7442C1.32777 12.3276 1 13.1189 1 13.944V15.5"
                        stroke="#222222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path
                        d="M7 7.5C8.65685 7.5 10 6.15685 10 4.5C10 2.84315 8.65685 1.5 7 1.5C5.34315 1.5 4 2.84315 4 4.5C4 6.15685 5.34315 7.5 7 7.5Z"
                        stroke="#222222" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
                <span>{{ lead.nomeLead }}</span>
                <img class="block ml-auto" src="/static/img/temperatura-quente.svg" alt="Temperatura Lead">
            </p>
            <a class="telefone-lead" href="#">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" fill="none">
                    <path
                        d="M11.374 12.332C11.6408 12.332 11.8993 12.2322 12.0976 12.0503C12.3197 11.8466 12.4456 11.5587 12.4444 11.2573V9.65175C12.4578 9.10844 12.062 8.64127 11.5239 8.56535C11.0101 8.49758 10.5056 8.37191 10.02 8.19072C9.62886 8.04369 9.18791 8.13773 8.89078 8.43155L8.21111 9.11123C6.87127 8.34937 5.76191 7.24001 5.00005 5.90017L5.67972 5.22049C5.97354 4.92337 6.06759 4.48242 5.92055 4.09127C5.73937 3.60572 5.6137 3.10123 5.54593 2.58743C5.47074 2.05544 5.01285 1.66164 4.47558 1.66692H2.87005C2.5696 1.66721 2.2831 1.79375 2.08054 2.01566C1.87798 2.23756 1.77801 2.53438 1.80505 2.83361C1.98071 4.48784 2.54358 6.07742 3.44804 7.47359C4.26972 8.76667 5.36602 9.86297 6.6591 10.6846C8.04895 11.586 9.63084 12.1487 11.2777 12.3276C11.3099 12.3305 11.342 12.332 11.374 12.332ZM11.3741 13.832C11.2971 13.832 11.2193 13.8285 11.1426 13.8215C11.1336 13.8207 11.1246 13.8198 11.1156 13.8189C9.24713 13.6158 7.42604 12.9686 5.84856 11.9468C4.38404 11.0149 3.11763 9.74849 2.18576 8.28395C1.16019 6.69902 0.512772 4.86922 0.313441 2.992C0.312611 2.98421 0.311841 2.97641 0.311141 2.96861C0.246371 2.25184 0.487501 1.53591 0.972701 1.00438C1.45787 0.47287 2.1489 0.16762 2.8686 0.16692L4.48625 0.16687C5.75898 0.16687 6.85306 1.11724 7.03117 2.37752C7.03182 2.3821 7.03244 2.38669 7.03305 2.39128C7.08595 2.79235 7.18448 3.18788 7.3259 3.56687C7.64496 4.41561 7.48575 5.37335 6.92468 6.07477C7.2527 6.48548 7.62553 6.85832 8.03621 7.18636C8.49087 6.82088 9.05244 6.62224 9.64358 6.62224C9.95336 6.62224 10.2576 6.67755 10.5478 6.78664C10.9234 6.9268 11.3189 7.02533 11.72 7.07823C11.7245 7.07882 11.7289 7.07943 11.7334 7.08006C13.0185 7.26136 13.9654 8.37115 13.9444 9.66651V11.2542C13.9464 11.9753 13.643 12.6681 13.1116 13.1557C12.6363 13.5918 12.0192 13.832 11.3741 13.832Z"
                        fill="#222222" />
                </svg>
                <span>{{ lead.telefoneLead }}</span>
            </a>
            <div class="badge">
                <Badges :class="'badge-compra'" type="Compra" />
                <Badges :class="'badge-aluguel'" type="Aluguel" />
            </div>

            <div class="lead-footer mt-3 mb-3">
                <p>R$ 650.000</p>

                <!-- Se a imagem estiver disponível, exibe a imagem. -->
                <img v-if="userImage" :src="userImage" alt="Foto Usuário" />

                <!-- Se a imagem não estiver disponível, exibe as iniciais. -->
                <div v-else class="iniciais-usuario">{{ iniciaisUsuario }}</div>
            </div>
        </div>
    </div>
</template>
<script>
import Badges from '@/components/Badges';
export default {
    name: "LeadCard",
    components: {
        Badges,
    },
    props: {
        lead: {
            type: Object,
            required: true,
        },
    },
    data(){
        return{
            user: {
                primeiroNome: 'Igor',
                ultimoNome: 'Henrique',
                image: null,
            },
            leadsArray: [],
        }
    },
    methods: {
       
    },  
    computed: {
        userImage() {
            return this.user.image;
        },
        iniciaisUsuario() {
            return this.user.primeiroNome[0] + this.user.ultimoNome[0];
        },
    },
}
</script>