<template>
  <div class="vpage">
    <myheader></myheader>
    <h1>逛逛主页</h1>
    <button @click="dialogFormVisible = true">发帖<i class="el-icon-s-promotion"/></button>
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
    <el-dialog title="发帖" :visible.sync="dialogFormVisible" :before-close="handleClose" center>
      <el-form>
        <el-form-item label="帖子标题" required>
          <el-input v-model="form.title" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="帖子标签" required>
          <el-select v-model="form.label" placeholder="请选择帖子相关标签">
            <el-option
              v-for="item in options"
              :key="item"
              :label="item"
              :value="item">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="帖子图片" required>
          <el-upload action="https://jsonplaceholder.typicode.com/posts/" :limit="1" list-type="picture-card" :auto-upload="false"
					:on-change='handleUpload' :on-preview="handlePictureCardPreview" :on-remove="handleRemove" :file-list="fileList">
					<i slot="default" class="el-icon-plus"></i>
          <template #tip>
            <div class="el-upload__tip">只能上传一张图片。</div>
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
        </el-form-item>
        <el-form-item label="帖子内容" required>
          <el-input
            type="textarea"
            :rows="3"
            placeholder="请输入内容"
            v-model="form.content">
          </el-input>
        </el-form-item>
        <el-form-item label="帖子可见性" required>
          <el-radio v-model="form.private" label=false>公开</el-radio>
          <el-radio v-model="form.private" label=true>仅自己可见</el-radio>
        </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="dialogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="submitForm">确认发布</el-button>
    </div>
    </el-dialog>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import { getVisitBlogs } from "@/api/blogs";
import {sendBlog} from "../../api/blogs";
import {mapGetters} from "vuex";
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
      dialogFormVisible:false,
      form: {
        content: '',
        title: '',
        label: '',
        private: false,
        picture: null,
      },
      options: ['菜肴分享','美食地点分享','日常分享','其他'],
      disabled: false,
      fileList: [],
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
    },
    handleClose() {
      this.dialogFormVisible = false;
    },
    submitForm() {
      let param = new FormData(); // 创建form对象
      param.append("blogLabel", this.form.label);
      param.append("blogTitle", this.form.title);
      param.append("blogContent", this.form.content);
      param.append("blogPicture", this.form.picture);
      if (this.userinfo) {
        param.append("blogPosterName", this.userinfo.username);
        console.log(param);
        this.$router.go(0);
        sendBlog(param).then((response)=>{
          alert('修改成功');
          this.$router.go(0);
        }).catch(function(error) {
          alert('修改失败');
          console.log(JSON.stringify(error));
        })
      } else {
        alert('您尚未登录，请先登录后再来发帖！');
      }
      this.dialogFormVisible = false;
    },
    handleRemove(file, fileList) {
			this.fileList = fileList.slice(-3);
			console.log(file, fileList);
		},
		handlePictureCardPreview(file) {
			console.log(file.raw);
			this.form.picture = file.raw;
		},
		handleUpload(file) {
			this.form.private = file.raw;
			console.log(file);
    },
  },
  created() {
    this.getData();
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
  .vpage {
    margin-top: 10vh;
  }
</style>
