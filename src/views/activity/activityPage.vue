<template>
  <div class="vpage">
    <myheader></myheader>
    <h1>活动界面</h1>
    <img :src="activity.activityHeadPhoto" alt="activity-picture"/>
    <p>活动名称：{{activity.activityName}}</p>
    <p>活动简介：{{activity.activityBrief}}</p>
    <p>活动时间：{{activity.activityBegin}}~{{activity.activityEnd}}</p>
    <router-link :to="{name: 'canteenPage', params: {id: activity.activityOrganizerId}}">
      <p>活动主办方：{{activity.activityOrganizerName}}</p>
    </router-link>
    <p>活动内容： {{activity.activityContent}}</p>
    <p>活动参与人数： {{activity.activityPersonCnt}}</p>
    <p>活动发帖人员：{{activity.activityPerson}}</p>
    <p>这里加一个发帖组件，获取关于这个活动的帖子！需要后端的列表信息。</p>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import { getActivityById } from "@/api/activities"
export default {
  name: "activityPage",
  components: {
    myheader,
    myfooter
  },
  data() {
    return {
      id: -1,
      activity: {
        activityId: 999,
        activityName: '光盘行动',
        activityBrief: '让我们一起光盘吧',
        activityBegin: '2022.11.30',
        activityEnd: '2022.12.30',
        activityOrganizerName: '学一食堂',
        activityOrganizerId: 999,
        activityHeadPhoto: '../../../static/images/poster.png',
        activityContent: '坚持40天光盘行动并将打卡发送到xxx，凭借打卡记录到学六食堂领取奖品，一等奖xxx,二等将xxx。',
        activityPerson: '',
        activityPersonCnt: 0,
      },
    }
  },
  methods: {
    getData() {
      // 获取传递过来的id
      console.log(this.$route.params.id);
      this.id = this.$route.params.id;
      if (this.$route.params.id) {
        getActivityById(this.$route.params.id).then((response) => {
          console.log(response.data.data);
          this.activity = response.data;
        })
      }
    }
  },
  created() {
    this.getData();
  }
}
</script>

<style scoped>
  .vpage {
    margin-top: 10vh;
    margin-bottom: 36px;
  }

</style>
