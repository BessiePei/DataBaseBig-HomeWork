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
    <button @click="dialogVisible=true">参加活动</button>
    <remark :source="'activity'" :id="id"></remark>
    <myfooter></myfooter>
    <el-dialog
      title="提示"
      :visible.sync="dialogVisible"
      width="30%"
      center>
      <el-form>
      <el-text>本平台只提供活动展示界面，具体活动参与方式与参与奖励等请见活动界面活动详情。活动最终解释权归活动主办方所有。本平台不承担任何法律责任。</el-text>
      <el-form-item label=" " required>
        <el-checkbox v-model="checked">我已知悉并同意。</el-checkbox>
      </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import { getActivityById } from "@/api/activities"
import {joinIn} from "../../api/activities";
import {mapGetters} from "vuex";
import Remark from "../app/remark";
export default {
  name: "activityPage",
  components: {
    Remark,
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
      dialogVisible: false,
      checked: false,
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
    },
    submit() {
      if (this.checked) {
        joinIn(this.id, this.userinfo).then((response) => {
          //console.log(response.data);
          alert('参与成功');
        })
        .catch(function (error) {
          alert('参与失败');
          console.log(error);
        });
      } else {
        alert('请先勾选同意');
      }

    },
    computed: {
      /* ES6 使用辅助函数mapGetters，将组件中的方法映射为score.getters调用 */
      ...mapGetters({
        userinfo: "userinfo",
      })
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
