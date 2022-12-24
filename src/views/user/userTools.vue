<template>
  <div class="userTools">
    <el-tabs v-model="activeName" type="border-card" @tab-click="handleClick">
      <el-tab-pane label="我的菜品" name="myDish">
        我的菜品
        <p v-show="dishes.length === 0">你还未收藏任何菜品，快去收藏您喜欢的菜品吧！</p>
        <el-card :body-style="{ padding: '0px',width: '200px'}" shadow="hover" v-for="dish in dishes" :key="dish.dishId">
          <router-link :to="{name: 'dishPage', params: {id: dish.dishId}}">
            <img :src="$store.getters.imgUrl + dish.dishPicture" alt="activity-picture"/>
            <span class="name">{{dish.dishName}}</span>
            <div class="price" >￥{{dish.dishPrice}}</div>
            <div class="seller">{{dish.dishSeller}}</div>
            <div class="mark"><i class="el-icon-s-marketing"/>{{dish.dishStars}}</div>
            <div class="love"><i class="el-icon-star-off" />{{dish.dishFollowerCnt}}</div>
          </router-link>
          <el-button type="danger" icon="el-icon-delete" circle  @click="deleteDish(dish.dishId)"></el-button>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="我的活动" name="myActivity">
        我的活动
        <p v-show="activities.length === 0">你还未参加任何活动，快去参加您感兴趣的活动吧！</p>
        <el-card shadow="hover" v-for="activity in activities" :key="activity.activityId">
          <router-link :to="{name: 'activityPage', params: {id: activity.activityId}}">
            <img :src="$store.getters.imgUrl + activity.activityHeadPhoto" alt="activity-picture"/>
            <p>活动名称：{{activity.activityName}}</p>
            <p>活动简介：{{activity.activityBrief}}</p>
            <p>活动时间：{{activity.activityBegin}}~{{activity.activityEnd}}</p>
            <p>活动主办方：{{activity.activityOrganizerName}}</p>
          </router-link>
          <el-button type="danger" icon="el-icon-delete" circle  @click="deleteActivity(activity.activityId)"></el-button>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="我发布的帖子" name="myBlog">
        我发布的帖子
        <p v-show="blogs.length === 0">你还未发布任何帖子，快去逛逛页面发帖吧！</p>
        <el-card shadow="hover" v-for="blog in blogs" :key="blog.blogId">
        <router-link :to="{name: 'blogPage', params: {id: blog.blogId}}">
          <img :src="$store.getters.imgUrl + blog.blogPicture" alt="activity-picture"/>
          <p>帖子名：{{blog.blogTitle}}</p>
          <p>帖子类型：{{blog.blogLabel}}</p>
          <p>发帖人：{{blog.blogPosterName}}</p>
          <p>帖子收藏人数：{{blog.blogFavoriterCnt}}</p>
          <p>帖子喜爱人数：{{blog.blogLikeCnt}}</p>
        </router-link>
          <el-button type="danger" icon="el-icon-delete" circle  @click="deleteLoveBlog(blog.blogId)"></el-button>
      </el-card>
      </el-tab-pane>
      <el-tab-pane label="我收藏的帖子" name="myLoveBlog">
        我收藏的帖子
        <p v-show="loveBlogs.length === 0">你还未收藏任何帖子，快去逛逛看吧！</p>
        <el-card shadow="hover" v-for="blog in loveBlogs" :key="blog.blogId">
          <router-link :to="{name: 'blogPage', params: {id: blog.blogId}}">
            <img :src="$store.getters.imgUrl + blog.blogPicture" alt="activity-picture"/>
            <p>帖子名：{{blog.blogTitle}}</p>
            <p>帖子类型：{{blog.blogLabel}}</p>
            <p>发帖人：{{blog.blogPosterName}}</p>
            <p>帖子收藏人数：{{blog.blogFavoriterCnt}}</p>
            <p>帖子喜爱人数：{{blog.blogLikeCnt}}</p>
          </router-link>
          <el-button type="danger" icon="el-icon-delete" circle  @click="deleteBlog(blog.blogId)"></el-button>
        </el-card>
      </el-tab-pane>
      <el-tab-pane label="修改个人信息" name="myInfo">
        修改个人信息
        <p>昵称：</p>
        <input v-model="info.username" required/>
        <p>邮箱：</p>
        <input type="email" v-model="info.email" required/>
        <p>个性签名；</p>
        <input v-model="info.userSignature" type="text"/>
        <p>用户头像：</p>
        <el-upload action="https://jsonplaceholder.typicode.com/posts/" :limit="1" list-type="picture-card" :auto-upload="false"
					:on-change='handleUpload' :on-preview="handlePictureCardPreview" :on-remove="handleRemove" :file-list="fileList">
					<i slot="default" class="el-icon-plus"></i>
          <template #tip>
            <div class="el-upload__tip">只能上传一张图片，如不上传默认为原头像不变。</div>
          </template>
          <div slot="file" slot-scope="{ file }">
						<img class="el-upload-list__item-thumbnail" :src="file.url" alt="" />
						<span class="el-upload-list__item-actions">
							<!--<span class="el-upload-list__item-preview" @click="handlePictureCardPreview(file)">
								<i class="el-icon-zoom-in"></i>
							</span>-->
							<!--<span v-if="!disabled" class="el-upload-list__item-delete" @click="handleDownload(file)">
								<i class="el-icon-download"></i>
							</span>-->
							<span v-if="!disabled" class="el-upload-list__item-delete" @click="handleRemove(file, fileList)">
								<i class="el-icon-delete"></i>
							</span>
						</span>
					</div>
        </el-upload>
        <!--<p>学号：</p>
        <input v-model="info.userNumber" />-->
        <p>用户年级</p>
        <el-select v-model="info.userGrade" placeholder="请选择">
          <el-option
            v-for="item in options"
            :key="item"
            :label="item"
            :value="item">
          </el-option>
        </el-select>
        <p>性别：</p>
        <el-radio v-model="info.userSex" label=1>男</el-radio>
        <el-radio v-model="info.userSex" label=0>女</el-radio>
        <p>用户的口味偏好：</p>
        <input type="text" v-model="info.userPrefer" />
        <button @click="updateUserInfo">确认修改信息</button>
      </el-tab-pane>
      <el-tab-pane label="修改密码" name="myPassword">
        修改密码
        <p>原密码：</p>
        <input v-model="password.old_password" type="password" placeholder="请输入原密码" required/>
        <p>新密码：</p>
        <input v-model="password.password" type="password" placeholder="请输入新密码" required/>
        <p>确认密码：</p>
        <input v-model="confirmPassword" type="password" placeholder="请再次输入新密码" required/>
        <button @click="updateUserPassword">提交</button>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import {
  deleteUserActivity, deleteUserBlog,
  deleteUserDish, deleteUserLoveBlog,
  getUserActivity, getUserBlog,
  getUserDish, getUserLoveBlog,
  getUsersByID, updatePwd,
  updateUsers
} from "../../api/users";

