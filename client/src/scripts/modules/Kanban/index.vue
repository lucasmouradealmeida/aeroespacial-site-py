<template>
    <div class="kanban-container">
        <div class="kanban">
            <div class="column" v-for="(column, columnIndex) in columns" :key="columnIndex" :data-column-index="columnIndex">
                <div :class="'column-title-card' + columnIndex" :style="{ backgroundColor: column.bgColor, color: column.textColor,}">
                    <div class="elipse" :style="{ backgroundColor: column.elipseColor }"></div>
                    {{ column.title }}
                </div>

                <draggable style="min-height: 100vh;" :group="{ name: 'kanban' }" :animation="200" handle=".card" scroll-sensitivity="100" scroll-speed="10" :list="column.leads" @start="onDragStart" @end="onDragEnd">
                    <div v-for="(lead, index) in column.leads" :key="lead.id">
                        <div>
                            <LeadCard :lead="lead" @click="handleCardClick(lead.faseLead)" class="card" />
                        </div>
                    </div>
                </draggable>
            </div>
        </div>
    </div>
</template>

<script>
    import LeadCard from '@/components/LeadCard';
    import { VueDraggableNext } from 'vue-draggable-next';

    export default {
    components: {
        LeadCard,
        draggable: VueDraggableNext,
    },
    data() {
        return {
            columns: [
                {
                    title: 'Novo',
                    bgColor: '#D4EBFC',
                    textColor: '#1DB1FF',
                    elipseColor: '#1DB1FF',
                    leads: [
                        { nomeLead: "Igor", telefoneLead: "11999999999", faseLead: "Novo" },
                    ],
                },
                {
                    title: 'Aguardando atendimento',
                    bgColor: '#E2D5F6',
                    textColor: '#7120CF',
                    elipseColor: '#7120CF',
                    leads: [
                        { nomeLead: "André Master Legend", telefoneLead: "11999999999", faseLead: "Visita realizada" },
                        { nomeLead: "Igor", telefoneLead: "11999999999", faseLead: "Em atendimento" },
                        { nomeLead: "Igor", telefoneLead: "11999999999", faseLead: "Em atendimento" },
                    ],
                },
                {
                    title: 'Em atendimento',
                    bgColor: '#F3D9F8',
                    textColor: '#E433DD',
                    elipseColor: '#E433DD',
                    leads: [
                        { nomeLead: "Igor", telefoneLead: "11999999999", faseLead: "Em atendimento" },
                    ],
                },
                {
                    title: 'Visita agendada',
                    bgColor: '#F3DBD6',
                    textColor: '#E84700',
                    elipseColor: '#E84700',
                    leads: [],
                },
                {
                    title: 'Visita realizada',
                    bgColor: '#F3E4D5',
                    textColor: '#E88600',
                    elipseColor: '#E88600',
                    leads: [],
                },
                {
                    title: 'Em negociação',
                    bgColor: '#DBECDE',
                    textColor: '#4EB63F',
                    elipseColor: '#4EB63F',
                    leads: [],
                },
            ],
            sourceLead: null,
            sourceColumnIndex: null,
            leadsArray: [],
            totalCount: 0,
        };
    },
    methods: {
        handleCardClick(title) {
            console.log('Clicked card with title:', title);
        },

        // realiza o fetch para recuperar os leads dentro do componente LeadCard.vue
        async fetchFunilLeads() {
            try {
                const apiUrl = `/funil-api`;
                const rawResponse = await fetch(apiUrl, {
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                    },
                });

                const response = await rawResponse.json();
                this.leadsArray = response.nodes;
                this.totalCount = response.totalCount;
                this.$parent.totalCount = this.totalCount;


                this.columns.forEach((column) => {
                    column.leads = response.nodes.filter((lead) => lead.faseLead === column.title);
                });

            } catch (error) {
                console.error('Erro ao buscar os dados do funil:', error);
            }
        },
        
        // atualiza o status do lead
        async atualizarStatusLead() {

            const fields = {
                idLead: 6,
                idStatusLead: 3,
            }

            try {
                const rawResponse = await fetch(`/atualizarlead-api`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.cookie.replace(/(?:(?:^|.*;\s*)csrf_token\s*=\s*([^;]*).*$)|^.*$/, "$1"),
                    },
                    body: JSON.stringify({
                        query: fields,
                    }),
                })

                const response = await rawResponse.json();

            } catch (error) {
                console.error('Erro ao atualizar o status do lead:', error);
            }
        },

        // captura o "start" do card
        onDragStart(event) {
            this.sourceLead = event.item;
            this.sourceColumnIndex = event.from.dataset.columnIndex;
        },

        // captura o "término" do movimento de arrastar no card e limpa as variáveis
        onDragEnd(event) {
            const destinationColumnIndex = event.to.dataset.columnIndex;
            if (this.sourceColumnIndex !== null && destinationColumnIndex !== undefined) {
                const sourceColumn = this.columns[this.sourceColumnIndex];
                const destinationColumn = this.columns[destinationColumnIndex];

                const sourceLeadIndex = sourceColumn.leads.indexOf(this.sourceLead);
                if (sourceLeadIndex > -1) {
                    sourceColumn.leads.splice(sourceLeadIndex, 1);
                    destinationColumn.leads.splice(event.newIndex, 0, this.sourceLead);
                    this.sourceLead.faseLead = destinationColumn.title;
                }
            }

            // função para atualizar o status do lead
            this.atualizarStatusLead();

            this.sourceLead = null;
            this.sourceColumnIndex = null;
        },
    },
    async mounted() {
        await this.fetchFunilLeads();
    },
};
</script>