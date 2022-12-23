<template>
  <div class="vpage">
    <myheader></myheader>
    <div class="dish-card">
      <img class="dishImg" :src="$store.getters.imgUrl + dish.dishPicture" alt="activity-picture"/>
      <div class="dishInf">
      <p>菜品名称：{{dish.dishName}}</p>
      <p>菜品价格：￥{{dish.dishPrice}}</p>
      <p>菜品销售商家：{{dish.dishSeller}}</p>
      <p>菜品评分：{{dish.dishStars}}</p>
      <p>菜品简介：{{dish.dishBrief}}</p>
      <p>菜品口味：{{dish.dishTaste}}</p>
      <p>菜品收藏人数：{{dish.dishFollowerCnt}}</p>
      <favorite-button :source="'dish'" :id="id"></favorite-button>
      </div>
    </div>
    <h1>菜品评论</h1>
    <remark :source="'dish'" :id="id"></remark>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import { getDishByID } from "../../api/dishes";
import Remark from "../app/remark";
import FavoriteButton from "../app/favoriteButton";

export default {
  name: "dishPage",
  components: {
    FavoriteButton,
    Remark,
    myheader,
    myfooter
  },
  data() {
    return {
      id: -1,
      dish: {
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishRaw: '菜品原料',
        dishBrief: '菜品简介',
        dishTaste: '菜品口味',
        dishFollowerCnt: 0,
      }
    }
  },
  methods: {
    getData() {
      console.log(this.$route.params.id);
      this.id = this.$route.params.id;
      if (this.$route.params.id) {
        getDishByID(this.$route.params.id).then((response) => {
          this.dish = response.data;
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
@import "../../../static/css/dishPage.css";
  .vpage {
    margin-top: 10vh;
  }
</style>
