<template>
    <div class="main">


        <div class="header">
            <a class="logo">/explore</a>

            <div class="menu">
                <a class="menu-item">universe</a>
                <a class="menu-item">posicionamento</a>
                <a class="menu-item">manobras</a>
                <a class="menu-item">lagrange</a>
            </div>
        </div>

        <div class="content">

        </div>

        <div class="footer">

        </div>



    </div>
</template>
<script>


export default {
    name: "Home",
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
<style lang="scss" scoped>
@import "../../../styles/pages/home";


</style>