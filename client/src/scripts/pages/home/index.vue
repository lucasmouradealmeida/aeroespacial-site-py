<template>

</template>
<script>


export default {
    name: "home",
    components: {

    },
    data() {
        return {

        }
    },
    methods:{
        teste(){

        }
    },
    mounted() {
        if (/Mobi/.test(navigator.userAgent)) {
            // O usuário está em um dispositivo móvel, redirecione para a versão móvel.
            console.log('redirect for not developed page')
        }
    },
}
</script>
<style lang="scss">
    
</style>