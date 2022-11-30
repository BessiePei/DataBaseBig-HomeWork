<template>
  <div id="hot-dishes">
    <h1> 热门菜品 </h1>
    <div class="dishes">
      <el-card shadow="hover" v-for="dish in lists" :key="dish.dishId">
        <router-link :to="{name: 'dishPage', params: {id: dish.dishId}}">
          <img :src="dish.dishPicture" alt="activity-picture"/>
          <p>菜品名称：{{dish.dishName}}</p>
          <p>菜品价格：￥{{dish.dishPrice}}</p>
          <p>菜品销售商家：{{dish.dishSeller}}</p>
          <p>菜品评分：{{dish.dishStars}}</p>
          <p>菜品收藏人数：{{dish.dishFollowerCnt}}</p>
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
          this.lists = response.data.data;
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

</style>
