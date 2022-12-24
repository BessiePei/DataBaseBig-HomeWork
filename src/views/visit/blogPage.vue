<template>
  <div class="vpage">
    <myheader></myheader>
    <div class="blog-card">
      <img :src="$store.getters.imgUrl + blog.blogPicture" alt="activity-picture"/>
      <div class="card-content">
        <p>帖子名：{{blog.blogTitle}}</p>
      <p>帖子类型：{{blog.blogLabel}}</p>
      <p>发帖人：{{blog.blogPosterName}}</p>
      <p>帖子收藏人数：{{blog.blogFavoriterCnt}}</p>
      <!--<p>帖子喜爱人数：{{blog.blogLikeCnt}}</p>-->
      <p>帖子发布时间：{{blog.day_time}} {{blog.min_time}}</p>
      <favorite-button :source="'blog'" :id="id"></favorite-button>
      </div>
    </div>
    <div class="blog-content-card">
      <h1>帖子内容</h1>
      <div class="blog-content">{{blog.blogContent}}</div>
    </div>
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
import favoriteButton from "../app/favoriteButton";
export default {
  name: "blogPage",
  components: {
    Remark,
    myheader,
    myfooter,
    favoriteButton
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
        blogDeliverTime: '2022-12-15T14:04:59.643933Z',
        blogContent: 'akvsduvgdfkhfksegbfdgnefsdgnfggsdgnregnhfgsfdgfsdsdhrtgeshrteesshrnthrsgfrtrgeaehth',
        day_time: '2022-12-15',
        min_time: '14:04',
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
        }).then((data)=>{
          console.log(data);
          console.log(this.blog);
          this.blog.day_time=this.blog.blogDeliverTime.slice(0,10),
          this.blog.min_time=this.blog.blogDeliverTime.slice(11,16)
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

  .blog-card {
    width: 580px;
  height: 280px;
  border-radius: 20px;
  background-color: blanchedalmond;
  box-shadow: 1px 1px #8c939d;
  margin: 20px auto;
  position: relative;
  top: 20px;
  display: flex;
  padding: 20px;
  }

  img {
    width: 240px;
    height: 240px;
  }

  .card-content {
    height: 240px;
    margin-left: 20px;
    text-align: left;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    /* border: 1px solid black; */
  }

  .blog-content-card {
    border-radius: 20px 20px 0 0;
    /* border: 1px solid black; */
    width: 580px;
    margin: 10px auto;
    font-size: 1rem;
    text-align: left;
    padding: 5px;
    background: rgba(217, 217, 217, 0.3);
  }

  .blog-content {
    border-top: 1px solid black;
    font-size: 1rem;
    text-align: left;
    position:relative;
    top: 5px;
    word-break: break-word;
    white-space: pre-line;
  }
</style>
