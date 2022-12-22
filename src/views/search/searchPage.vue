<template>
  <div class="vpage">
    <myheader></myheader>
    <h1>这里是搜索结果展示界面</h1>
    <p>搜索内容：{{this.content}}</p>
    <div class="dishes">
      <el-card :body-style="{ padding: '0px',width: '200px'}" shadow="hover" v-for="dish in result" :key="dish.dishId">
        <router-link :to="{name: 'dishPage', params: {id: dish.dishId}}">
          <img :src="dish.dishPicture" alt="activity-picture"/>
          <span class="name">{{dish.dishName}}</span>
          <div class="price" >￥{{dish.dishPrice}}</div>
          <div class="seller">{{dish.dishSeller}}</div>
          <div class="mark"><i class="el-icon-s-marketing"/>{{dish.dishStars}}</div>
          <div class="love"><i class="el-icon-star-off" />{{dish.dishFollowerCnt}}</div>
        </router-link>
        <el-button v-show='isMerchant && username === dish.dishSeller' type="danger" icon="el-icon-delete" circle  @click="deleteDish(dish.dishId)"></el-button>
      </el-card>
    </div>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import {searchContent} from "../../api/dishes";
export default {
  name: "searchPage",
  components: {
    myheader,
    myfooter
  },
  data() {
    return {
      content: '',
      result: [{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      }],

    }
  },
  created() {
    this.content = this.$route.params.content;
    searchContent(this.content).then((response) => {
          //console.log(response.data);
          this.result = response.data;
          console.log("searchResult: " + JSON.stringify(this.result));
        })
        .catch(function (error) {
          console.log(error);
        });
      console.log(this.result);
  },
  updated() {
    this.content = this.$route.params.content;
  }
}
</script>

<style scoped>
  .vpage {
    margin-top: 10vh;
    margin-bottom: 36px;
  }
</style>
