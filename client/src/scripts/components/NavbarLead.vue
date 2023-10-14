<template>
    <!-- Desktop -->
    <div class="bg-white hidden md:flex items-center rounded-2xl h-20">
        <div class="flex items-center pl-4">
            <!-- SVG Botão para voltar -->
            <button @click="goBack" class="flex-shrink-0 mr-3">
                <svg width="19" height="17" viewBox="0 0 19 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M8.007 15.5L1 8.5L8.007 1.5" stroke="#EC0000" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round" />
                    <path d="M1 8.49304H18" stroke="#EC0000" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round" />
                </svg>
            </button>

            <!-- Nome e Role do Lead -->
            <div class="flex flex-col items-start">
                <h1 class="text-xl font-bold">{{ leadNome }}</h1>
                <span class="text-xs">{{ leadRole }}</span>
            </div>

            <div class="ml-4">
                <div class="dropdown-container">
                    <!-- Botão de abertura do dropdown -->
                    <div @click="toggleDropdown" class="selected-status-container">
                        <div class="selected-status-content"
                            :style="selectedStatus ? `background-color: ${selectedStatus.bgSelect};` : ''">
                            <div v-if="selectedStatus" :style="{ backgroundColor: selectedStatus.color }"
                                class="status-elipse"></div>
                            {{ selectedStatus ? selectedStatus.name : "Status" }}
                        </div>
                        <span class="chevron">
                            <svg width="12" height="8" viewBox="0 0 12 8" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path d="M11.2 1.62L5.6 7.5L0 1.62L1.12 0.5L5.6 5.12L10.08 0.5L11.2 1.62Z"
                                    fill="#222222" />
                            </svg>
                        </span>
                    </div>


                    <!-- Dropdown com os status -->
                    <div v-if="showDropdown" class="dropdown-box">
                        <p class="font-bold mt-3 mb-3 text-sm">Status do Funil</p>
                        <div v-for="status in statusLead" :key="status.name" class="status-item"
                            @click="selectStatus(status)">
                            <div
                                :class="['status-checkbox', (selectedStatus && selectedStatus.name === status.name) ? 'active-status' : '']">
                                <i v-if="selectedStatus && selectedStatus.name === status.name" class="check-icon">
                                    <svg width="11" height="8" viewBox="0 0 11 8" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path
                                            d="M3.66299 7.92818C3.39779 7.92813 3.14348 7.82273 2.95599 7.63518L0.293987 4.97218C0.116332 4.78273 0.0193527 4.5316 0.0235695 4.27191C0.0277863 4.01223 0.132869 3.76438 0.316581 3.58079C0.500294 3.39721 0.748224 3.2923 1.00791 3.28827C1.26759 3.28424 1.51866 3.3814 1.70799 3.55919L3.66299 5.51418L8.81199 0.365185C9.00059 0.183027 9.25319 0.082232 9.51539 0.0845105C9.77759 0.0867889 10.0284 0.191958 10.2138 0.377366C10.3992 0.562774 10.5044 0.813587 10.5067 1.07578C10.5089 1.33798 10.4081 1.59058 10.226 1.77918L4.36999 7.63518C4.18249 7.82273 3.92818 7.92813 3.66299 7.92818Z"
                                            fill="white" />
                                    </svg>
                                </i>
                            </div>
                            <div class="content" :style="`background-color: ${status.bgSelect};`">
                                <div :style="{ backgroundColor: status.color }" class="status-elipse"></div>
                                <span class="status-name">{{ status.name }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="ml-auto flex items-center pr-4">

            <div class="flex items-center">
                <!-- Avatar -->
                <div class="w-8 h-8 rounded-full bg-gray-200 text-gray-700 flex items-center justify-center">
                    {{ userInitials }}
                </div>

                <!-- Select com corretores -->
                <div class="flex flex-col items-start">
                    <div class="user-dropdown-container">
                        <!-- Botão de abertura do dropdown -->
                        <div @click="toggleUserDropdown" class="selected-user">
                            <span v-if="selectedUser.name">{{ selectedUser.name }}</span>
                            <span v-if="selectedUser.role" class="user-role">{{ selectedUser.role }}</span>
                            <span v-else>Atribuição</span>
                        </div>

                        <!-- Dropdown com os usuários -->
                        <div v-if="showUserDropdown" class="user-dropdown-box">
                            <p class="font-bold mt-3 mb-3 text-sm">Atribuição</p>
                            <div v-for="user in users" :key="user.id" @click="selectUser(user)" class="user-row">
                                <div :class="['atribuicao-checkbox', { 'active-status': selectedUser.id === user.id }]">
                                    <i v-if="selectedUser && selectedUser.id === user.id" class="check-icon">
                                        <svg width="11" height="8" viewBox="0 0 11 8" fill="none"
                                            xmlns="http://www.w3.org/2000/svg">
                                            <path
                                                d="M3.66299 7.92818C3.39779 7.92813 3.14348 7.82273 2.95599 7.63518L0.293987 4.97218C0.116332 4.78273 0.0193527 4.5316 0.0235695 4.27191C0.0277863 4.01223 0.132869 3.76438 0.316581 3.58079C0.500294 3.39721 0.748224 3.2923 1.00791 3.28827C1.26759 3.28424 1.51866 3.3814 1.70799 3.55919L3.66299 5.51418L8.81199 0.365185C9.00059 0.183027 9.25319 0.082232 9.51539 0.0845105C9.77759 0.0867889 10.0284 0.191958 10.2138 0.377366C10.3992 0.562774 10.5044 0.813587 10.5067 1.07578C10.5089 1.33798 10.4081 1.59058 10.226 1.77918L4.36999 7.63518C4.18249 7.82273 3.92818 7.92813 3.66299 7.92818Z"
                                                fill="white" />
                                        </svg>
                                    </i>
                                </div>
                                <span>{{ user.name }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


            <button class="ml-4 pr-3 pl-3 text-sm bg-white text-primary border border-primary h-11 rounded-xl"
                @click="modalProposta = true">Criar Proposta</button>
            <button class="ml-2.5 pr-3 pl-3 text-sm bg-primary h-11 rounded-xl text-white">Marcar como Negócio
                Fechado</button>
            <button class="ml-2.5 border rounded-xl h-11 pr-3 pl-3" @click="modalArquivar = true">
                <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M3.667 1.5L1 4.9V16.8C1.01049 17.2612 1.20367 17.6993 1.53708 18.0181C1.87049 18.3368 2.31683 18.5102 2.778 18.5H15.222C15.6832 18.5102 16.1295 18.3368 16.4629 18.0181C16.7963 17.6993 16.9895 17.2612 17 16.8V4.9L14.333 1.5H3.667Z"
                        stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M1 5.09998H17" stroke="black" stroke-width="1.5" stroke-linecap="round"
                        stroke-linejoin="round" />
                    <path d="M8.83203 8.5V12.5" stroke="black" stroke-width="1.5" stroke-linecap="round"
                        stroke-linejoin="round" />
                    <path d="M11.3906 12.152L8.89062 14.304L6.39062 12.152" stroke="black" stroke-width="1.5"
                        stroke-linecap="round" stroke-linejoin="round" />
                </svg>
            </button>
        </div>
    </div>

    <!-- Mobile -->
    <div class="bg-white rounded-2xl mx-4 p-3 h-auto lead-mobile md:hidden">
        <!-- Conjunto botão voltar/nome e role do lead -->
        <div class="flex items-center">
            <!-- SVG Botão para voltar -->
            <button @click="goBack" class="flex-shrink-0 mr-3">
                <svg width="19" height="17" viewBox="0 0 19 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M8.007 15.5L1 8.5L8.007 1.5" stroke="#EC0000" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round" />
                    <path d="M1 8.49304H18" stroke="#EC0000" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round" />
                </svg>
            </button>

            <!-- Nome e Role do Lead -->
            <div class="flex flex-col items-start">
                <h1 class="text-xl font-bold">{{ leadNome }}</h1>
                <span class="text-xs">{{ leadRole }}</span>
            </div>
        </div>

        <!-- Dropdowns Container -->
        <div class="grid grid-cols-2 gap-2 mt-3 items-center">
            <!-- Primeira coluna -->
            <div>
                <div class="dropdown-container">
                    <!-- Botão de abertura do dropdown -->
                    <div @click="toggleDropdown" class="selected-status-container">
                        <div class="selected-status-content"
                            :style="selectedStatus ? `background-color: ${selectedStatus.bgSelect};` : ''">
                            <div v-if="selectedStatus" :style="{ backgroundColor: selectedStatus.color }"
                                class="status-elipse"></div>
                            {{ selectedStatus ? selectedStatus.name : "Status" }}
                        </div>
                        <span class="chevron">
                            <svg width="12" height="8" viewBox="0 0 12 8" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path d="M11.2 1.62L5.6 7.5L0 1.62L1.12 0.5L5.6 5.12L10.08 0.5L11.2 1.62Z"
                                    fill="#222222" />
                            </svg>
                        </span>
                    </div>


                    <!-- Dropdown com os status -->
                    <div v-if="showDropdown" class="dropdown-box">
                        <p class="font-bold mt-3 mb-3 text-sm">Status do Funil</p>
                        <div v-for="status in statusLead" :key="status.name" class="status-item"
                            @click="selectStatus(status)">
                            <div
                                :class="['status-checkbox', (selectedStatus && selectedStatus.name === status.name) ? 'active-status' : '']">
                                <i v-if="selectedStatus && selectedStatus.name === status.name" class="check-icon">
                                    <svg width="11" height="8" viewBox="0 0 11 8" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path
                                            d="M3.66299 7.92818C3.39779 7.92813 3.14348 7.82273 2.95599 7.63518L0.293987 4.97218C0.116332 4.78273 0.0193527 4.5316 0.0235695 4.27191C0.0277863 4.01223 0.132869 3.76438 0.316581 3.58079C0.500294 3.39721 0.748224 3.2923 1.00791 3.28827C1.26759 3.28424 1.51866 3.3814 1.70799 3.55919L3.66299 5.51418L8.81199 0.365185C9.00059 0.183027 9.25319 0.082232 9.51539 0.0845105C9.77759 0.0867889 10.0284 0.191958 10.2138 0.377366C10.3992 0.562774 10.5044 0.813587 10.5067 1.07578C10.5089 1.33798 10.4081 1.59058 10.226 1.77918L4.36999 7.63518C4.18249 7.82273 3.92818 7.92813 3.66299 7.92818Z"
                                            fill="white" />
                                    </svg>
                                </i>
                            </div>
                            <div class="content" :style="`background-color: ${status.bgSelect};`">
                                <div :style="{ backgroundColor: status.color }" class="status-elipse"></div>
                                <span class="status-name">{{ status.name }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Segunda coluna -->
            <div>
                <div class="flex items-center">
                    <!-- Avatar -->
                    <div class="w-8 h-8 rounded-full bg-gray-200 text-gray-700 flex items-center justify-center">
                        {{ userInitials }}
                    </div>

                    <!-- Select com corretores e espaçamento entre Avatar -->
                    <div class="flex flex-col items-start">
                        <div class="user-dropdown-container">
                            <!-- Botão de abertura do dropdown -->
                            <div @click="toggleUserDropdown" class="selected-user">
                                <span v-if="selectedUser.name">{{ selectedUser.name }}</span>
                                <span v-if="selectedUser.role" class="user-role">{{ selectedUser.role }}</span>
                                <span v-else>Atribuição</span>
                            </div>

                            <!-- Dropdown com os usuários -->
                            <div v-if="showUserDropdown" class="user-dropdown-box">
                                <p class="font-bold mt-3 mb-3 text-sm">Atribuição</p>
                                <div v-for="user in users" :key="user.id" @click="selectUser(user)" class="user-row">
                                    <div
                                        :class="['atribuicao-checkbox', { 'active-status': selectedUser.id === user.id }]">
                                        <i v-if="selectedUser && selectedUser.id === user.id" class="check-icon">
                                            <svg width="11" height="8" viewBox="0 0 11 8" fill="none"
                                                xmlns="http://www.w3.org/2000/svg">
                                                <path
                                                    d="M3.66299 7.92818C3.39779 7.92813 3.14348 7.82273 2.95599 7.63518L0.293987 4.97218C0.116332 4.78273 0.0193527 4.5316 0.0235695 4.27191C0.0277863 4.01223 0.132869 3.76438 0.316581 3.58079C0.500294 3.39721 0.748224 3.2923 1.00791 3.28827C1.26759 3.28424 1.51866 3.3814 1.70799 3.55919L3.66299 5.51418L8.81199 0.365185C9.00059 0.183027 9.25319 0.082232 9.51539 0.0845105C9.77759 0.0867889 10.0284 0.191958 10.2138 0.377366C10.3992 0.562774 10.5044 0.813587 10.5067 1.07578C10.5089 1.33798 10.4081 1.59058 10.226 1.77918L4.36999 7.63518C4.18249 7.82273 3.92818 7.92813 3.66299 7.92818Z"
                                                    fill="white" />
                                            </svg>
                                        </i>
                                    </div>
                                    <span>{{ user.name }}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Botões -->
        <div class="mt-4 flex md:flex md:justify-end md:space-x-2">
            <button class="pr-3 pl-3 text-sm bg-white text-primary border border-primary h-11 rounded-xl mr-2"
                @click="modalProposta = true">Criar Proposta</button>
            <button class="pr-3 pl-3 text-sm bg-primary h-11 rounded-xl text-white mr-2">Negócio Fechado</button>
            <button class="border rounded-xl h-11 pr-3 pl-3" @click="modalArquivar = true">
                <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M3.667 1.5L1 4.9V16.8C1.01049 17.2612 1.20367 17.6993 1.53708 18.0181C1.87049 18.3368 2.31683 18.5102 2.778 18.5H15.222C15.6832 18.5102 16.1295 18.3368 16.4629 18.0181C16.7963 17.6993 16.9895 17.2612 17 16.8V4.9L14.333 1.5H3.667Z"
                        stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M1 5.09998H17" stroke="black" stroke-width="1.5" stroke-linecap="round"
                        stroke-linejoin="round" />
                    <path d="M8.83203 8.5V12.5" stroke="black" stroke-width="1.5" stroke-linecap="round"
                        stroke-linejoin="round" />
                    <path d="M11.3906 12.152L8.89062 14.304L6.39062 12.152" stroke="black" stroke-width="1.5"
                        stroke-linecap="round" stroke-linejoin="round" />
                </svg>
            </button>
        </div>
    </div>

    <Modal v-show="modalArquivar" @close="modalArquivar = false">
        <template v-slot:header>
            <div class="modal-close">
                <button :class="'fecharModal mt-4'" @click="modalArquivar = false">
                    <svg width="14" height="15" viewBox="0 0 14 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M13 1.5L1 13.5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M1 1.5L13 13.5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    </svg>
                </button>
            </div>

            <h2 class="modal-title">Arquivar Lead</h2>
        </template>

        <template v-slot:body>
            <form>
                <div class="mt-6">
                    <label for="motivoArquivo" class="label-default">Motivo*</label>
                    <select style="width: 100%;" name="motivoArquivo" id="motivoArquivo" class="mt-2">
                        <option value="">Selecione</option>
                        <option value="">1</option>
                        <option value="">2</option>
                    </select>
                </div>
            </form>

        </template>

        <template v-slot:footer>
            <div class="bnt-block">
                <button class="btn-red">Confirmar</button>
                <button class="btn-red-white">Cancelar</button>
            </div>
        </template>
    </Modal>

    <Modal v-show="modalProposta" @close="modalProposta = false">
        <template v-slot:header>
            <div class="modal-close">
                <button :class="'fecharModal mt-4'" @click="modalProposta = false">
                    <svg width="14" height="15" viewBox="0 0 14 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M13 1.5L1 13.5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M1 1.5L13 13.5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    </svg>
                </button>
            </div>

            <h2 class="modal-title">Criar Proposta</h2>
        </template>
        <template v-slot:body>
            <form action="">
                <div class="mt-4 mb-2">
                    <label for="" class="label-default mb-3">Selecione o imóvel</label>
                    <div class="flex items-center">
                        <input class="mr-2" type="radio" name="inputInteresse" id="interesse">
                        <label for="" class="mb-0 text-sm">Interesses</label>
                        <select class="ml-3 w-full" name="selectImoveisInteresse" id="imoveisInteresse">
                            <option value="0">Selecione</option>
                        </select>
                    </div>
                </div>
                <div class="mt-4 mb-2">
                    <div class="flex items-center">
                        <input class="mr-2" type="radio" name="inputInteresse" id="interesse">
                        <label for="" class="mb-0 text-sm">Outro</label>
                        <input type="text" placeholder="Digite o codigo do imóvel" name="codImovel" class="w-full ml-3">
                    </div>
                </div>
                <div class="mt-4 mb-2">
                    <label for="inputValorProposta" class="label-default">Valor da proposta</label>
                    <input type="text" class="w-full mt-2" name="inputProposta" id="inputValorProposta"
                        placeholder="R$">
                </div>
                <div class="mt-4 mb-2">
                    <label for="inputComentarios" class="label-default">Condições ou comentários</label>
                    <textarea name="inputCondicoesComentarios" id="inputComentarios" rows="5" class="w-full mt-2"></textarea>
                </div>
            </form>
        </template>
        <template v-slot:footer>
            <div class="block btn-grupo w-full">
                <div class="btn-arquivar">
                    <button class="btn-red w-full">Enviar</button>
                </div>
                <div class="btn-cancelar">
                    <button class="btn-red w-full">Cancelar</button>
                </div>
            </div>
        </template>
    </Modal>
</template>
<script>
import Modal from '@/components/Modal';
export default {
    name: "NavbarLead",
    components: {
        Modal,
    },
    data() {
        return {
            modalArquivar: false,
            modalProposta: false,
            leadNome: "Igor Henrique",
            leadRole: "Lead | Proprieário",
            showDropdown: false,
            showUserDropdown: false,
            selectedStatus: null,
            statusLead: [
                { name: "Novos", color: "rgb(29, 177, 255)", bgSelect: "rgb(212, 235, 252)" },
                { name: "Aguardando Atendimento", color: "rgb(113, 32, 207)", bgSelect: "rgb(226, 213, 246)"},
                { name: "Em atendimento", color: "rgb(228, 51, 221)", bgSelect: "rgb(243, 217, 248)"},
                { name: "Visita Agendada", color: "rgb(232, 71, 0)", bgSelect: "rgb(243, 219, 214)" },
                { name: "Visita Realizada", color: "rgb(232, 134, 0)", bgSelect: "rgb(243, 228, 213)" },
                { name: "Em negociação", color: "rgb(78, 182, 63)", bgSelect: "rgb(219, 236, 222)"},
            ],
            status: "",
            users: [
                { id: 1, name: "Alessandro Furlan", role: "Corretor", photo: "link da foto" },
            ],
            selectedUser: {}
        }
    },
    computed: {
        userInitials() {
            if (this.selectedUser && this.selectedUser.name) {
                const splitName = this.selectedUser.name.split(' ');
                return splitName.length > 1
                    ? splitName[0][0] + splitName[1][0]
                    : splitName[0][0];
            }
            return '';
        }
    },
    methods: {
        goBack() {
            this.$router.go(-1);
        },
        toggleDropdown() {
            this.showDropdown = !this.showDropdown;
        },
        selectStatus(status) {
            this.selectedStatus = status;
            this.showDropdown = false;
        },
        toggleUserDropdown() {
            this.showUserDropdown = !this.showUserDropdown;
        },
        selectUser(user) {
            this.selectedUser = user;
            this.showUserDropdown = false;
        },
    }
}
</script>
<style lang="scss" scoped>
@import "../../styles/index.scss";

.btn-red{
    display: flex;
    padding: 20px;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}


.btn-red-white{
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>