<template>
  <div class="header">
    <img class="bk-photo" src="static/images/header-background.png"/>
    <!--<c-popover placement="bottom" trigger="hover">
      <c-popover-trigger>
        <router-link :to="{path:'/'}">
          <img src="static/images/headLogo.png" />
        </router-link>
      </c-popover-trigger>
      <c-popover-content w="100px" fontSize="1em">
        <c-popover-arrow />
        点击返回首页
      </c-popover-content>
    </c-popover>-->
    <div class="h-content">
    <el-tooltip content="点击返回首页" placement="bottom" effect="light">
      <router-link :to="{path:'/'}">
          <img src="static/images/headLogo.png" />
        </router-link>
    </el-tooltip>
    <div class="middle">
      <div class="search">
        <input class="search-text" type="text" placeholder="快来搜索想吃的菜品吧" v-model="search" />
        <button class="search-btn" @click.enter="searches">搜索</button>
      </div>
    </div>
    <div class="buttons">
        <router-link :to="{path: '/visit'}"><button class="router-btn btn">逛逛</button></router-link>
        <div class="login" v-if="userinfo">
          <div v-if="userinfo.isMerchant">
            <router-link :to="{name: 'merchantPage', params: {id: userinfo.id}}">
              <button class="router-btn btn" >用户{{ userinfo.username }}</button>
            </router-link>
          </div>
          <div v-else>
            <router-link :to="{path: '/profile'}">
              <button class="router-btn btn" >用户{{ userinfo.username }}</button>
            </router-link>
          </div>
          <button @click="logout" class="btn">退出</button>
        </div>
        <div class="notLogin" v-else>
          <router-link :to="{path: '/reg'}"><button class="router-btn btn">登录/注册</button></router-link>
        </div>
    </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import {CPopover, CPopoverContent, CPopoverTrigger, CPopoverArrow} from "@chakra-ui/vue";
export default {
  name: "header",
  data() {
    return {
      search: '',
      /* userinfo: {username:'Hangfood'}, 仅用于排版 */
    }
  },
  methods: {
    logout() {
      console.log(this.userinfo);
      console.log("退出中。。。");
      this.$cookies.set("sessionid", "xxx");
      this.$cookies.isKey("sessionid");
      this.$cookies.remove("sessionid")
      this.$store.dispatch("delUser");
      this.$router.push("/"); //跳转到首页
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
  img {
    height: 10vh;
  }

</style>
