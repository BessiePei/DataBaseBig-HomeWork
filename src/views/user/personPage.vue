<template>
  <div class="vpage">
    <myheader></myheader>
    <h1 class="title">个人主页</h1>
    <user-info-card></user-info-card>
    <div id="main" style="width: 600px; height: 600px"></div>
    <user-tools></user-tools>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import userInfoCard from "./userInfoCard";
import userTools from "./userTools";
import echarts from 'echarts';
import {getChart} from "../../api/users";
export default {
  name: "personPage",
  components: {
    myheader,
    myfooter,
    userInfoCard,
    userTools
  },
  methods: {
    echartsInit() {
        var chartDom = document.getElementById('main');
        var myChart = echarts.init(chartDom);
        var option;
option = {
  legend: {
    top: 'bottom'
  },
  toolbox: {
    show: true,
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  series: [
    {
      name: 'Nightingale Chart',
      type: 'pie',
      radius: [50, 250],
      center: ['50%', '50%'],
      roseType: 'area',
      itemStyle: {
        borderRadius: 8
      },
      data: [
        { value: 40, name: 'rose 1' },
        { value: 38, name: 'rose 2' },
        { value: 32, name: 'rose 3' },
        { value: 30, name: 'rose 4' },
        { value: 28, name: 'rose 5' },
        { value: 26, name: 'rose 6' },
        { value: 22, name: 'rose 7' },
        { value: 18, name: 'rose 8' }
      ]
    }
  ]
};
        getChart().then((response) => {
          option.data = response.data;
        }).catch (function(error){
          console.log(error);
        })


option && myChart.setOption(option);
      }
  },
  mounted() {
    console.log("mounted");

    this.echartsInit();
  },
}
</script>

<style scoped>
  .vpage {
    margin-top: 10vh;
    margin-bottom: 36px;
  }

  .title {
    font-size: 2rem;
    font-weight: bold;
  }


</style>
