<template>
    <div class="main">
        <div class="menu">
            <div class="logo">
                <svg class="ml-6 w-6 h-6 rotate-45 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                    <path d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z"/>
                </svg>
            </div>
            <div class="pages">
                <a :class="['label', prefix.home]" href="#home" @click="menu('home')">Home</a>
                <a :class="['label', prefix.explore]" href="#explore" @click="menu('explore')">Explore</a>
                <div class="ml-4 mr-4 cursor-pointer" @click="userModal ? userModal = false : userModal = true">
                    <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
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
                    <div class="card">
                        <svg @click="modalSolarSystema = true" class="expandcard w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>  
                    </div>
                    <div class="card">
                        <svg @click="modalPosicionamento = true" class="expandcard w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>  
                    </div>
                    <div class="card">
                        <svg @click="modalManobras = true" class="expandcard w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>  
                    </div>
                    <div class="card">
                        <svg @click="modalLagrange = true" class="expandcard w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>  
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
            <div></div>
        </template>

        <template v-slot:footer>
            <div></div>
        </template>

    </UserModal>

</template>
<script>
import UserModal from '@/components/UserModal'

export default {
    name: "Home",
    components: {
        UserModal,

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

<style lang="scss">

.main{
    width: 100%;
}

html{
    overflow: hidden;
}

.expandcard{
    position: absolute;
    top: 30px;
    right: 30px;
    cursor: pointer;
}

.container{
    display: flex;
    flex-wrap: wrap;
    color: #d3d3d3;
    font-size: 20px;
    margin-bottom: 200px;

    .title{
        width: 100%;
        font-size: 30px;
        font-weight: 900;
        color: #d3d3d3;
        margin-top: 60px;
    }

    .divider{
        width: 100%;
        height: 1px;
        background-color: #d3d3d3;
        margin-bottom: 20px;
    }
}

.content{
    height: 100vh;
    background-color: #222222;
    overflow: auto;
}

.pagetitle{
    display: flex;
    flex-direction: column;

    .title{
        width: fit-content;
        font-size: 40px;
        font-weight: 900;
        color: #324AB2;
        margin: 20px;
    }
}

.cards{
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    margin-bottom: 100px;
    margin-top: 20px;

    .card{
        width: 350px;
        height: 300px;
        margin: 20px;
        background-color: rgba(211, 211, 211, 0.3);
        filter: drop-shadow(0px 10px 10px rgba(0, 0, 0, 0.25));
        border-radius: 25px;
    }
}


.menu{
    display: flex;
    align-items: center;
    gap: 20px;
    height: 80px;
    background-color: #222222;
    

    .logo{
        width: 50%;
        justify-content: flex-start;
        font-size: 20px;
        font-weight: 700;
        color: #fff;
        margin-left: 20px;
    }

    .pages{
        display: flex;
        width: 50%;
        align-items: center;
        justify-content: flex-end;
        gap: 20px;
        margin-right: 20px;

        .label{
            width: fit-content;
            font-size: 20px;
            font-weight: 800;
            color: #fff;
            cursor: pointer;
        }

        .selected{
            color: #324AB2
        }

    }

}

</style>