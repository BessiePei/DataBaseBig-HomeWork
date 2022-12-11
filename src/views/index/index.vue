<template>
  <div id="index">
    <myheader></myheader>
      <slider class="slider_pos"></slider>
      <user-show class="user-show_pos"></user-show>
      <merchantList class="merchantList_pos"></merchantList>
      <hotDishes class="dishList_pos"></hotDishes>
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
/*
* {
  border: 1px solid black;
}
*/
  #index {
    margin-top: 10vh;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .slider_pos {
    order: 1;
    flex-shrink: 0;
    margin: 10px 10px 10px 5% ;
    /* position: absolute;
    margin: 10px 0;
    top: 10vh;
    left: 10%; */
  }

  .user-show_pos {
    order: 2;
    flex-shrink: 0;
    margin: 10px;
    /* position: absolute;
    margin: 10px 0;
    right: 10%;
    top: 10vh; */
  }

  .merchantList_pos {
    order: 3;
    flex-shrink: 0;
    margin: 10px;
    /* position: absolute;
    top: calc(10vh + 50vh + 80px);
    left: 10%; */
  }

  .dishList_pos {
    order: 4;
    flex-shrink: 0;
    margin: 10px;
    /* position: absolute;
    top: calc(10vh + 50vh + 80px);
    right: 10%; */
  }

  .footer {
    order: 5;
  }
</style>
