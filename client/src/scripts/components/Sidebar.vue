<template>
    <div class="menu">
        <aside class="side-box">
            <div class="side-bar">
                <nav class="nav" id="menuLateral">
                <ul>
                    <li class="item">
                        <div @click="redirect('./inicio')" class="menu-item" id="inicio-menu">
                            <div class="itens">
                                <svg class="menu-icon" width="20" height="21" viewBox="0 0 20 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M17 1.5H3C1.89543 1.5 1 2.39543 1 3.5V17.5C1 18.6046 1.89543 19.5 3 19.5H17C18.1046 19.5 19 18.6046 19 17.5V3.5C19 2.39543 18.1046 1.5 17 1.5Z" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M8 5.5H5V14.5H8V5.5Z" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M15 5.5H12V10.5H15V5.5Z" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <!-- Inserir elemento de menu ativo -->
                                <a class="menu-text">Início</a>
                            </div>

                        </div>
                    </li>

                    <li class="item">
                        <div @click="redirect('./imoveis')" class="menu-item" id="imoveis-menu">
                            <div class="itens">
                                <svg class="menu-icon" width="20" height="23" viewBox="0 0 20 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M1 8.5L10 1.5L19 8.5V19.5C19 20.0304 18.7893 20.5391 18.4142 20.9142C18.0391 21.2893 17.5304 21.5 17 21.5H3C2.46957 21.5 1.96086 21.2893 1.58579 20.9142C1.21071 20.5391 1 20.0304 1 19.5V8.5Z" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M7 21.5V11.5H13V21.5" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <svg class="menu-icon-active" style="display: none" xmlns="http://www.w3.org/2000/svg" width="18" height="21" viewBox="0 0 18 21" fill="none">
                                    <path d="M0 7L9 0L18 7V18C18 18.5304 17.7893 19.0391 17.4142 19.4142C17.0391 19.7893 16.5304 20 16 20H2C1.46957 20 0.960859 19.7893 0.585786 19.4142C0.210714 19.0391 0 18.5304 0 18V7Z" fill="#EC0000"/>
                                    <path d="M6 20V10H12V20" fill="#EC0000"/>
                                    <path d="M6 20V10H12V20" stroke="#FEF3F3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <a class="menu-text">Imóveis</a>
                            </div>

                        </div>
                    </li>

                    <li class="collapse__content">
                        <div @click="showSubMenu('balcao-menu')" class="menu-item" id="balcao-menu">
                            <div class="itens">
                                <svg class="menu-icon" width="24" height="19" viewBox="0 0 24 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M6.04346 2.5C5.92206 2.5 5.80386 2.53937 5.70673 2.61224L2.2261 5.21375C2.08408 5.3208 2.00037 5.48819 2 5.66608V9.14667C2.00043 9.35867 2.11963 9.55255 2.30859 9.64865C2.49756 9.74475 2.72446 9.72693 2.89606 9.60236L5.33093 7.82208L5.33096 15.8835C5.33188 16.1945 5.58435 16.4463 5.89545 16.4462L9.73315 16.4463C10.0443 16.4463 10.2968 16.1945 10.2977 15.8834V3.06454C10.2977 2.75275 10.0449 2.5 9.73315 2.5H6.04681C6.04568 2.5 6.04459 2.5 6.04346 2.5ZM6.04349 0.5H9.73315C11.1472 0.5 12.2977 1.65045 12.2977 3.06454V15.8893C12.2935 17.2992 11.1431 18.4463 9.73315 18.4463L5.89542 18.4462C5.89532 18.4462 5.89548 18.4462 5.89542 18.4462C4.48578 18.4462 3.33508 17.2994 3.33096 15.8893V11.5936C3.08521 11.6705 2.82761 11.71 2.56442 11.71C2.16235 11.71 1.76041 11.6136 1.40201 11.4314C0.539124 10.9926 0.00192261 10.1187 0 9.15063V5.66608C0.00161743 4.86252 0.383789 4.09787 1.02231 3.61661L1.02875 3.61176L4.50937 1.01025C4.94699 0.681946 5.49283 0.5 6.04349 0.5Z" fill="#222222"/>
                                    <path d="M16.8593 2.5C16.7375 2.5 16.619 2.53937 16.5215 2.61224L13.0425 5.21375C12.9001 5.32043 12.8163 5.48807 12.8164 5.66608V9.14667C12.8168 9.35867 12.936 9.55255 13.125 9.64865C13.314 9.74472 13.5409 9.72681 13.7125 9.60236L16.1457 7.82208V15.8835C16.1465 16.1945 16.399 16.4463 16.7102 16.4462H20.5479C20.8588 16.4462 21.1107 16.1943 21.1107 15.8834V3.06454C21.1107 2.75342 20.8589 2.50095 20.5479 2.5H16.8615C16.8608 2.5 16.86 2.5 16.8593 2.5ZM16.8593 0.5H20.554C21.9637 0.504303 23.1107 1.65475 23.1107 3.06454V15.8834C23.1107 17.2965 21.9611 18.4462 20.5479 18.4462H16.7102C16.7101 18.4462 16.7103 18.4462 16.7102 18.4462C15.3003 18.4462 14.1495 17.2992 14.1457 15.8889V11.5941C13.9005 11.6707 13.6434 11.71 13.3809 11.71C12.9788 11.71 12.5769 11.6136 12.2185 11.4314C11.3555 10.9926 10.8184 10.1187 10.8164 9.15063V5.66608C10.8158 4.86334 11.1997 4.09534 11.8433 3.61313L15.3237 1.01053C15.7646 0.681152 16.3097 0.5 16.8593 0.5Z" fill="#222222"/>
                                </svg>
                                <!-- Inserir elemento de menu ativo -->
                                <a class="menu-text">Balcão Apê11</a>
                            </div>

                            <div class="arrow" id="arrow">
                                <svg width="12" height="8" viewBox="0 0 12 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M1.01873 1.95009L5.96899 6.99934L11.0182 2.04907L10.0282 1.03922L5.98879 4.99943L2.02858 0.960037L1.01873 1.95009Z" fill="#222222"/>
                                </svg>
                            </div>
                        </div>

                        <ul class="collapse-menu">
                            <li class="collapse-sublink">
                                <a class="submenu-item" @click="redirect('./sub-menu-1')">SubMenu 1</a>
                            </li>
                        </ul>

                    </li>

                    <li class="item">
                        <div @click="redirect('./clientes')" class="menu-item" id="clientes-menu">
                            <div class="itens">
                                <svg class="menu-icon" width="24" height="21" viewBox="0 0 24 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M17 19.5V17.5C17 16.4391 16.5786 15.4217 15.8284 14.6716C15.0783 13.9214 14.0609 13.5 13 13.5H5C3.93913 13.5 2.92172 13.9214 2.17157 14.6716C1.42143 15.4217 1 16.4391 1 17.5V19.5" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M9 9.5C11.2091 9.5 13 7.70914 13 5.5C13 3.29086 11.2091 1.5 9 1.5C6.79086 1.5 5 3.29086 5 5.5C5 7.70914 6.79086 9.5 9 9.5Z" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M23 19.5V17.5C22.9993 16.6137 22.7044 15.7528 22.1614 15.0523C21.6184 14.3519 20.8581 13.8516 20 13.63" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M16 1.63C16.8604 1.85031 17.623 2.35071 18.1676 3.05232C18.7122 3.75392 19.0078 4.61683 19.0078 5.505C19.0078 6.39318 18.7122 7.25608 18.1676 7.95769C17.623 8.6593 16.8604 9.1597 16 9.38" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <svg class="menu-icon-active" style="display: none;" xmlns="http://www.w3.org/2000/svg" width="24" height="21" viewBox="0 0 24 21" fill="none">
                                    <path d="M17 20.5V18.167C17 15.589 15.209 13.5 13 13.5H5C2.791 13.5 1 15.589 1 18.167V20.5" fill="#EC0000"/>
                                    <path d="M17 20.5C16.7348 20.5 16.4804 20.3946 16.2929 20.2071C16.1054 20.0196 16 19.7652 16 19.5V17.5C16 16.7044 15.6839 15.9413 15.1213 15.3787C14.5587 14.8161 13.7956 14.5 13 14.5H5C4.20435 14.5 3.44129 14.8161 2.87868 15.3787C2.31607 15.9413 2 16.7044 2 17.5V19.5C2 19.7652 1.89464 20.0196 1.70711 20.2071C1.51957 20.3946 1.26522 20.5 1 20.5C0.734784 20.5 0.48043 20.3946 0.292893 20.2071C0.105357 20.0196 0 19.7652 0 19.5V17.5C0.00158786 16.1744 0.528882 14.9036 1.46622 13.9662C2.40356 13.0289 3.67441 12.5016 5 12.5H13C14.3256 12.5016 15.5964 13.0289 16.5338 13.9662C17.4711 14.9036 17.9984 16.1744 18 17.5V19.5C18 19.7652 17.8946 20.0196 17.7071 20.2071C17.5196 20.3946 17.2652 20.5 17 20.5Z" fill="#EC0000"/>
                                    <path d="M9 9.5C11.2091 9.5 13 7.70914 13 5.5C13 3.29086 11.2091 1.5 9 1.5C6.79086 1.5 5 3.29086 5 5.5C5 7.70914 6.79086 9.5 9 9.5Z" fill="#EC0000" stroke="#EC0000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M23 19.5V17.5C22.9993 16.6137 22.7044 15.7528 22.1614 15.0523C21.6184 14.3519 20.8581 13.8516 20 13.63" stroke="#EC0000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M16 1.63C16.8604 1.85031 17.623 2.35071 18.1676 3.05232C18.7122 3.75392 19.0078 4.61683 19.0078 5.505C19.0078 6.39318 18.7122 7.25608 18.1676 7.95769C17.623 8.6593 16.8604 9.1597 16 9.38" stroke="#EC0000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <a class="menu-text">Clientes</a>
                            </div>

                        </div>
                    </li>

                    <li class="item">
                        <div @click="redirect('./funil')" class="menu-item" id="funil-menu">
                            <div class="itens">
                                <svg class="menu-icon" xmlns="http://www.w3.org/2000/svg" width="22" height="21" viewBox="0 0 22 21" fill="none">
                                    <path d="M21 1.05396H1L9 10.514V17.054L13 19.054V10.514L21 1.05396Z" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <svg class="menu-icon-active" style="display: none" xmlns="http://www.w3.org/2000/svg" width="20" height="19" viewBox="0 0 20 19" fill="none">
                                    <path d="M12 18.5L8.00586 16.5V11H12.0059V18.5H12ZM12.8105 9H7.19336L0 0.5H20L12.8066 9H12.8105Z" fill="#EC0000"/>
                                </svg>
                                <a class="menu-text">Funil</a>
                            </div>

                        </div>
                    </li>

                    <li class="item">
                        <div @click="redirect('./agenda')" class="menu-item" id="agenda-menu">
                            <div class="itens">
                                <svg class="menu-icon" width="20" height="23" viewBox="0 0 20 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M17 3.5H3C1.89543 3.5 1 4.39543 1 5.5V19.5C1 20.6046 1.89543 21.5 3 21.5H17C18.1046 21.5 19 20.6046 19 19.5V5.5C19 4.39543 18.1046 3.5 17 3.5Z" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M14 1.5V5.5" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M6 1.5V5.5" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M1 9.5H19" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <svg class="menu-icon-active" style="display: none;" xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22" fill="none">
                                    <path d="M18 3.5H4C2.89543 3.5 2 4.39543 2 5.5V19.5C2 20.6046 2.89543 21.5 4 21.5H18C19.1046 21.5 20 20.6046 20 19.5V5.5C20 4.39543 19.1046 3.5 18 3.5Z" fill="#EC0000"/>
                                    <path d="M15 1.5V5.5" stroke="#EC0000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M7 1.5V5.5" stroke="#EC0000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M1 9.5H21" stroke="#FEF3F3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <a class="menu-text">Agenda</a>
                            </div>

                        </div>
                    </li>

                    <li class="item">
                        <div @click="redirect('./credito-imobiliario')" class="menu-item" id="credito-imob-menu">
                            <div class="itens">
                                <svg class="menu-icon" width="22" height="23" viewBox="0 0 22 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M11 21.5C16.5228 21.5 21 17.0228 21 11.5C21 5.97715 16.5228 1.5 11 1.5C5.47715 1.5 1 5.97715 1 11.5C1 17.0228 5.47715 21.5 11 21.5Z" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M10.8672 5.46106V17.5401" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M14.1603 7.47302H8.96531C8.44615 7.47302 7.94825 7.67926 7.58115 8.04636C7.21405 8.41346 7.00781 8.91136 7.00781 9.43052C7.00781 9.94968 7.21405 10.4476 7.58115 10.8147C7.94825 11.1818 8.44615 11.388 8.96531 11.388H12.7653C13.2845 11.388 13.7824 11.5943 14.1495 11.9614C14.5166 12.3285 14.7228 12.8264 14.7228 13.3455C14.7228 13.8647 14.5166 14.3626 14.1495 14.7297C13.7824 15.0968 13.2845 15.303 12.7653 15.303H7.00831" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <!-- Inserir elemento de menu ativo -->
                                <a class="menu-text">Crédito Imobiliário</a>
                            </div>
                        </div>
                    </li>

                    <li class="collapse__content">
                        <div @click="showSubMenu('relatorios-menu')" class="menu-item" id="relatorios-menu">

                            <div class="itens">
                                <svg class="menu-icon" width="18" height="22" viewBox="0 0 18 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M11 1H3C2.46957 1 1.96086 1.21071 1.58579 1.58579C1.21071 1.96086 1 2.46957 1 3V19C1 19.5304 1.21071 20.0391 1.58579 20.4142C1.96086 20.7893 2.46957 21 3 21H15C15.5304 21 16.0391 20.7893 16.4142 20.4142C16.7893 20.0391 17 19.5304 17 19V7L11 1Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M11 1V7H17" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M13 12H5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M13 16H5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M7 8H5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <!-- Inserir elemento do menu ativo -->
                                <a class="menu-text">Relatórios</a>
                            </div>

                            <div class="arrow" id="arrow">
                                <svg width="12" height="8" viewBox="0 0 12 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M1.01873 1.95009L5.96899 6.99934L11.0182 2.04907L10.0282 1.03922L5.98879 4.99943L2.02858 0.960037L1.01873 1.95009Z" fill="#222222"/>
                                </svg>
                            </div>
                        </div>

                        <ul class="collapse-menu">
                            <li class="collapse-sublink">
                                <a class="submenu-item" @click="redirect('./sub-menu-1')">SubMenu 1</a>
                            </li>
                        </ul>

                    </li>

                    <li class="collapse__content">
                        <div @click="showSubMenu('integracoes-menu')" class="menu-item" id="integracoes-menu">

                            <div class="itens">
                                <svg class="menu-icon" width="20" height="22" viewBox="0 0 20 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M16 7C17.6569 7 19 5.65685 19 4C19 2.34315 17.6569 1 16 1C14.3431 1 13 2.34315 13 4C13 5.65685 14.3431 7 16 7Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M4 14C5.65685 14 7 12.6569 7 11C7 9.34315 5.65685 8 4 8C2.34315 8 1 9.34315 1 11C1 12.6569 2.34315 14 4 14Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M16 21C17.6569 21 19 19.6569 19 18C19 16.3431 17.6569 15 16 15C14.3431 15 13 16.3431 13 18C13 19.6569 14.3431 21 16 21Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M6.58984 12.51L13.4198 16.49" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M13.4098 5.51001L6.58984 9.49001" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <!-- Inserir elemento de menu ativo -->
                                <a class="menu-text">Integrações</a>
                            </div>

                            <div class="arrow" id="arrow">
                                <svg width="12" height="8" viewBox="0 0 12 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M1.01873 1.95009L5.96899 6.99934L11.0182 2.04907L10.0282 1.03922L5.98879 4.99943L2.02858 0.960037L1.01873 1.95009Z" fill="#222222"/>
                                </svg>
                            </div>
                        </div>

                        <ul class="collapse-menu">
                            <li class="collapse-sublink">
                                <a class="submenu-item" @click="redirect('./sub-menu-1')">SubMenu 1</a>
                            </li>
                        </ul>

                    </li>

                    <li class="collapse__content">
                        <div @click="showSubMenu('configuracoes-menu')" class="menu-item" id="configuracoes-menu">
                            <div class="itens">
                                <svg class="menu-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <path d="M19.4 15C19.2669 15.3016 19.2272 15.6362 19.286 15.9606C19.3448 16.285 19.4995 16.5843 19.73 16.82L19.79 16.88C19.9758 17.0658 20.1232 17.2864 20.2238 17.5292C20.3244 17.772 20.3761 18.0322 20.3761 18.295C20.3761 18.5578 20.3244 18.818 20.2238 19.0608C20.1232 19.3036 19.9758 19.5242 19.79 19.71C19.6042 19.8958 19.3836 20.0432 19.1408 20.1438C18.898 20.2444 18.6378 20.2961 18.375 20.2961C18.1122 20.2961 17.852 20.2444 17.6092 20.1438C17.3664 20.0432 17.1458 19.8958 16.96 19.71L16.9 19.65C16.6663 19.4236 16.3712 19.2707 16.0514 19.2103C15.7317 19.15 15.4012 19.1848 15.101 19.3104C14.8008 19.436 14.5441 19.6469 14.3626 19.917C14.1811 20.1872 14.0828 20.5046 14.08 20.83V21C14.08 21.5304 13.8693 22.0391 13.4942 22.4142C13.1191 22.7893 12.6104 23 12.08 23C11.5496 23 11.0409 22.7893 10.6658 22.4142C10.2907 22.0391 10.08 21.5304 10.08 21V20.91C10.0723 20.579 9.96512 20.258 9.77251 19.9887C9.5799 19.7194 9.31074 19.5143 9 19.4C8.69838 19.2669 8.36381 19.2272 8.03941 19.286C7.71502 19.3448 7.41568 19.4995 7.18 19.73L7.12 19.79C6.74472 20.1653 6.23573 20.3761 5.705 20.3761C5.17427 20.3761 4.66528 20.1653 4.29 19.79C3.91472 19.4147 3.70389 18.9057 3.70389 18.375C3.70389 17.8443 3.91472 17.3353 4.29 16.96L4.35 16.9C4.57642 16.6663 4.72929 16.3712 4.78966 16.0514C4.85003 15.7317 4.81525 15.4012 4.68963 15.101C4.56402 14.8008 4.35308 14.5441 4.08296 14.3626C3.81284 14.1811 3.49541 14.0828 3.17 14.08H3C2.46957 14.08 1.96086 13.8693 1.58579 13.4942C1.21071 13.1191 1 12.6104 1 12.08C1 11.5496 1.21071 11.0409 1.58579 10.6658C1.96086 10.2907 2.46957 10.08 3 10.08H3.09C3.42099 10.0723 3.742 9.96512 4.0113 9.77251C4.28059 9.5799 4.48572 9.31074 4.6 9C4.73312 8.69838 4.77282 8.36381 4.714 8.03941C4.65519 7.71502 4.50054 7.41568 4.27 7.18L4.21 7.12C4.02418 6.93418 3.87678 6.71358 3.77621 6.47079C3.67565 6.22801 3.62389 5.96779 3.62389 5.705C3.62389 5.44221 3.67565 5.18199 3.77621 4.93921C3.87678 4.69642 4.02418 4.47582 4.21 4.29C4.39582 4.10418 4.61642 3.95678 4.85921 3.85621C5.10199 3.75565 5.36221 3.70389 5.625 3.70389C5.88779 3.70389 6.14801 3.75565 6.39079 3.85621C6.63358 3.95678 6.85418 4.10418 7.04 4.29L7.1 4.35C7.33568 4.58054 7.63502 4.73519 7.95941 4.794C8.28381 4.85282 8.61838 4.81312 8.92 4.68H9C9.29577 4.55324 9.54802 4.34276 9.72569 4.07447C9.90337 3.80618 9.99872 3.49179 10 3.17V3C10 2.46957 10.2107 1.96086 10.5858 1.58579C10.9609 1.21071 11.4696 1 12 1C12.5304 1 13.0391 1.21071 13.4142 1.58579C13.7893 1.96086 14 2.46957 14 3V3.09C14.0028 3.41541 14.1011 3.73284 14.2826 4.00296C14.4641 4.27308 14.7208 4.48402 15.021 4.60963C15.3212 4.73525 15.6517 4.77003 15.9714 4.70966C16.2912 4.64929 16.5863 4.49642 16.82 4.27L16.88 4.21C17.2553 3.83472 17.7643 3.62389 18.295 3.62389C18.5578 3.62389 18.818 3.67565 19.0608 3.77621C19.3036 3.87678 19.5242 4.02418 19.71 4.21C19.8958 4.39582 20.0432 4.61642 20.1438 4.85921C20.2444 5.10199 20.2961 5.36221 20.2961 5.625C20.2961 5.88779 20.2444 6.14801 20.1438 6.39079C20.0432 6.63358 19.8958 6.85418 19.71 7.04L19.65 7.1C19.4195 7.33568 19.2648 7.63502 19.206 7.95941C19.1472 8.28381 19.1869 8.61838 19.32 8.92V9C19.4468 9.29577 19.6572 9.54802 19.9255 9.72569C20.1938 9.90337 20.5082 9.99872 20.83 10H21C21.5304 10 22.0391 10.2107 22.4142 10.5858C22.7893 10.9609 23 11.4696 23 12C23 12.5304 22.7893 13.0391 22.4142 13.4142C22.0391 13.7893 21.5304 14 21 14H20.91C20.5882 14.0013 20.2738 14.0966 20.0055 14.2743C19.7372 14.452 19.5268 14.7042 19.4 15Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                <!-- Inserir elemento de menu ativo -->
                                <a class="menu-text">Configurações</a>
                            </div>

                            <div class="arrow" id="arrow">
                                <svg width="12" height="8" viewBox="0 0 12 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M1.01873 1.95009L5.96899 6.99934L11.0182 2.04907L10.0282 1.03922L5.98879 4.99943L2.02858 0.960037L1.01873 1.95009Z" fill="#222222"/>
                                </svg>
                            </div>
                        </div>

                        <ul class="collapse-menu">
                            <li class="collapse-sublink">
                                <a class="submenu-item" @click="redirect('./sub-menu-1')">SubMenu 1</a>
                            </li>
                        </ul>

                    </li>
                </ul>            
                </nav>
            </div>
        </aside> 
    </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: "Sidebar",
    components: {

    },
    props: {
        menuActive: String,
    },
    data() {
        return {
            
        }
    },
    methods: {
        redirect(url){
            window.location.href = url;
        },
        showSubMenu(id){
            let className = document.getElementById(id).lastChild.className
            let classArrow = _.get(document.getElementById(id), 'nextElementSibling', null)

            if(className == "arrow" && classArrow){
                document.getElementById(id).lastChild.className = "arrow rotate" 
            } else if (classArrow) {
                document.getElementById(id).lastChild.className = "arrow"  
            }

            switch (id) {
                case 'balcao-menu':
                    if(className == "arrow"){
                        document.getElementsByClassName('collapse-menu')[0].className = "collapse-menu collapse-active"  
                    } else {
                        document.getElementsByClassName('collapse-menu')[0].className = "collapse-menu" 
                    }
                    break;
                case 'relatorios-menu':
                    if(className == "arrow"){
                        document.getElementsByClassName('collapse-menu')[1].className = "collapse-menu collapse-active"  
                    } else {
                        document.getElementsByClassName('collapse-menu')[1].className = "collapse-menu" 
                    } 
                    break;
                case 'integracoes-menu':
                    if(className == "arrow"){
                        document.getElementsByClassName('collapse-menu')[2].className = "collapse-menu collapse-active"  
                    } else {
                        document.getElementsByClassName('collapse-menu')[2].className = "collapse-menu" 
                    }
                    break;
                case 'configuracoes-menu':
                    if(className == "arrow"){
                        document.getElementsByClassName('collapse-menu')[3].className = "collapse-menu collapse-active"  
                    } else {
                        document.getElementsByClassName('collapse-menu')[3].className = "collapse-menu" 
                    } 
                    break;
            
                default:
                    break;
            }
        
        },


    },
    async mounted () {
        document.getElementById(this.menuActive).className = "menu-item active"
        document.getElementsByClassName('menu-item active')[0].querySelector(".menu-text").style.color = "#E6161E"
        document.getElementsByClassName('menu-item active')[0].querySelector(".menu-icon").style.display = "none"
        document.getElementsByClassName('menu-item active')[0].querySelector(".menu-icon-active").style.display = "flex"

    },
    watch:{
 
    },
    
}
</script>