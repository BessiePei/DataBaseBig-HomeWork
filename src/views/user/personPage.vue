<template>
  <div class="vpage">
    <myheader></myheader>
    <h1>个人主页</h1>
    <img :src="info.userPortrait"/>
    <p>用户名：{{info.userName}}</p>
    <p>个性签名： {{info.userSignature}}</p>
    <p>性别： {{info.userSex}}</p>
    <p>学号： {{info.userNumber}}</p>
    <p>年级： {{info.userGrade}}</p>
    <p>偏好：{{info.userPrefer}}</p>
    <p>此处还差操作没有写</p>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import { getUsersByID,updateUsers} from "../../api/users";

export default {
  name: "personPage",
  components: {
    myheader,
    myfooter,
  },
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
        this.info=response.data.data;
      }).catch (function(error){
        console.lg(error);
      })
    },
    updateUserinfo() {
      updateUsers(this.info).then((response) => {
        alert('修改成功')
      }).catch(function(error){
        alert(JSON.stringify(error));
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
