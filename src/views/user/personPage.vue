<template>
  <div class="vpage">
    <myheader></myheader>
    <h1 class="title">个人主页</h1>
    <user-info-card></user-info-card>
    <user-tools></user-tools>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import userInfoCard from "./userInfoCard";
import userTools from "./userTools";

export default {
  name: "personPage",
  components: {
    myheader,
    myfooter,
    userInfoCard,
    userTools
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
