<template>
    <div class="main">
        <div class="menu">
            <div class="logo flex flex-row">
                <svg fill="#ffffff" class="ml-6 mt-6 w-10 h-10 rotate-90 text-white" version="1.1" id="Icons" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                    viewBox="0 0 32 32" xml:space="preserve">
                    <g>
                        <path d="M16,9c-3.9,0-7,3.1-7,7s3.1,7,7,7s7-3.1,7-7S19.9,9,16,9z"/>
                        <path d="M27.7,8.3C27.9,7.9,28,7.5,28,7c0-1.7-1.3-3-3-3c-0.5,0-0.9,0.1-1.3,0.3C21.4,2.8,18.8,2,16,2C8.3,2,2,8.3,2,16
                            s6.3,14,14,14s14-6.3,14-14C30,13.2,29.2,10.6,27.7,8.3z M16,28C9.4,28,4,22.6,4,16S9.4,4,16,4c2.2,0,4.4,0.6,6.3,1.8
                            C22.1,6.1,22,6.6,22,7c0,1.7,1.3,3,3,3c0.4,0,0.9-0.1,1.2-0.3c1.2,1.9,1.8,4,1.8,6.3C28,22.6,22.6,28,16,28z"/>
                    </g>
                </svg>
            </div>
            <div class="pages">
                <a :class="['label', prefix.home]" href="#home" @click="menu('home')">Home</a>
                <a :class="['label', prefix.explore]" href="#explore" @click="menu('explore')">Explore</a>
                <!-- <div class="ml-4 mr-4 cursor-pointer" @click="userModal ? userModal = false : userModal = true">
                    <svg class="w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19a9 9 0 1 0 0-18 9 9 0 0 0 0 18Zm0 0a8.949 8.949 0 0 0 4.951-1.488A3.987 3.987 0 0 0 11 14H9a3.987 3.987 0 0 0-3.951 3.512A8.948 8.948 0 0 0 10 19Zm3-11a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
                    </svg>
                </div> -->
            </div>
        </div>

        <div class="content">
            <div v-show="home" class="content-home">
                <div class="pagetitle">
                    <label class="title">Project ORION</label>
                </div>

                <div class="container">
                    <div class="title">
                        Sobre
                    </div>
                    <div class="divider"></div>

                    <div class="paragraph text-justify indent-12">
                        Este projeto tem como intuito passar alguns dos conhecimentos aprendidos ao longo da graduação em Engenheira Aeroespacial. 
                        Campo que incorpora o estado da arte da engenharia aplicada ao projeto, análise,
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
                    <div class="card cursor-pointer" @click="modalPousoLunar = true">
                        <div class="cardback"></div>
                        <svg @click="modalPousoLunar = true" class="expandcard w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>  
                        <div class="cardcontent">
                            <div>Pouso Lunar</div>
                        </div>
                    </div>

                    <div class="card cursor-pointer" @click="modalCelestrak = true">
                        <div class="cardback"></div>
                        <svg @click="modalCelestrak = true" class="expandcard w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>  
                        <div class="cardcontent">
                            <div>Two Lines</div>
                        </div>
                    </div>

                    <!-- <div class="card cursor-pointer" @click="modalSolarSystema = true">
                        <div class="cardback"></div>
                        <svg @click="modalSolarSystema = true" class="expandcard w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>  
                        <div class="cardcontent">
                            <div>Sistema Solar</div>
                        </div>
                    </div> -->

                    <!-- <div class="card cursor-pointer" @click="modalPosicionamento = true">
                        <div class="cardback"></div>
                        <svg @click="modalPosicionamento = true" class="expandcard w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>  
                        <div class="cardcontent">
                            <div>Posicionamento de Satélites</div>
                        </div>
                    </div> -->

                    <!-- <div class="card cursor-pointer" @click="modalManobras = true">
                        <div class="cardback"></div>
                        <svg @click="modalManobras = true" class="expandcard w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>
                        <div class="cardcontent">
                            <div>Manobras Orbitais</div>
                        </div>
                    </div> -->

                    <!-- <div class="card cursor-pointer" @click="modalLagrange = true" >
                        <div class="cardback"></div>
                        <svg @click="modalLagrange = true" class="expandcard w-6 h-6 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 16 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 1h4m0 0v4m0-4-5 5.243M5 15H1m0 0v-4m0 4 5.243-5"/>
                        </svg>
                        <div class="cardcontent">
                            <div>Pontos de Lagrange</div>
                        </div>
                    </div> -->
                </div>

            </div>


        </div>
    </div>


    <!-- Página do Pouso Lunar -->

    <Modal v-show="modalPousoLunar">
        <template v-slot:header>
            <svg @click="modalPousoLunar = false" class="cursor-pointer w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                <path stroke="#222222" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m13 7-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
            </svg>
        </template>

        <template v-slot:body>
            <div class="font-bold text-3xl mb-8">Pouso Lunar</div>

            <div class="flex flex-row items-center mt-8">
                <div @click="contentHS('cont')" class="w-6 h-6 black cursor-pointer cont rotate-180 mr-2">
                    <svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m5 15 7-7 7 7"/>
                    </svg>
                </div>

                <div class="font-bold text-xl mr-4">Conteúdo</div>
            </div>

            <div class="flex-col hidden cont-content md:flex-row xl:flex-row">
                <div class="flex-col mr-10">
                    <div class="font-medium text-xl mb-4 mt-4">Simplificações</div>
    
                    <ul class="list ml-6">
                        <li>O movimento é bidimensional</li>
                        <li>A massa é constante</li>
                    </ul>
                </div>

                <div class="flex-col">
                    <div class="font-medium text-xl mb-4 mt-4">Equações</div>
    
                    <ul class="list ml-6">
                        <li>Terceira Lei de Newton</li>
                        <li>Torricelli</li>
                    </ul>
                </div>
            </div>


            <div class="flex flex-row items-center  mb-8 mt-8">
                <div @click="contentHS('axis')" class="w-6 h-6 black cursor-pointer axis rotate-180 mr-2">
                    <svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m5 15 7-7 7 7"/>
                    </svg>
                </div>

                <div class="font-bold text-xl mr-4">Range para eixo X</div>
            </div>

            <div class="hidden axis-content justify-center align-middle items-center">

                <div class="flex-col md:flex-row xl:flex-row">
                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="flex mr-4 items-center w-20 md:w-40 xl:w-40">Mínimo: </div>
                        <input class="flex input rounded-md p-1 border-2 border-black w-30" id="graph_min" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="flex mr-4 items-center w-20 md:w-40 xl:w-40">Máximo: </div>
                        <input class="flex input rounded-md p-1 w-30 border-2 border-black" id="graph_max" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="flex mr-4 items-center w-20 md:w-40 xl:w-40">Step: </div>
                        <input class="flex input rounded-md p-1 w-30 border-2 border-black" id="graph_stepsize" type="text">
                    </div>
                </div>

                <button @click="graphRangeX" class="border-2 border-black rounded-lg p-1 font-bold h-fit w-60 mt-4 mb-6">Modificar</button>

            </div>

            <div class="flex flex-row items-center  mb-8 ">
                <div @click="contentHS('axisY')" class="w-6 h-6 black cursor-pointer axisY rotate-180 mr-2">
                    <svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m5 15 7-7 7 7"/>
                    </svg>
                </div>

                <div class="font-bold text-xl mr-4">Range para eixo Y</div>
            </div>

            <div class="hidden axisY-content justify-center align-middle items-center">

                <div class="flex-col md:flex-row xl:flex-row">
                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="flex mr-4 items-center w-20 md:w-40 xl:w-40">Mínimo: </div>
                        <input class="flex input rounded-md p-1 border-2 border-black w-30" id="graph_min_y" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="flex mr-4 items-center w-20 md:w-40 xl:w-40">Máximo: </div>
                        <input class="flex input rounded-md p-1 w-30 border-2 border-black" id="graph_max_y" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="flex mr-4 items-center w-20 md:w-40 xl:w-40">Step: </div>
                        <input class="flex input rounded-md p-1 w-30 border-2 border-black" id="graph_stepsize_y" type="text">
                    </div>
                </div>

                <button @click="graphRangeY" class="border-2 border-black rounded-lg p-1 font-bold h-fit w-60 mt-4 mb-6">Modificar</button>

            </div>
            
            <div class="flex flex-row items-center mb-8">
                <div @click="contentHS('cvel')" class="w-6 h-6 black cursor-pointer cvel rotate-180 mr-2">
                    <svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m5 15 7-7 7 7"/>
                    </svg>
                </div>

                <div class="font-bold text-xl mr-4">Curvas de Velocidade</div>
            </div>

            <div class="hidden cvel-content justify-center align-middle items-center">

                <div class="flex-col md:flex-row xl:flex-row">
                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Curva: </div>
                        <input class="input rounded-md p-1 mr-4" id="cv_curva_cor" type="color">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Ponto: </div>
                        <input class="input rounded-md p-1" id="cv_point_cor" type="color">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Label: </div>
                        <input class="input rounded-md p-1 border-2 border-black w-1/2" id="cv_label" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Altura inicial: </div>
                        <input class="input rounded-md p-1 w-1/2 border-2 border-black" id="cv_altura_inicial" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Velocidade inicial: </div>
                        <input class="input rounded-md p-1 w-1/2 border-2 border-black" id="cv_velocidade_inicial" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Massa: </div>
                        <input class="input rounded-md p-1 w-1/2 border-2 border-black" id="cv_massa" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Gravidade: </div>
                        <input class="input rounded-md p-1 w-1/2 border-2 border-black" id="cv_gravidade" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Intensidade: </div>
                        <input class="input rounded-md p-1 w-1/2 border-2 border-black" id="cv_intensidade" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Ângulo: </div>
                        <input class="input rounded-md p-1 w-1/2 border-2 border-black" id="cv_angulo" type="text">
                    </div>
                </div>

                <button @click="curvaVelocidade" class="border-2 border-black rounded-lg p-1 font-bold h-fit w-60 mt-4 mb-6">Calcular</button>

            </div>


            <div class="flex flex-row items-center mb-8">
                <div @click="contentHS('cpouso')" class="w-6 h-6 black cursor-pointer cpouso rotate-180 mr-2">
                    <svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m5 15 7-7 7 7"/>
                    </svg>
                </div>

                <div class="font-bold text-xl mr-4">Curvas de Pouso Suave</div>
            </div>

            <div class="hidden cpouso-content justify-center align-middle items-center">

                <div class="flex-col md:flex-row xl:flex-row">
                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Curva: </div>
                        <input class="input rounded-md p-1 mr-4" id="ps_curva_cor" type="color">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Label: </div>
                        <input class="input rounded-md p-1 border-2 border-black w-1/2" id="ps_label" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Massa: </div>
                        <input class="input rounded-md p-1 w-1/2 border-2 border-black" id="ps_massa" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Gravidade: </div>
                        <input class="input rounded-md p-1 w-1/2 border-2 border-black" id="ps_gravidade" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Intensidade: </div>
                        <input class="input rounded-md p-1 w-1/2 border-2 border-black" id="ps_intensidade" type="text">
                    </div>

                    <div class="flex flex-row mb-4 md:mr-4 xl:mr-4">
                        <div class="first-line:flex mr-4 items-center w-20 md:w-40 xl:w-40">Ângulo: </div>
                        <input class="input rounded-md p-1 w-1/2 border-2 border-black" id="ps_angulo" type="text">
                    </div>
                </div>

                <button @click="curvaPousoSuave" class="border-2 border-black rounded-lg p-1 font-bold h-fit w-60 mt-4 mb-6">Calcular</button>
            </div>

            <div class="w-full flex justify-end">
                <button @click="resetGraph" class="border-2 border-black rounded-lg p-1 font-bold h-fit w-40 mt-4 mb-6">Reset</button>
            </div>

            <LineChart :chart-data="data" :options="options" class="flex justify-center items-center w-full mt-2 mb-2 md:h-80 xl:h-80" ref="pageChart"></LineChart>

        </template>

        <template v-slot:footer>
            <div></div>
        </template>
    </Modal>

    <!-- Fim da página do pouso lunar -->

    <!-- Inicio da página do twolines -->
    <Modal v-show="modalCelestrak">
        <template v-slot:header>
            <svg @click="modalCelestrak = false" class="cursor-pointer w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                <path stroke="#222222" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m13 7-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
            </svg>

            
        </template>

        <template v-slot:body>
            <div class="font-bold text-3xl mb-8">Two Lines</div>

            <div class="flex flex-row items-center mt-8 mb-8">
                <div @click="contentHS('cont-cel')" class="w-6 h-6 black cursor-pointer cont-cel rotate-180 mr-2">
                    <svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m5 15 7-7 7 7"/>
                    </svg>
                </div>

                <div class="font-bold text-xl mr-4">Conteúdo</div>
            </div>

            <div class="flex-col hidden cont-cel-content mb-8">
                <a><img src="https://i.imgur.com/0p4MmcU.png" title="tle" /></a>

                <div class="">Powered by
                    <img class="h-12" src="https://i.pinimg.com/736x/bb/7c/4c/bb7c4cfe7485487929ff3af7e6cbe6f8.jpg" title="celestrak" />
                </div>
            </div>

            <select  @input="selectGroupCelestrak($event.target.value)" class="p-3 rounded-md w-full mb-8" name="celestrak-group">
                <option selected disabled hidden>Selecione um grupo</option>
                <option v-for="item in celestrakGroups" :value="item.code">{{ item.name }}</option>
            </select>

            <div v-if="selectedGroup != null">
                <select  @input="selectObjectCelestrak($event.target.value)" class="p-3 rounded-md w-full" name="celestrak-object">
                    <option selected disabled hidden>Selecione um veículo espacial</option>
                    <option v-for="item in celestrakObjects" :value="item.OBJECT_NAME">{{ item.OBJECT_NAME }}</option>
                </select>
            </div>
            <div v-else>
                <select class="p-3 rounded-md w-full" disabled>
                    <option selected disabled hidden>Selecione um veiculo espacial</option>
                </select>
            </div>

            <div v-if="selectedObject != null">
                <div class="flex mr-4 w-ful">Argumento do Perigeu: </div>
                <input :value="selectedObject.ARG_OF_PERICENTER" class="p-3 rounded-md w-full mb-8" type="text" disabled>

                <div class="flex mr-4 w-ful">BStar: </div>
                <input :value="selectedObject.BSTAR" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Classificação: </div>
                <input :value="selectedObject.CLASSIFICATION_TYPE" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Excentricidade: </div>
                <input :value="selectedObject.ECCENTRICITY" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Element Set No: </div>
                <input :value="selectedObject.ELEMENT_SET_NO" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Tipo de ephemeris: </div>
                <input :value="selectedObject.EPHEMERIS_TYPE" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Epoch: </div>
                <input :value="selectedObject.EPOCH" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Inclinação: </div>
                <input :value="selectedObject.INCLINATION" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Anomalia Média: </div>
                <input :value="selectedObject.MEAN_ANOMALY" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">MOvimento Médio: </div>
                <input :value="selectedObject.MEAN_MOTION" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Movimento Médio DDot: </div>
                <input :value="selectedObject.MEAN_MOTION_DDOT" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Movimento Médio Dot: </div>
                <input :value="selectedObject.MEAN_MOTION_DOT" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">NORAD CAT ID: </div>
                <input :value="selectedObject.NORAD_CAT_ID" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Object ID: </div>
                <input :value="selectedObject.OBJECT_ID" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Object Name: </div>
                <input :value="selectedObject.OBJECT_NAME" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">RA do Nodo ascendente: </div>
                <input :value="selectedObject.RA_OF_ASC_NODE" class="p-3 rounded-md w-full mb-8" type="text" disabled>
                <div class="flex mr-4 w-ful">Rev at Epoch: </div>
                <input :value="selectedObject.REV_AT_EPOCH" class="p-3 rounded-md w-full mb-8" type="text" disabled>
            </div>
        </template>

        <template v-slot:footer>
            <div></div>
        </template>
    </Modal>

    <!-- <UserModal v-show="userModal">
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
    </UserModal> -->

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
import LineChart from './LineChart.vue'
import _ from 'lodash'

