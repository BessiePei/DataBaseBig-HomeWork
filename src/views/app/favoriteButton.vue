<template>
  <button @click="favor" class="loveButton"><i class="el-icon-star-off" />收藏</button>
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
            if (response.data.status === 1) {
              alert('收藏成功');
            } else if (response.data.status === 0) {
              alert('您已经收藏过此帖');
            }
            this.$router.go(0);
          }).catch(function (error) {
            alert('收藏失败');
            console.log(JSON.stringify(error));
          })
        } else if (this.source === 'dish') {
          favoriteDish(this.id, this.userinfo).then((response) => {
            if (response.data.status === 1) {
              alert('收藏成功');
            } else if (response.data.status === 0) {
              alert('您已经收藏过此菜品');
            }
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
  .loveButton {
    background-color: var(--orange);
	  background-image: linear-gradient(90deg, var(--orange) 0%, var(--lightorange) 74%);
	  border-radius: 20px;
	  border: 1px solid var(--orange);
	  color: var(--white);
	  cursor: pointer;
	  font-size: 0.8rem;
	  font-weight: bold;
	  letter-spacing: 0.1rem;
	  padding: 0.9rem 4rem;
	  text-transform: uppercase;
	  transition: transform 80ms ease-in;
  }
</style>
