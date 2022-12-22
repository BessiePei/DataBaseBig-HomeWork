<template>
  <div class="remark">
    <div class="sendRemark" v-if="userinfo">
      <input v-model="content" placeholder="快来发表你的评论吧" />
      <button @click="postRemark"><i class="el-icon-s-promotion"/>发布评论</button>
    </div>
    <p v-else>请先登录再发表评论哦！</p>
    <p>相关评论</p>
    <div class="blogs">
      <el-card shadow="hover" v-for="remark in lists" :key="remark.commentId">
        <p>评论发布者：{{remark.commenter.username}}</p>
        <p>评论时间：{{remark.commentDeliverTime}}</p>
        <p>评论内容：{{remark.commentContent}}</p>
      </el-card>
    </div>
  </div>
</template>

<script>
import {getBlogRemark, postBlogRemark} from "../../api/blogs";
import {getDishRemark, postDishRemark} from "../../api/dishes";
import {getActivityRemark, postActivityRemark} from "../../api/activities";
import {mapGetters} from "vuex";

export default {
  name: "remark",
  props: {
    source: {
      type: String,
      required: true,
    },
    id: Number,
  },
  data() {
    return {
      content: '',
      lists: [{
        commentId: 999,
        commentContent: 'xxx',
        commenter: {
          username: "小碗菜21",
          email: "125346@qq.com"
        },
        commentDeliverTime: 'xxx-xxx-xx 00:00',
      }],
    }
  },
  methods: {
    getBlogRemarkData() {
      getBlogRemark(this.id).then((response) => {
          //console.log(response.data);
          this.lists = response.data;
          console.log("blogRemarks: " + JSON.stringify(this.lists));
        })
        .catch(function (error) {
          console.log(error);
        });
      console.log(this.lists);
    },
    getDishRemarkData() {
      getDishRemark(this.id).then((response) => {
          //console.log(response.data);
          this.lists = response.data;
          console.log("dishRemarks: " + JSON.stringify(this.lists));
        })
        .catch(function (error) {
          console.log(error);
        });
      console.log(this.lists);
    },
    getActivityRemarkData() {
      getActivityRemark(this.id).then((response) => {
          //console.log(response.data);
          this.lists = response.data;
          console.log("activityRemarks: " + JSON.stringify(this.lists));
        })
        .catch(function (error) {
          console.log(error);
        });
      console.log(this.lists);
    },
    postRemark() {
      if (this.source === 'blog') {
        postBlogRemark(this.id, this.content).then((response)=>{
          alert('提交成功');
          this.lists.unshift(response.data);
          // this.$router.go(0);
        }).catch(function(error) {
          alert('提交失败');
          console.log(JSON.stringify(error));
        })
      } else if (this.source === 'dish') {
        postDishRemark(this.id, this.content).then((response)=>{
          alert('提交成功');
          this.lists.unshift(response.data);
          // this.$router.go(0);
        }).catch(function(error) {
          alert('提交失败');
          console.log(JSON.stringify(error));
        })
      } else if (this.source === 'activity') {
        postActivityRemark(this.id, this.content).then((response)=>{
          alert('提交成功');
          this.lists.unshift(response.data);
          // this.$router.go(0);
        }).catch(function(error) {
          alert('提交失败');
          console.log(JSON.stringify(error));
        })
      }
      console.log(this.content);
      /* var now = new Date();
      this.lists.unshift({
        commentId: 1000,
        commentContent: this.content,
        commentPosterName: this.userinfo.username,
        commentDeliverTime: now.toLocaleTimeString(),
      }) */
    }
  },
  created() {
    if (this.source === 'blog') {
      this.getBlogRemarkData();
    } else if (this.source === 'dish') {
      this.getDishRemarkData();
    } else if (this.source === 'activity') {
      this.getActivityRemarkData();
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
