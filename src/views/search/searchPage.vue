<template>
  <div class="vpage">
    <myheader></myheader>
    <h1>这里是搜索结果展示界面</h1>
    <p>搜索内容：{{this.content}}</p>
    <p>还没写怎么连后端</p>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
export default {
  name: "searchPage",
  components: {
    myheader,
    myfooter
  },
  data() {
    return {
      content: '',
      result: {},

    }
  },
  created() {
    this.content = this.$route.params.content;

  },
  update() {
    this.content = this.$route.params.content;
  }
}
</script>

<style scoped>
  .vpage {
    margin-top: 10vh;
    margin-bottom: 36px;
  }
</style>
