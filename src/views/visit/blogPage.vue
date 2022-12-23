<template>
  <div class="vpage">
    <myheader></myheader>
    <h1> 帖子主页 </h1>
    <img :src="$store.getters.imgUrl + blog.blogPicture" alt="activity-picture"/>
    <p>帖子名：{{blog.blogTitle}}</p>
    <p>帖子类型：{{blog.blogLabel}}</p>
    <p>发帖人：{{blog.blogPosterName}}</p>
    <p>帖子收藏人数：{{blog.blogFavoriterCnt}}</p>
    <p>帖子喜爱人数：{{blog.blogLikeCnt}}</p>
    <p>帖子发布时间：{{blog.blogDeliverTime}}</p>
    <favorite-button :source="'blog'" :id="id"></favorite-button>
    <h1>帖子评论</h1>
    <remark :source="'blog'" :id="id"></remark>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import { getBlogByID } from "../../api/blogs";
import Remark from "../app/remark";

export default {
  name: "blogPage",
  components: {
    Remark,
    myheader,
    myfooter
  },
  data() {
    return {
      id: -1,
      blog: {
        blogId: 0,
        blogLabel: 'xxx',
        blogTitle: '一个blog',
        blogPicture: '../../../static/images/blogImage.png',
        blogPosterName: '用户名',
        blogFavoriterCnt: 0,
        blogLikeCnt: 0,
        blogDeliverTime: 'xxxx年xx月xx日 xx:xx',
      },
    }
  },
  methods: {
    getData() {
      // 获取传递过来的id
      console.log(this.$route.params.id);
      this.id = this.$route.params.id;
      if (this.$route.params.id) {
        getBlogByID(this.$route.params.id).then((response) => {
          console.log(response.data);
          this.blog = response.data;
        })
      }
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
