<template>
  <div id="userShow">
    <div class="avatar">
      <img src="static/images/CartoonCharacter.jpg"/>
      <p>快来登录吧！</p>
    </div>
    <router-link :to="{path: '/reg'}"><button>登录/注册</button></router-link>
    <router-link :to="{path: '/openShopPage'}"><button>开店</button></router-link>
    <router-link :to="{path: '/profile'}"><button>个人主页</button></router-link>
  </div>
</template>

<script>
export default {
  name: "userShow"
}
</script>

<style scoped>

</style>
