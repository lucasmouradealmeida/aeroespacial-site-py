<template>
    <div class="temperature-container">
      <!-- SVG de frio -->
      <img src="static/img/temperatura-fria.svg" alt="Frio" class="temperature-icon" />
  
      <!-- TemperatureRange -->
      <div class="temperature-range">
        <!-- Parte do frio -->
        <div class="temperature-section cold"></div>
  
        <!-- Parte do morno -->
        <div class="temperature-section moderate"></div>
  
        <!-- Parte do quente -->
        <div class="temperature-section hot"></div>
  
        <div class="ellipse-temperatura" :style="{ left: temperaturePosition }"></div>
      </div>
  
  
      <!-- SVG de quente -->
      <img src="static/img/temperatura-quente.svg" alt="Quente" class="temperature-icon" />
    </div>
</template>
<script>
export default {
    name: "TemperaturaLead",
    props: {
        temperaturaSelecionada: String,
    },
    computed: {
        temperaturePosition() {
            if (this.temperaturaSelecionada === "frio") {
                return "0%";
            } else if (this.temperaturaSelecionada === "morno") {
                return "48%";
            } else if (this.temperaturaSelecionada === "quente") {
                return "94%";
            } else {
                return "0%";
            }
        },
    },
}
</script>
<style lang="scss">
  .temperature-container {
    display: flex;
    align-items: center;

    .temperature-icon {
      margin: 0 5px;
    }

    .temperature-range {
      flex-grow: 1;
      display: flex;
      align-items: center;
      height: 20px;
      position: relative;
    }

    .temperature-section {
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      text-align: center;
      overflow: hidden;
      height: 15px;
    }

    .temperature-section.cold {
      background-color: #1DB1FF;
      height: 10px;
      width: 33.33%;
      border-top-left-radius: 20px;
      border-bottom-left-radius: 20px;
    }

    .temperature-section.moderate {
      background-color: #EBAB2F;
      height: 10px;
      width: 33.33%;
    }

    .temperature-section.hot {
      background-color: #E84700;
      height: 10px;
      width: 33.33%;
      border-bottom-right-radius: 20px;
      border-top-right-radius: 20px;
    }

    .ellipse-temperatura {
      width: 20px;
      height: 20px;
      background-color: #fff;
      border-radius: 50%;
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      transition: left 0.2s ease-in-out;
      border: 1px solid #EC0000;
    }

  }
</style>