export default {
    name: "Home",
    components: {
        UserModal,
        Modal,
        LineChart,

    },
    data() {
        return {
            userModal: false,
            modalSolarSystema: false,
            modalPosicionamento: false,
            modalManobras: false,
            modalLagrange: false,
            modalPousoLunar: false,
            modalCelestrak: false,
            prefix:{
                home: 'selected',
                explore: '',
            },
            celestrakGroups:[
                {'code': 'last-30-days', 'name': 'Last 30 days'},
                {'code': 'stations', 'name': 'Space Stations'},
                {'code': 'visual', 'name': '100 (or so) Brightest'},
                {'code': 'iridium-33-debris', 'name': 'Iridium 33 Debris'},
                {'code': 'weather', 'name': 'Weather Satellites'},
                {'code': 'starlink', 'name': 'Starlink Satellites'},
                {'code': 'intelsat', 'name': 'Intelsat Satellites'},
                {'code': 'iridium', 'name': 'Iridium Satellites'},
                {'code': 'orbcomm', 'name': 'Orbcomm Satellites'},
                {'code': 'cubesat', 'name': 'Cubesats'},
                {'code': 'radar', 'name': 'Radar Calibration'},
                {'code': 'planet', 'name': 'Planet Labs'}
            ],
            celestrakObjects: [],
            selectedGroup: null,
            selectedObject: null,
            home: true,
            explore: false,
            signin: true,
            register: false,
            loggedin: false,
            data: {
                datasets: [

                ],
            },
            options: {
                tension: 0.4,
                scales: {
                    x: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Velocidade Vertical'
                        },
                        type: 'linear',
                        min: -20,
                        max:10, // Define o range do eixo x
                        ticks: {
                            stepSize: 2 // Define o intervalo entre os ticks
                        }
                    },
                    y: {
                        beginAtZero: true,
                        display: true,
                        title: {
                            display: true,
                            text: 'Altitude'
                        },
                        type: 'linear',
                        min: -20,
                        max:10, // Define o range do eixo x
                        ticks: {
                            stepSize: 2 // Define o intervalo entre os ticks
                        }
                    }
                },
                elements: {
                    point: {
                        radius: 0, // Define o raio do ponto como 0 para não exibir pontos
                    },
                },
                plugins: {
                    legend: {
                        display: true,
                    },
                    
    
                },
            }
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
        async selectGroupCelestrak(code){
            this.selectedGroup = code
            this.celestrakObjects = null
            console.log(code)

            const rawResponse = await fetch(`https://celestrak.org/NORAD/elements/gp.php?GROUP=${code}&FORMAT=json-pretty`, {
            })

            const content = await rawResponse.json()
            this.celestrakObjects = content
        },
        selectObjectCelestrak(code){
            this.selectedObject = _.find(this.celestrakObjects, {OBJECT_NAME: code})
        },
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
        contentHS(baseClass){
            let className = document.getElementsByClassName(baseClass)[0].className
            let classContent = document.getElementsByClassName(baseClass + '-content')[0].className

            if(className.includes('180')){
                className = className.replace('rotate-180', 'rotate-0')
                document.getElementsByClassName(baseClass)[0].className = className
                classContent = classContent.replace('hidden', 'flex flex-col')
                document.getElementsByClassName(baseClass + '-content')[0].className = classContent
            } else {
                className = className.replace('rotate-0', 'rotate-180')
                document.getElementsByClassName(baseClass)[0].className = className
                classContent = classContent.replace('flex flex-col', 'hidden')
                document.getElementsByClassName(baseClass + '-content')[0].className = classContent
            }
        },
        graphRangeX(){
            const min = parseFloat(document.getElementById('graph_min').value);
            const max = parseFloat(document.getElementById('graph_max').value);
            const stepsize = parseFloat(document.getElementById('graph_stepsize').value);

            this.options.scales.x.min = min;
            this.options.scales.x.max = max;
            this.options.scales.x.ticks.stepSize = stepsize;
            this.options.scales.x.type = 'linear';

            const pageChart = this.$refs.pageChart;
            pageChart.update();
        },
        graphRangeY(){
            const min = parseFloat(document.getElementById('graph_min_y').value);
            const max = parseFloat(document.getElementById('graph_max_y').value);
            const stepsize = parseFloat(document.getElementById('graph_stepsize_y').value);

            this.options.scales.y.min = min;
            this.options.scales.y.max = max;
            this.options.scales.y.ticks.stepSize = stepsize;
            this.options.scales.y.type = 'linear';

            const pageChart = this.$refs.pageChart;
            pageChart.update();
        },
        async curvaVelocidade(){
            const y = parseInt(document.getElementById('cv_altura_inicial').value)
            const x = parseInt(document.getElementById('cv_velocidade_inicial').value)
            const corCurva = document.getElementById('cv_curva_cor').value
            const corPonto = document.getElementById('cv_point_cor').value
            const nome = document.getElementById('cv_label').value
            const massa = parseFloat(document.getElementById('cv_massa').value)
            const gravidade = parseFloat(document.getElementById('cv_gravidade').value)
            const intensidade = parseFloat(document.getElementById('cv_intensidade').value)
            const angulacao = parseFloat(document.getElementById('cv_angulo').value)


            const rawResponse = await fetch('/pouso/curva/velocidade', {
                method: 'POST',
                headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': document.cookie.replace(/(?:(?:^|.*;\s*)csrf_token\s*=\s*([^;]*).*$)|^.*$/, '$1')
                },
                body: JSON.stringify({
                    massa: massa,
                    gravidade: gravidade,
                    intensidade: intensidade,
                    angulacao: angulacao,
                    altura: y,
                    velocidade_inicial: x,
                })
            })

            const content = await rawResponse.json()
            this.addCurvaVelocidade(content.velocidade, content.altura, corCurva, nome, corPonto, x, y)

        },
        resetGraph(){
            this.data.datasets = []
            const pageChart = this.$refs.pageChart
            pageChart.update()
        },
        async curvaPousoSuave(){
            const corCurva = document.getElementById('ps_curva_cor').value
            const nome = document.getElementById('ps_label').value
            const massa = parseFloat(document.getElementById('ps_massa').value)
            const gravidade = parseFloat(document.getElementById('ps_gravidade').value)
            const intensidade = parseFloat(document.getElementById('ps_intensidade').value)
            const angulacao = parseFloat(document.getElementById('ps_angulo').value)


            const rawResponse = await fetch('/pouso/curva/pouso/suave', {
                method: 'POST',
                headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': document.cookie.replace(/(?:(?:^|.*;\s*)csrf_token\s*=\s*([^;]*).*$)|^.*$/, '$1')
                },
                body: JSON.stringify({
                    massa: massa,
                    gravidade: gravidade,
                    intensidade: intensidade,
                    angulacao: angulacao,
                })
            })

            const content = await rawResponse.json()
            this.addCurvaVelocidade(content.velocidade, content.altura, corCurva, nome, null, null, null)

        },
        addCurvaVelocidade(velocidade, altura, corCurva, nome, corPonto, x, y){

            let dados = []

            // Monta os objetos {x, y} para cada par de valores
            for (let i = 0; i < velocidade.length; i++) {
                dados.push({ x: velocidade[i], y: altura[i] });
            }

            const newDataset = {
                label: nome,
                data: dados,
                borderColor: corCurva,
                backgroundColor: 'transparent',
                borderWidth: 1
            }

            this.data.datasets.push(newDataset)

            // Criar um novo conjunto de dados com o ponto adicionado
            if (corPonto && x && y) {
                const newPoint = {
                    label: 'Ponto: ' + nome,
                    data: [{x: x, y: y}],
                    showLine: false,
                    pointRadius: 5,
                    pointBackgroundColor: corPonto,
                    borderColor: corPonto,
                    backgroundColor: corPonto,
                };

                this.data.datasets.push(newPoint)
            }

            const pageChart = this.$refs.pageChart
            pageChart.update()

        },
        addPointToDataset() {
           
            const y = parseFloat(document.getElementById('cv_altura_inicial').value)
            const x = parseFloat(document.getElementById('cv_velocidade_inicial').value)
            const cor = document.getElementById('cv_point_cor').value
            const nome = document.getElementById('cv_label').value

            // Encontrar o índice correspondente ao valor x no array de labels
            const index = this.data.labels.reduce((prevIndex, label, i) => {
                const labelValue = parseFloat(label);
                const prevLabelValue = parseFloat(this.data.labels[prevIndex]);
                const xValue = parseFloat(x.toFixed(1));

                const diff = Math.abs(labelValue - xValue);
                const prevDiff = Math.abs(prevLabelValue - xValue);

                return diff < prevDiff ? i : prevIndex;
            }, 0);

            // Criar um novo conjunto de dados com o ponto adicionado
            const newDataset = {
                label: nome,
                data: this.data.labels.map((label, i) => (i === index ? y : null)),
                showLine: false,
                pointRadius: 5,
                pointBackgroundColor: cor,
                borderColor: cor,
                backgroundColor: cor,
            };

            // Adicionar o novo conjunto de dados ao array de datasets
            this.data.datasets.push(newDataset);
            // Atualizar o gráfico
            const pageChart = this.$refs.pageChart
            pageChart.update()

        },
        async curvasPousoSuave(){
            const rawResponse = await fetch('/pouso/lunar/suave', {
                method: 'POST',
                headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': document.cookie.replace(/(?:(?:^|.*;\s*)csrf_token\s*=\s*([^;]*).*$)|^.*$/, '$1')
                },
                body: JSON.stringify({
                    massa: 1.1,
                    gravidade: 1.8,
                    intensidade: 3.6,
                    angulacao: 0,
                    altura: 18,
                    velocidade_inicial: -7,
                })
            })

            const content = await rawResponse.json()
            return content



            // {
            //             label: ,
            //             data: [65, 59, 80, 81, 56, 55, 100],
            //             fill: false,
            //             borderColor: 'rgb(75, 192, 192)',
            //             tension: 0.4,
            //         },
        },
        linspace(start, end, n) {
            const step = (end - start) / (n - 1);
            const result = [];
            for (let i = 0; i < n; i++) {
                result.push((start + i * step).toFixed(1));
            }
            return result;
        }
    }
}
</script>