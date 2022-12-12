<template>
  <div class="user-card">
      <img :src="info.userPortrait"/>
      <p>用户名：{{info.userName}}</p>
      <p>个性签名： {{info.userSignature}}</p>
      <p>性别： {{info.userSex}}</p>
      <p>学号： {{info.userNumber}}</p>
      <p>年级： {{info.userGrade}}</p>
      <p>偏好：{{info.userPrefer}}</p>
  </div>
</template>

<script>
import {getUsersByID} from "../../api/users";

export default {
  name: "userInfoCard",
  data() {
    return {
      info: {
        userId: 0,
        userName: 'HangFood',
        userPassword: '',
        userEmail: '',
        userSignature: 'I love buaa food!',
        userNumber: '19521025',
        userSex: '男',
        userGrade: '本科',
        userPortrait: '../../../static/images/userPortrait.png',
        userPrefer: '食物',
      }
    }
  },
  methods: {
    getData() {
      getUsersByID().then((response) => {
        this.info = response.data;
      }).catch(function (error) {
        console.lg(error);
      })
    },
  },
  created() {
    this.getData();
  }
}
</script>

<style scoped>

</style>
