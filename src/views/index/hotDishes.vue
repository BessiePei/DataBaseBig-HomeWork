<template>
  <div id="hot-dishes">
    <h1 class="title"> 热门菜品 </h1>
    <div class="dishes">
      <el-card :body-style="{ padding: '0px',width: '200px'}" shadow="hover" v-for="dish in lists" :key="dish.dishId">
        <router-link :to="{name: 'dishPage', params: {id: dish.dishId}}">
          <img :src="dish.dishPicture" alt="activity-picture"/>
          <span class="name">{{dish.dishName}}</span>
          <div class="price" >￥{{dish.dishPrice}}</div>
          <div class="seller">{{dish.dishSeller}}</div>
          <div class="mark"><i class="el-icon-s-marketing"/>{{dish.dishStars}}</div>
          <div class="love"><i class="el-icon-star-off" />{{dish.dishFollowerCnt}}</div>
        </router-link>
      </el-card>
    </div>
  </div>
</template>

<script>
import {getHotDishes} from '@/api/dishes'
export default {
  name: "hotDishes",
  components: {
    getHotDishes
  },
  data() {
    return {
      lists: [{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      }]
    }
  },
  methods: {
    getData() {
      getHotDishes()
        .then((response) => {
          //console.log(response.data);
          this.lists = response.data;
          console.log("hotDishes: " + JSON.stringify(this.lists));
        })
        .catch(function (error) {
          console.log(error);
        });
      console.log(this.lists);
    }
  },
  created() {
    this.getData();
  }
}
</script>

<style scoped>
  #hot-dishes {
    width: 60%;
  }

  .title {
    font-size: 2rem;
    font-weight: bold;
  }

  .dishes {
    display: flex;
    flex-wrap: wrap;
  }

  img {
    width: 100%;
    height: 200px;
  }

  .name {
    float: left;
    font-size: 1.5rem;
    font-weight: bold;
    margin: 5px;
  }

  .price {
    float: right;
    color: red;
    font-size: 1.2rem;
    font-weight: bold;
  }

  .seller {
    float: left;
    color: #8c939d;
    font-size: 0.8rem;
    position: relative;
    top: 1rem;
    left: -3.5rem;
    margin: 5px;
  }

  .mark {
    float: right;
  }

  .love {
    float: right;
  }
</style>
