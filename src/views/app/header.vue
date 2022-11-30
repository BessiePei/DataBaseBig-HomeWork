<template>
  <div class="header">
    <router-link :to="{path:'/'}"><p class="logo">航食</p></router-link>
    <div class="middle">
      <div class="search">
        <input class="search-text" type="text" placeholder="快来搜索想吃的菜品吧" v-model="search" />
        <button class="search-btn" @click.enter="searches">搜索</button>
      </div>
    </div>
    <div class="buttons">
        <router-link :to="{path: '/visit'}"><button class="router-btn">逛逛</button></router-link>
        <div class="login" v-if="userinfo">
          <router-link :to="{path: '/profile'}"><button class="router-btn" >用户{{userinfo.username}}</button></router-link>
          <a @click="logout">退出</a>
        </div>
        <div class="notLogin" v-else>
          <router-link :to="{path: '/reg'}"><button class="router-btn">登录/注册</button></router-link>
        </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  name: "header",
  data() {
    return {
      search: '',
      /* userinfo: {username:'Hangfood'}, 仅用于排版*/
    }
  },
  methods: {
    logout() {
      this.$store.dispatch("delUser");
    },
    searches() {
      const _this = this;
      _this.$router.push({name: 'searchPage', params: {content: this.search}})
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
  @import "../../../static/css/header.css";
</style>
