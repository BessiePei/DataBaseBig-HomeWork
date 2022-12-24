<template>
  <div class="app-container">
    <h1 class="slider__title">进行中的活动</h1>
    <p v-if="lists.length===0">还未发布任何活动</p>
    <div class="swiper" v-else>
      <swiper ref="mySwiper" :options="swiperOptions">
        <swiper-slide v-for="activity in lists" :key="activity.activityId">
            <div class="activity-card">
              <img :src="$store.getters.imgUrl + activity.activityHeadPhoto" alt="activity-picture"/>
              <div class="activity-content">
              <p>活动名称：{{activity.activityName}}</p>
              <p>活动简介：{{activity.activityBrief}}</p>
              <p>活动时间：{{activity.activityBegin}}~{{activity.activityEnd}}</p>
              <p>活动主办方：{{activity.activityOrganizerName}}</p>
                <el-button v-show='isMerchant && username === activity.activityOrganizerName' type="danger"
                           icon="el-icon-delete" circle  @click="deleteActivity(activity.activityId)"></el-button>
              </div>
              <router-link :to="{name: 'activityPage', params: {id: activity.activityId}}">
                <button class="btn btn_pos">点击进入了解活动详情</button>
              </router-link>
            </div>
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
import {deleteMerchantActivity, getMerchantActivities} from "../../api/merchants";
export default {
  name: "default",
  props: {
    id: {
      type: Number,
      default: -1,
    }
  },
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
      isMerchant: false,
      username: '',
    };
  },
  components: {
    swiper,
    swiperSlide,
  },
  methods: {
    getData() {
      if (this.id === -1) {
        getSlide()
        .then((response) => {
          //console.log(response.data);
          this.lists = response.data;
          console.log("slide " + JSON.stringify(this.lists));
        })
        .catch(function (error) {
          console.log(error);
        });
        console.log(this.lists);
      } else {
        getMerchantActivities(this.id).then((response) => {
          //console.log(response.data);
          this.lists = response.data;
          console.log("merchant activities " + JSON.stringify(this.lists));
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    },
    deleteActivity(id) {
      deleteMerchantActivity(id).then((response) => {
        this.lists = this.lists.filter(function (item) {
          return item.activityId !== id;
        });
      }).catch(function (error){
        alert("删除失败");
        console.log(error)
      })
    }
  },
  created() {
    if (this.$store.state.userinfo) {
      this.isMerchant = this.$store.state.userinfo.isMerchant;
      this.username = this.$store.state.userinfo.username;
    }
    this.getData();
  },
};
</script>

<style scope>
  .app-container {
    /* border: 1px solid black; */
    width: 50%;
    max-width: 600px;
    background: white;
  }

  .slider__title {
    font-size: 2rem;
    font-weight: bold;
  }

  .swiper {
    height: 50vh;
    overflow: hidden;
    border-radius: 20px;
    box-shadow: 1px 1px #8c939d;
  }

  .activity-card {
    /*border: 1px solid black;*/
  }

  .activity-content {
    z-index: 3;
    position: absolute;
    top: 4rem;
    width: 80%;
    left: 10%;
    padding: 10px;
    background-color: rgba(245, 245, 245, 0.8);
    border: 1px dashed grey;
  }

  .swiper-pagination {
    position: absolute;
    top: calc(50vh - 45px);
  }

  .btn {
	background-color: var(--orange);
	background-image: linear-gradient(90deg, var(--orange) 0%, var(--lightorange) 74%);
	border-radius: 20px;
	border: 1px solid var(--orange);
	color: var(--white);
	cursor: pointer;
	font-size: 0.8rem;
	font-weight: bold;
	letter-spacing: 0.1rem;
	padding: 0.5rem;
	text-transform: uppercase;
	transition: transform 80ms ease-in;
}
  .btn_pos {
    position: absolute;
    top: 230px;
    width: 40%;
    left: 30%;
  }

</style>
