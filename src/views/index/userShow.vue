<template>
  <div id="userShow">
    <div class="avatar avatar_pos">
      <img src="static/images/CartoonCharacter.jpg"/>
    </div>
    <p class="text_pos" v-if="hasLogin">{{userinfo.username}}</p>
    <p class="text_pos" v-else>快来登录吧！</p>
    <div class="btn-grp">
      <router-link :to="{path: '/reg'}"><button class="btn" v-show="!hasLogin">登录/注册</button></router-link>
      <router-link :to="{path: '/openShopPage'}"><button class="btn"  v-show="!hasLogin">开店</button></router-link>
      <div v-if="hasLogin">
        <router-link :to="{path: '/profile'}">
          <button class="btn" v-show="!isMerchant">个人主页</button>
        </router-link>
        <router-link :to="{name: 'merchantPage', params: {id: userinfo.id}}">
          <button class="btn" v-show="isMerchant">商家主页</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "userShow",
  data() {
    return {
      hasLogin: false,
      isMerchant: false,
    }
  },
  created() {
    if (this.userinfo) {
      this.hasLogin = true;
    }
    if (this.userinfo.isMerchant) {
      this.isMerchant = true;
    }
  },
  computed: {
    /* ES6 使用辅助函数mapGetters，将组件中的方法映射为score.getters调用 */
    ...mapGetters({
      userinfo: "userinfo",
    })
  }
}
</script>

<style scoped>
  #userShow {
    width: 30%;
    max-width: 400px;
    background-color: whitesmoke;
    border: 2px solid var(--orange);
    height: calc(50vh + 2rem + 10px);
    box-shadow: 1px 1px #8c939d;
  }

  .avatar {
    width: 160px;
    height: 160px;
    border-radius: 100%;
    overflow: hidden;
  }

  .avatar_pos {
    position: relative;
    top: 2rem;
    left: 50%;
    transform: translate(-50%, 0);
  }

  .text_pos {
    position: relative;
    top: 60px;
    left: 50%;
    transform: translate(-50%);
  }

  .btn-grp {
    position: relative;
    top: 90px;
    left: 50%;
    transform: translate(-50%);
    width: 100%;
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
	  padding: 0.5rem 1rem;
	  text-transform: uppercase;
	  transition: transform 80ms ease-in;
  }
</style>
