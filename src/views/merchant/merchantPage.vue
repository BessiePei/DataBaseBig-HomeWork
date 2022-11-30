<template>
  <div class="vpage">
    <myheader></myheader>
    <h1>窗口主页</h1>
    <img :src="info.merchantPortrait"/>
    <p>商家名：{{info.merchantName}}</p>
    <p>商家电话： {{info.merchantPhone}}</p>
    <p>商家评分： {{info.merchantStars}}</p>
    <p>营业时间： {{info.merchantOpen}}~{{info.merchantClose}}</p>
    <p>商家地址： {{info.merchantAddr}}</p>
    <p>收藏该窗口的用户数：{{info.merchantFollowerCnt}}</p>
    <h1>窗口活动</h1>
    <p>这里是获取活动，展示活动的组件</p>
    <h1>窗口菜品</h1>
    <p>这里缺获取菜品和展示菜品的组件</p>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import { getMerChantByID } from "@/api/merchants";

export default {
  name: "merchantPage",
  components: {
    myheader,
    myfooter
  },
  data() {
    return {
      id: -1,
      info: {
        merchantName: '学一食堂xx窗口',
        merchantPortrait: '../../../static/images/userPortrait.png',
        merchantPhone: '123456789',
        merchantStars: 5.0,
        merchantAddr: '和一楼四楼清真食堂左手第一个窗口',
        merchantOpen: '9:00',
        merchantClose: '19:00',
        merchantFollowerCnt: 0,
      }
    }
  },
  methods: {
    getData() {
      console.log(this.$route.params.id);
      this.id = this.$route.params.id;
      if (this.$route.params.id) {
        getMerChantByID(this.$route.params.id).then((response) => {
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
