<template>
  <div class="vpage">
    <myheader></myheader>
    <h1>逛逛主页</h1>
    <div class="blogs">
      <el-card shadow="hover" v-for="blog in lists" :key="blog.blogId">
        <router-link :to="{name: 'blogPage', params: {id: blog.blogId}}">
          <img :src="blog.blogPicture" alt="activity-picture"/>
          <p>帖子名：{{blog.blogTitle}}</p>
          <p>帖子类型：{{blog.blogLabel}}</p>
          <p>发帖人：{{blog.blogPosterName}}</p>
          <p>帖子收藏人数：{{blog.blogFavoriterCnt}}</p>
          <p>帖子喜爱人数：{{blog.blogLikeCnt}}</p>
        </router-link>
      </el-card>
    </div>
    <myfooter></myfooter>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import { getVisitBlogs } from "@/api/blogs";
export default {
  name: "visitPage",
  components: {
    myheader,
    myfooter
  },
  data() {
    return {
      lists: [{
        blogId: 999,
        blogLabel: 'xxx',
        blogTitle: '一个blog',
        blogPicture: '../../../static/images/blogImage.png',
        blogPosterName: '用户名',
        blogFavoriterCnt: 0,
        blogLikeCnt: 0,
      }],
    }
  },
  methods: {
    getData() {
      getVisitBlogs()
        .then((response) => {
          //console.log(response.data);
          this.lists = response.data.data;
          console.log("visitBlogs: " + JSON.stringify(this.lists));
        })
        .catch(function (error) {
          console.log(error);
        });
      console.log(this.lists);
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