export default {
  name: "userTools",
  data() {
    return {
      activeName: 'myDish',
      dishes: [{
        dishId: 999,
        dishName: '面包',
        dishSeller: '学一食堂xx窗口',
        dishPrice: 9.8,
        dishStars: 1.2,
        dishPicture: '../../../static/images/dish.png',
        dishFollowerCnt: 0,
      }],
      info: {
        userId: 0,
        username: 'HangFood',
        userPassword: '',
        email: '',
        userSignature: 'I love buaa food!',
        userSex: 1,
        userGrade: '大一',
        userPortrait: '../../../static/images/userPortrait.png',
        userPrefer: '食物',
      },
      password: {
        username: '',
        old_password: '',
        password: '',
      },
      confirmPassword: '',
      activities: [{
        activityId: 999,
        activityName: '光盘行动',
        activityBrief: '让我们一起光盘吧',
        activityBegin: '2022.11.30',
        activityEnd: '2022.12.30',
        activityOrganizerName: '学一食堂',
        activityOrganizerId: 999,
        activityHeadPhoto: '../../../static/images/poster.png',
        activityContent: '坚持40天光盘行动并将打卡发送到xxx，凭借打卡记录到学六食堂领取奖品，一等奖xxx,二等将xxx。',
        activityPerson: '',
        activityPersonCnt: 0,
      }],
      options: ["大一","大二","大三","大四","研一","研二","博士","教师"],
      blogs: [{
        blogId: 999,
        blogLabel: 'xxx',
        blogTitle: '一个blog',
        blogPicture: '../../../static/images/blogImage.png',
        blogPosterName: '用户名',
        blogFavoriterCnt: 0,
        blogLikeCnt: 0,
      }],
      loveBlogs: [{
        blogId: 999,
        blogLabel: 'xxx',
        blogTitle: '一个blog',
        blogPicture: '../../../static/images/blogImage.png',
        blogPosterName: '用户名',
        blogFavoriterCnt: 0,
        blogLikeCnt: 0,
      }],
      fileList: [],
      disabled: false,
      avatar_img: null,
    };
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    },
    handleRemove(file, fileList) {
			this.fileList = fileList.slice(-3);
			console.log(file, fileList);
		},
		handlePictureCardPreview(file) {
			console.log(file.raw);
			this.avatar_img = file.raw;
		},
		handleUpload(file) {
			this.avatar_img = file.raw;
			console.log(file);
    },
    getDishData() {
      getUserDish().then((response) => {
          //console.log(response.data);
          this.dishes = response.data;
          console.log("userDishes: " + JSON.stringify(this.dishes));
        })
        .catch(function (error) {
          console.log(error);
        });
      console.log(this.dishes);
    },
    getActivityData() {
      getUserActivity().then((response) => {
          //console.log(response.data);
          this.activities = response.data;
          console.log("userInfo: " + JSON.stringify(this.activities));
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    getUserBlogData() {
      getUserBlog().then((response) => {
          //console.log(response.data);
          this.blogs = response.data;
          console.log("userBlog: " + JSON.stringify(this.blogs));
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    getUserLoveBlogData() {
      getUserLoveBlog().then((response) => {
          //console.log(response.data);
          this.loveBlogs = response.data;
          console.log("userInfo: " + JSON.stringify(this.loveBlogs));
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    getUserData() {
      getUsersByID().then((response) => {
          //console.log(response.data);
          this.info = response.data;
          console.log("userInfo: " + JSON.stringify(this.info));
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    deleteDish(id) {
      this.dishes = this.dishes.filter(function (item) {
          return item.dishId !== id;
        });
      deleteUserDish(id).then((response) => {
        this.dishes = this.dishes.filter(function (item) {
          return item.dishId !== id;
        });
      }).catch(function (error){
        alert("删除失败");
        console.log(error)
      })
    },
    deleteActivity(id) {
      deleteUserActivity(id).then((response) => {
        this.activities = this.activities.filter(function (item) {
          return item.activityId !== id;
        });
      }).catch(function (error){
        alert("删除失败");
        console.log(error)
      })
    },
    deleteBlog(id) {
      deleteUserBlog(id).then((response) => {
        this.blogs = this.blogs.filter(function (item) {
          return item.blogId !== id;
        });
      }).catch(function (error){
        alert("删除失败");
        console.log(error)
      })
    },
    deleteLoveBlog(id) {
      deleteUserLoveBlog(id).then((response) => {
        this.loveBlogs = this.loveBlogs.filter(function (item) {
          return item.blogId !== id;
        });
      }).catch(function (error){
        alert("删除失败");
        console.log(error)
      })
    },
    updateUserInfo() {
      let param = new FormData();  // 创建form对象
      param.append("username", this.info.userName);
      param.append("email", this.info.userEmail);
      param.append("userSignature", this.info.userSignature);
      param.append("userSex", this.info.userSex);
      param.append("userGrade", this.info.userGrade);
      param.append("userPrefer", this.info.userPrefer);
      param.append("userPortrait", this.avatar_img);
      updateUsers(param).then((response)=>{
        alert('修改成功');
        this.$router.go(0);  // 刷新界面
      }).catch(function(error) {
        alert('修改失败');
        console.log(JSON.stringify(error));
      })
    },
    updateUserPassword() {
      this.password.username = this.$store.getters.userinfo.username;
      updatePwd(this.password).then((response)=>{
        alert('修改成功');
      }).catch(function(error) {
        alert('修改失败');
        console.log(JSON.stringify(error));
      })
    }
  },
  created() {
    this.getDishData();
    this.getActivityData();
    this.getUserData();
    this.getUserBlogData();
    this.getUserLoveBlogData();
  }
}
</script>

<style scoped>

</style>
