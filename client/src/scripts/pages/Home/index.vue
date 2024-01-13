<template>
    <div class="main">
        <div class="menu">
            <div class="logo">
                <svg class="ml-6 w-6 h-6 rotate-45 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                    <path d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z"/>
                </svg>
            </div>
            <div class="pages">
                <a :class="['label', prefix.home]" href="#home" @click="menu('home')">Home</a>
                <a :class="['label', prefix.explore]" href="#explore" @click="menu('explore')">Explore</a>
                <div class="ml-4 mr-4 cursor-pointer" @click="userModal ? userModal = false : userModal = true">
                    <svg class="w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19a9 9 0 1 0 0-18 9 9 0 0 0 0 18Zm0 0a8.949 8.949 0 0 0 4.951-1.488A3.987 3.987 0 0 0 11 14H9a3.987 3.987 0 0 0-3.951 3.512A8.948 8.948 0 0 0 10 19Zm3-11a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
                    </svg>
                </div>
            </div>
        </div>

        <div class="content">
            <div v-show="home" class="content-home">
                <div class="pagetitle">
                    <label class="title">Engenharia Aeroespacial</label>
                </div>

                <div class="container">
                    <div class="title">
                        Sobre
                    </div>
                    <div class="divider"></div>

                    <div class="paragraph text-justify indent-12">
                        O Engenheiro Aeroespacial incorpora o estado da arte da engenharia aplicada ao projeto, análise,
                        construção e testes de sistemas associados com o Setor Aeroespacial, envolvendo aeronaves, foguetes
                        e satélites artificiais. Seus conhecimentos incluem sistemas de propulsão, comunicação, controle de
                        aeronaves, navegação e interação homem-máquina.

                        As tecnologias que este profissional utilizará são complementadas com noções de sensores e
                        instrumentação de bordo, de materiais especiais, de aerodinâmica e de controle de temperatura.
                        A formação na UFABC possibilita amplos conhecimentos de física, química, matemática, computação
                        e noções fundamentais de engenharia.
                    </div>
                    
                    <div class="title">
                        Perfil do profissional
                    </div>
                    <div class="divider"></div>

                    <div class="paragraph text-justify indent-12">

                        É o engenheiro apto a atuar em modelagem, controle, projeto, análise, construção e testes de sistemas
                        no setor aeroespacial

                        Atuação:

                        Pesquisa científica nas várias entidades que estudam aeronaves e veículos espaciais no Brasil
                        (UFABC, INPE, CTA, AEB,...)

                        Indústria: qualquer empresa que presta serviço ao setor aeroespacial
                        (EMBRAER, AVIBRAS, Helibrás, etc).

                        Empresário autônomo como fabricante/fornecedor de peças, componentes, serviços e soluções
                        para o mercado aeroespacial brasileiro.
                    </div>
                    
                    <div class="title">
                        Atuação profissional
                    </div>
                    <div class="divider"></div>

                    <div class="paragraph text-justify indent-12">

                        Desenvolvimento e a avaliação de sistemas diversos (computação, eletrônicos, mecânicos, hidráulicos)
                        associados a aeronaves, foguetes e sondas espaciais.

                        Desenvolvimento de satélites artificiais (modelagem, controle,...) para diversas finalidades (satélites
                        meteorológicos, de comunicação, observacionais)

                        Sistemas de propulsão, comunicação, controle de atitude, navegação, interação homem-máquina,...

                        Sensores e instrumentação de bordo, materiais especiais, aerodinâmica, controle de temperatura, controle
                        de vibração, em sistemas diversos associados a aeronaves, foguetes,...

                    </div>

                    <div class="title">
                        Formação na UFABC
                    </div>
                    <div class="divider"></div>

                    <div class="paragraph text-justify indent-12">

                        Para a sua formação como Engenheiro Espacial, nosso curso oferece as seguintes disciplinas:
                        Aerodinâmica, Aeroelasticidade, Astrodinâmica, Aviônica, Ciência dos Materiais, Controle de aeronaves,
                        Desempenho, Ensaios em vôo, Estabilidade de vôo, Helicópteros, Instrumentação e sistemas, Propulsão,
                        Sistemas de radar. Ao longo do curso, também serão estudados: Circuitos elétricos, Estruturas, Gestão,
                        Matemática, Mecânica clássica, Mecânica dos Ruídos, Mecânica dos sólidos, Probabilidades e Estatística, Telecomunicações, Termodinâmica e Vibrações e ruído. 
                    </div>                     
                </div>

            </div>
            <div v-show="explore" class="content-explore">
                <div class="pagetitle">
                    <label class="title">Explore</label>
                </div>

                <div class="cards">
                    <div class="card cursor-pointer" @click="modalSolarSystema = true">
                        <div class="cardback"></div>
                        <svg @click="modalSolarSystema = true" class="expandcard w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>  
                        <div class="cardcontent">
                            <div>Sistema Solar</div>
                        </div>
                    </div>
                    <div class="card cursor-pointer" @click="modalPosicionamento = true">
                        <div class="cardback"></div>
                        <svg @click="modalPosicionamento = true" class="expandcard w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>  
                        <div class="cardcontent">
                            <div>Posicionamento de Satélites</div>
                        </div>
                    </div>
                    <div class="card cursor-pointer" @click="modalManobras = true">
                        <div class="cardback"></div>
                        <svg @click="modalManobras = true" class="expandcard w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>
                        <div class="cardcontent">
                            <div>Manobras Orbitais</div>
                        </div>
                    </div>
                    <div class="card cursor-pointer" @click="modalLagrange = true" >
                        <div class="cardback"></div>
                        <svg @click="modalLagrange = true" class="expandcard w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>
                        <div class="cardcontent">
                            <div>Pontos de Lagrange</div>
                        </div>
                    </div>
                </div>

            </div>


        </div>
    </div>

    <UserModal v-show="userModal">
        <template v-slot:header>
            <div></div>
        </template>

        <template v-slot:body>
            <div class="flex flex-row mb-4">
                <div :class="'cursor-pointer w-1/2 flex justify-center signin' + signin" @click="signin = true, register = false">
                    <svg class="w-6 h-6 blue-icon mr-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 18">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 8h6m-3 3V5m-6-.5a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0ZM5 11h3a4 4 0 0 1 4 4v2H1v-2a4 4 0 0 1 4-4Z"/>
                    </svg>
                    <a class="font-bold">Sign in</a>
                </div>

                <div :class="'cursor-pointer w-1/2 flex justify-center register' + register"  @click="signin = false, register = true">
                    <svg class="w-6 h-6 blue-icon mr-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 15">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 7.5h11m0 0L8 3.786M12 7.5l-4 3.714M12 1h3c.53 0 1.04.196 1.414.544.375.348.586.82.586 1.313v9.286c0 .492-.21.965-.586 1.313A2.081 2.081 0 0 1 15 14h-3"/>
                    </svg>
                    <a class="font-bold">Register</a>
                </div>
            </div>

            <div>
                <div class="flex flex-col justify-center" v-if="signin">
                    <a class="font-semibold mb-2 mt-2">Username</a>
                    <input class="input rounded-md p-1 mb-2" type="text">

                    <a class="font-semibold mb-2 mt-2">Password</a>
                    <input class="input rounded-md p-1 mb-2" type="password">

                    <a class="flex cursor-pointer justify-center font-semibold mt-1 mb-3">Forgot Password</a>

                    <button class="border-2 border-black rounded-lg p-1 font-bold">Sign in</button>
                </div>

                <div class="flex flex-col justify-center" v-if="register">
                    <a class="font-semibold mb-2 mt-2">Username</a>
                    <input class="input rounded-md p-1 mb-2" type="text">

                    <a class="font-semibold mb-2 mt-2">Password</a>
                    <input class="input rounded-md p-1 mb-2" type="password">

                    <a class="font-semibold mb-2 mt-2">Confirm Password</a>
                    <input class="input rounded-md p-1 mb-2" type="password">

                    <button class="border-2 border-black rounded-lg p-1 font-bold mt-3">Register</button>
                </div>
            </div>
        </template>

        <template v-slot:footer>
            <div></div>
        </template>
    </UserModal>

    <Modal v-show="modalSolarSystema">
        <template v-slot:header>
            <svg @click="modalSolarSystema = false" class="cursor-pointer w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                <path stroke="#222222" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m13 7-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
            </svg>
        </template>

        <template v-slot:body>
            <div></div>
        </template>

        <template v-slot:footer>
            <div></div>
        </template>
    </Modal>

    <Modal v-show="modalPosicionamento">
        <template v-slot:header>
            <svg @click="modalPosicionamento = false" class="cursor-pointer w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                <path stroke="#222222" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m13 7-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
            </svg>
        </template>

        <template v-slot:body>
            <div></div>
        </template>

        <template v-slot:footer>
            <div></div>
        </template>
    </Modal>

    <Modal v-show="modalManobras">
        <template v-slot:header>
            <svg @click="modalManobras = false" class="cursor-pointer w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                <path stroke="#222222" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m13 7-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
            </svg>
        </template>

        <template v-slot:body>
            <div></div>
        </template>

        <template v-slot:footer>
            <div></div>
        </template>
    </Modal>


    <Modal v-show="modalLagrange">
        <template v-slot:header>
            <svg @click="modalLagrange = false" class="cursor-pointer w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                <path stroke="#222222" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m13 7-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
            </svg>
        </template>

        <template v-slot:body>
            <div></div>
        </template>

        <template v-slot:footer>
            <div></div>
        </template>
    </Modal>


</template>
<script>
import Modal from '@/components/Modal'
import UserModal from '@/components/UserModal'

export default {
    name: "Home",
    components: {
        UserModal,
        Modal,

    },
    data() {
        return {
            userModal: false,
            modalSolarSystema: false,
            modalPosicionamento: false,
            modalManobras: false,
            modalLagrange: false,
            prefix:{
                home: 'selected',
                explore: '',
            },
            home: true,
            explore: false,
            signin: true,
            register: false,
        }
    },
    created(){
        window.location.hash = 'home'
        window.addEventListener('popstate', () => {
            const hash = window.location.hash.substring(1)

            const menu = ['home', 'explore']

            menu.forEach((item) => {
                this.prefix[item] = ''
                this[item] = false
            })

            this[hash] = true
            this.prefix[hash] = 'selected'
        })
    },
    methods:{
        menu(ref){
            this.userModal = false

            const menu = ['home', 'explore']

            menu.forEach((item) => {
                this.prefix[item] = ''
                this[item] = false
            })

            this.prefix[ref] = 'selected'
            this[ref] = true
        },
    }
}
</script>