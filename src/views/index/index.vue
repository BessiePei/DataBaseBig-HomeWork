<template>
  <div id="index" class="vpage">
    <myheader></myheader>
    <slider></slider>
    <user-show></user-show>
    <merchantList></merchantList>
    <hotDishes></hotDishes>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import slider from "./slider";
import merchantList from './merchantList'
import hotDishes from './hotDishes'
import UserShow from "./userShow";
export default {
  name: "index",
  components: {
    UserShow,
    myheader,
    myfooter,
    slider,
    merchantList,
    hotDishes
  },
}
</script>

<style scoped>
{
  border: 1px solid black;
}
  .vpage {
    margin-top: 10vh;
    margin-bottom: 36px;
  }
  #index {
    display: flex;
    flex-direction: column;
    margin-top: 10vh;
    margin-bottom: 36px;
  }
  slider {
    position: center;
    margin: auto;
  }
</style>
