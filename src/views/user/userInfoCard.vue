<template>
  <div class="dish-card">
      <img :src="$store.getters.imgUrl + info.userPortrait" class="dishImg"/>
    <div class="dishInf">
      <h1 class="title">个人信息卡</h1>
      <p>昵称：{{info.username}}</p>
      <p>个性签名： {{info.userSignature}}</p>
      <p>性别： {{info.userSex===0 ? '女':'男'}}</p>
      <p>年级： {{info.userGrade}}</p>
      <p>偏好：{{info.userPrefer}}</p>
    </div>
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
        username: 'HangFood',
        userSignature: 'I love buaa food!',
        userSex: 0,
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
.dish-card {
  width: 700px;
  height: 350px;
  border-radius: 20px;
  background-color: blanchedalmond;
  box-shadow: 1px 1px #8c939d;
  position: relative;
  top: 20px;
  display: flex;
  padding: 20px;
}

.dishImg {
  width: 300px;
  height: 300px;
}

.dishInf {
  height: 300px;
  width: 400px;
  margin-left: 20px;
  text-align: left;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.title {
  font-weight: bold;
  font-size: 1.5rem;
}
</style>
