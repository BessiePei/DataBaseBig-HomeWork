<template>
  <div class="vpage">
    <myheader></myheader>
    <h1>食堂主页</h1>
    <p>食堂名：{{info.canteenName}}</p>
    <p>食堂地址：{{info.canteenAddr}}</p>
    <p>食堂电话：{{info.canteenPhone}}</p>
    <h1>食堂下属窗口</h1>
    <p>缺窗口列表组件，从后端获取数据展示,请给我数据列表</p>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import { getCanteenByID } from "../../api/merchants";

export default {
  name: "canteenPage",
  components: {
    myheader,
    myfooter
  },
  data() {
    return {
      id: -1,
      info: {
        canteenName: '食堂名',
        canteenAddr: '食堂地址',
        canteenPhone: '食堂电话',
      }
    }
  },
  methods: {
    getData() {
      console.log(this.$route.params.id);
      this.id = this.$route.params.id;
      if (this.$route.params.id) {
        getCanteenByID(this.$route.params.id).then((response) => {
          this.info=response.data.data;
        }).catch (function(error){
          console.log(error);
        })
      }
    },
  },
  created() {
    this.getData();
  }
}
</script>

<style scoped>
  .vpage {
    margin-top: 10vh;
    margin-bottom: 36px;
  }
</style>
