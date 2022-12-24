<template>
  <div class="vpage">
    <myheader></myheader>
    <user-info-card></user-info-card>
    <div id="main" style="width: 400px; height: 400px"></div>
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
        /*
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
      name: '收藏菜品数据分析图',
      type: 'pie',
      radius: [50, 250],
      center: ['50%', '50%'],
      roseType: 'area',
      itemStyle: {
        borderRadius: 8
      },
      data: [
        { value: 1, name: 'rose 1' },
        { value: 2, name: 'rose 2' },
        { value: 0, name: 'rose 3' },
        { value: 3, name: 'rose 4' },
        { value: 4, name: 'rose 5' },
        { value: 0, name: 'rose 6' },
        { value: 2, name: 'rose 7' },
        { value: 5, name: 'rose 8' }
      ]
    }
  ]
};
*/
  myChart.setOption({
    legend: {
    top: 'bottom'
  },
  title: {
    text: '收藏菜品分类统计',
    left: 'center',
    top: 'center'
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
      type: 'pie',
      data: [
        { value: 1, name: 'rose 1' },
        { value: 2, name: '窗口xx' },
        { value: 0, name: '窗口1' },
        { value: 3, name: 'rose 4' }, ],
      radius: ['40%', '70%']
    }
  ]
});
        getChart().then((response) => {
          console.log(response.data);
          myChart.setOption({
            series: [
              {
                type: 'pie',
                data: response.data,
                radius: ['40%', '70%']
              }
            ]
          });
        }).catch (function(error){
          console.log(error);
        })

        window.onresize = myChart.resize();
      }
  },
  mounted() {
    console.log("mounted");
    setTimeout(() => {
            this.echartsInit() // 绘制图表
        }, 0)
  },
}
</script>

<style scoped>
  .vpage {
    margin-top: 10vh;
    margin-bottom: 36px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .title {
    font-size: 2rem;
    font-weight: bold;
  }


</style>
