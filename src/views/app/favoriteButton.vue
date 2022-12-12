<template>
  <button @click="favor">收藏</button>
</template>

<script>
import {favoriteBlog} from "../../api/blogs";
import {favoriteDish} from "../../api/dishes";
import {mapGetters} from "vuex";

export default {
  name: "favoriteButton",
  props: {
    source: {
      type: String,
      required: true,
    },
    id: Number,
  },
  methods: {
    favor() {
      if (this.userinfo) {
        if (this.source === 'blog') {
          favoriteBlog(this.id, this.userinfo).then((response) => {
            alert('收藏成功');
            this.$router.go(0);
          }).catch(function (error) {
            alert('收藏失败');
            console.log(JSON.stringify(error));
          })
        } else if (this.source === 'dish') {
          favoriteDish(this.blog, this.userinfo).then((response) => {
            alert('收藏成功');
            this.$router.go(0);
          }).catch(function (error) {
            alert('收藏失败');
            console.log(JSON.stringify(error));
          })
        }
      } else {
        alert('请先登录再收藏');
      }
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

</style>
