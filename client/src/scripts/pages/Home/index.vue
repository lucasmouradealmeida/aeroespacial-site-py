<template>
    <div class="main">
        <div class="menu">
            <div class="logo">
                <a>Engenharia Aeroespacial</a>
            </div>
            <div class="pages">
                <a class="label" href="/">Home</a>
                <a class="label" href="#item1">Item 1</a>
                <a class="label" href="#item2">Item 2</a>
                <a class="label" href="#item3">Item 3</a>
                <div class="userimg"></div>
                <div class="user">
                    <label class="username">Admin</label>
                    <label class="usermail">admin@admin.com</label>
                </div>
            </div>
        </div>

        <div class="content">
            <div class="content-home">
                <div class="pagetitle">
                    <label class="title">Sistema Solar</label>
                    <label class="subtitle">Conheça mais sobre o sistema solar</label>
                    <div class="divider"></div>
                </div>

                <div class="cards">
                    <div class="card sun"></div>
                    <div class="card"></div>
                    <div class="card"></div>
                </div>

                <div class="cards">
                    <div class="card"></div>
                    <div class="card"></div>
                    <div class="card"></div>
                </div>

                <div class="cards">
                    <div class="card"></div>
                    <div class="card"></div>
                    <div class="card"></div>
                </div>
            </div>
            <div class="content-item1">

            </div>


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
}
</script>

<style lang="scss">

.main{
    width: 100%;
}

.content{
    background-color: #222;
}

.pagetitle{
    display: flex;
    flex-direction: column;

    .title{
        font-size: 50px;
        font-weight: 700;
        color: #fff;
        margin-left: 40px;
        margin-top: 20px;
    }

    .subtitle{
        font-size: 18px;
        font-weight: 400;
        color: #fff;
        margin-left: 40px;
    }

    .divider{
        width: 90%;
        height: 1px;
        background-color: #fff;
        margin-top: 20px;
        margin-left: 40px;
    }
}

.cards{
    display: flex;
    flex-direction: row;

    .card{
        width: 30%;
        height: 250px;
        border-radius: 20px;
        margin: 40px;
        cursor: pointer;

        &:hover{
            box-shadow: 0px 0px 10px 0px rgba(255, 255, 255, 0.75);
        }
    }

    .sun{
        background-image: url('https://spaceplace.nasa.gov/gallery-sun/en/solar-flare.en.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
}


.menu{
    display: flex;
    align-items: center;
    gap: 20px;
    height: 80px;
    background-color: #222;
    border-bottom: 2px solid #fff;

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
            font-weight: 700;
            color: #fff;
            cursor: pointer;
        }

    }

    .userimg{
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background-color: #fff;
        justify-content: center;
        align-items: center;
    }

    .user{
        display: flex;
        flex-direction: column;
        align-items: center;

        .username{
            font-size: 20px;
            font-weight: 700;
            color: #fff;
        }

        .usermail{
            font-size: 15px;
            font-weight: 400;
            color: #fff;
        }
    }

}


</style>