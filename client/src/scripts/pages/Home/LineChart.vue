<template>
    <div>
      <canvas ref="chart"></canvas>
    </div>
  </template>
  
  <script>
 import { Chart, registerables } from 'chart.js';
  Chart.register(...registerables);
  
  export default {
    extends: Chart,
    data() {
      return {

      };
    },
    mounted() {
      this.chart = new Chart(this.$refs.chart, {
        type: 'line',
        data: this.chartData,
        options: this.options,
      });
    },
    methods: {
      update() {
        this.chart.update();
      },
    },
    props: {
      chartData: {
        type: Object,
        default: null,
      },
      options: {
        type: Object,
        default: null,
      },
    },
  };
  </script>
  