<template>
  <div class="vpage">
    <myheader></myheader>
    <div class="header-mes">
      <p class="mes">搜索内容：{{this.content}}</p>
      <div class="sort">
      <p class="text">价格范围</p>
      <el-input-number v-model="lowborder" :precision="2" :step="0.1" :max="500" :min="0"></el-input-number>
      <p class="text">~</p>
      <el-input-number v-model="highborder" :precision="2" :step="0.1" :max="500" :min="0"></el-input-number>
      <button @click="filterPrice" class="btn-grey">筛选</button>
      <button v-show="!sorted || flag" @click="sortAPrice" class="btn-grey">价格升序排列</button>
      <button v-show="!sorted || !flag" @click="sortDPrice" class="btn-grey">价格降序排列</button>
      </div>
    </div>
    <div class="dishes">
      <p v-show="showData.length === 0">没有符合条件的商品</p>
      <el-card :body-style="{ padding: '5px',width: '200px'}" shadow="hover" v-for="dish in showData" :key="dish.dishId" class="dish-item">
        <router-link :to="{name: 'dishPage', params: {id: dish.dishId}}">
          <img :src="$store.getters.imgUrl + dish.dishPicture" alt="activity-picture"/>
            <span class="name">{{dish.dishName}}</span>
            <div class="price" >￥{{dish.dishPrice}}</div>
            <div class="seller">{{dish.dishSeller}}</div>
            <div class="mark"><i class="el-icon-s-marketing"/>{{dish.dishStars}}</div>
            <div class="love"><i class="el-icon-star-off" />{{dish.dishFollowerCnt}}</div>
        </router-link>
      </el-card>
    </div>
    <el-pagination @size-change="sizeChange" @current-change="currentChange" :current-page="page" :page-size="size"
                   :page-sizes="pageSizes" layout="total, sizes, prev, pager, next, jumper" :total="total">
    </el-pagination>
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
        dishName: '面包1',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 1.2,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包2',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 8.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包3',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.0,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包4',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 120,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包5',
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
        dishName: '面包8',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      },{
        dishId: 999,
        dishName: '面包9',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      }],
      total: 0,  //总共多少条
      page: 1,  // 页码
      size: 10, // 一页多少数据
      showData: [],
      sorted: false,
      flag: true,
      lowborder: 0,
      highborder: 500,
      ftmp: [],
    }
  },
  methods: {
    getShowData() {
      this.showData = this.ftmp.slice(
        (this.page - 1) * this.size,
        this.page * this.size
      );
      this.total = this.ftmp.length;
    },
    // page改变时的回调函数，参数为当前页码
    currentChange(val) {
      console.log("翻页，当前为第几页",val);
      this.page = val;
      this.getShowData();
    },
    // size改变时回调的函数，参数为当前size
    sizeChange(val) {
      console.log("改变每页数据条数，当前一页多少条数据", val);
      this.size = val;
      this.page = 1;
      this.getShowData();
    },
    sortAPrice() {
      this.ftmp.sort((a,b) => {
        return a.dishPrice - b.dishPrice;
      });
      this.page = 1;
      this.getShowData();
      this.flag= !this.flag;
      this.sorted = true;
    },
    sortDPrice() {
      this.ftmp.sort((a,b) => {
        return b.dishPrice - a.dishPrice;
      });
      this.page = 1;
      this.getShowData();
      this.flag= !this.flag;
      this.sorted = true;
    },
    filterPrice() {
      this.ftmp = this.result.filter((item) => {
        return item.dishPrice >= this.lowborder && item.dishPrice <= this.highborder;
      })
      this.page=1;
      this.getShowData();
    }
  },
  created() {
    this.content = this.$route.params.content;
    console.log("create" + this.content);
    searchContent({search: this.content}).then((response) => {
          //console.log(response.data);
          this.result = response.data;
          console.log("searchResult: " + JSON.stringify(this.result));
          console.log(this.result);
          this.ftmp = this.result;
          this.getShowData();
        })
        .catch(function (error) {
          console.log(error);
        });
  },
  updated() {
    this.content = this.$route.params.content;
     console.log("update" + this.content);
  },
  watch: {
    $route: {
      handler: function(newl, oldl) {
        this.getShowData();
      }
    }

  }
}
</script>

<style scoped>
  @import "../../../static/css/searchPage.css";
  .vpage {
    margin-top: 10vh;
    margin-bottom: 36px;
  }
</style>
