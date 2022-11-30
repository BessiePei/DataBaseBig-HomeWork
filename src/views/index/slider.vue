<template>
  <div class="app-container">
    <h1>进行中的活动</h1>
    <div class="swiper">
      <swiper ref="mySwiper" :options="swiperOptions">
        <swiper-slide v-for="activity in lists" :key="activity.activityId">
          <router-link :to="{name: 'activityPage', params: {id: activity.activityId}}">
            <div class="activity-card">
              <img :src="activity.activityHeadPhoto" alt="activity-picture"/>
              <p>活动名称：{{activity.activityName}}</p>
              <p>活动简介：{{activity.activityBrief}}</p>
              <p>活动时间：{{activity.activityBegin}}~{{activity.activityEnd}}</p>
              <p>活动主办方：{{activity.activityOrganizerName}}</p>
            </div>
          </router-link>
        </swiper-slide>
        <div class="swiper-pagination" slot="pagination"></div>
      </swiper>
    </div>
  </div>
</template>

<script>
import { swiper, swiperSlide } from "vue-awesome-swiper";
import { getSlide } from "@/api/activities"; //引入api里面定义的方法
import "swiper/css/swiper.css";
export default {
  name: "default",
  data() {
    return {
      swiperOptions: {
        loop: true,
        autoplay: {
          delay: 3000,
          stopOnLastSlide: false,
        },
        pagination: {
          el: ".swiper-pagination", //与slot="pagination"处 class 一致
          clickable: true, //轮播按钮支持点击
          autoplay: true,
        },
      },
      lists: [],
    };
  },
  components: {
    swiper,
    swiperSlide,
  },
  methods: {
    getData() {
      getSlide()
        .then((response) => {
          //console.log(response.data);
          this.lists = response.data.data;
          console.log("slide " + JSON.stringify(this.lists));
        })
        .catch(function (error) {
          console.log(error);
        });
      this.lists.unshift({
        activityId: 999,
        activityName: '光盘行动',
        activityBrief: '让我们一起光盘吧',
        activityBegin: '2022.11.30',
        activityEnd: '2022.12.30',
        activityOrganizerName: '学六食堂',
        activityHeadPhoto: '../../../static/images/poster.png'
      });
      console.log(this.lists);
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style scope>


</style>
