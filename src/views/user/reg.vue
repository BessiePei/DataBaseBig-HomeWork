/* 用户登录 */
<template>
  <div class="body-bg">
  <div class="container right-panel-active">
    <!-- Sign Up -->
    <div class="container__form container--signup">
        <form action="#" class="form" id="form1">
            <h2 class="form__title">注 册</h2>
            <input type="text" placeholder="用户名" class="input" v-model="username" required/>
            <li class="error_box" id="username_notice">
              <em>{{err_username}}</em>
            </li>
            <input type="email" placeholder="邮箱" class="input" v-model="email" required/>
            <li class="error_box" id="email_notice">
              <em>{{err_email}}</em>
            </li>
            <input type="password" placeholder="密码" class="input" v-model="password" required/>
            <li class="error_box" id="password_notice">
              <em>8-15位，包含大小写，包含数字，否则会注册不成功{{err_password}}</em>
            </li>
            <button class="btn" @click="register">注 册</button>
        </form>
    </div>

    <!-- Sign In -->
    <div class="container__form container--signin">
        <form action="#" class="form" id="form2">
            <h2 class="form__title">登 录</h2>
            <input type="text" placeholder="用户名" class="input" v-model="username2" required/>
            <li class="error_box" id="username2_notice">
              <em>{{err_username2}}</em>
            </li>
            <input type="password" placeholder="密码" class="input" v-model="password2" required/>
            <a href="#" class="link">忘记密码？</a>
            <li class="error_box" id="password2_notice">
              <em>{{err_password2}}</em>
            </li>
            <button class="btn" @click="login">登 录</button>
        </form>
    </div>

    <!-- Overlay -->
    <div class="container__overlay">
        <div class="overlay">
            <div class="overlay__panel overlay--left">
                <button class="btn" id="signIn">登 录</button>
            </div>
            <div class="overlay__panel overlay--right">
                <button class="btn" id="signUp">注 册</button>
            </div>
        </div>
    </div>
  </div>
  </div>
</template>

<script>
import { reg } from '@/api/users';
import { login } from '@/api/users';
export default {
  name: "reg",
  data() {
    return {
      username: "",
      password: "",
      email: "",
      err_username: "",
      err_password: "",
      err_email: "",
      username2: "",
      password2: "",
      err_username2: "",
      err_password2: ""
    }
  },
  /*beforeCreate() {
    document.querySelector('body').setAttribute('style', 'margin:0;')
  },*/
  mounted() {
        let script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = '../../../static/js/login.js';
        document.body.appendChild(script);
  },
  methods: {
    register() {
      var that = this;
      that.err_username = "";
      that.err_password = "";
      that.err_email = "";
      reg({
        username: this.username,
        password: this.password,
        email: this.email,
      })
        .then((response) => {
          console.log(response.data);
          if (response.status === 201) {
            that.$message({
								message: "注册成功，请直接登录",
								type: "success",
            })
            /*
            localStorage.setItem("userinfo", response.data);
            this.$store.dispatch("saveUser", response.data);
            this.username = "";
            this.password = "";
            this.$router.push("/"); //跳转到首页*/
          }
        })
        .catch(function (error) {
          console.log(error);
          alert("注冊失敗");
          if ("non_field_errors" in error) {
            that.error = error.non_field_errors[0];
          }
          if ("username" in error) {
            that.err_username = error.username[0];
          }
          if ("password" in error) {
            that.err_password = error.password[0];
          }
          if ("email" in error) {
            that.err_email = error.email[0];
          }
        });
    },
    login() {
      var that = this;
      login({
        username: this.username2,
        password: this.password2,
      })
        .then((Response) => {
          console.log(Response);
          if (Response.status === 200) {
            //保存数据到本地存储
            console.log(Response.data);
            //同时保存到vuex
            // this.saveUser(Response.data);
            // localStorage.setItem('user',{'token':Response.data.token,'id':Response.data.id,'username':Response.data.username});
            localStorage.setItem("userinfo", Response.data);
            this.$store.dispatch("saveUser", Response.data);
            // console.log(this.$store.user.id);
            this.username2 = "";
            this.password2 = "";
            this.$router.push("/"); //跳转到首页
            alert('登录成功');
          }
        })
        .catch(function (error) {
          if ("username" in error) {
            that.err_username2 = error.username[0];
          } else if ("password" in error) {
            that.err_password2 = error.password[0];
          } else {
            alert("登录失败");
          }
        });
    },
  },
}
</script>

<style scoped>
@import "../../../static/css/login.css";
</style>
