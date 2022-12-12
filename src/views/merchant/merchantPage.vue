<template>
  <div class="vpage">
    <myheader></myheader>
    <h1>窗口主页</h1>
    <img :src="info.merchantPortrait"/>
    <p>商家名：{{info.merchantName}}</p>
    <p>商家电话： {{info.merchantPhone}}</p>
    <p>商家评分： {{info.merchantStars}}</p>
    <p>营业时间： {{info.merchantOpen}}~{{info.merchantClose}}</p>
    <p>商家地址： {{info.merchantAddr}}</p>
    <button v-show="isMerchant" @click="dialogDishVisible=true">发布菜品</button>
    <button v-show="isMerchant" @click="dialogActivityVisible=true">发布活动</button>
    <h1>窗口活动</h1>
    <slider :id="id"></slider>
    <h1>窗口菜品</h1>
    <hot-dishes :id="id"></hot-dishes>
    <myfooter></myfooter>
    <!-- 发布活动弹窗 -->
    <el-dialog title="发布活动" :visible.sync="dialogActivityVisible" :before-close="handleClose" center>
      <el-form>
        <el-form-item label="活动标题" required>
          <el-input v-model="activity.activityName" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="活动简介" required>
          <el-input v-model="activity.activityBrief" placeholder="放在网站首页的简介" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="活动图片" required>
          <el-upload action="https://jsonplaceholder.typicode.com/posts/" :limit="1" list-type="picture-card" :auto-upload="false"
					:on-change='handleUpload' :on-preview="handlePictureCardPreview" :on-remove="handleRemove" :file-list="fileList">
					<i slot="default" class="el-icon-plus"></i>
          <template #tip>
            <div class="el-upload__tip">只能上传一张图片。请上传活动海报。</div>
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
        <el-form-item label="活动内容" required>
          <el-input
            type="textarea"
            :rows="3"
            placeholder="请输入活动详细信息，包括参与方式，活动奖励等。"
            v-model="activity.activityContent">
          </el-input>
        </el-form-item>
        <el-form-item label="活动开始时间" required>
          <el-input v-model="activity.activityBegin"></el-input>
        </el-form-item>
        <el-form-item label="活动结束时间" required>
          <el-input v-model="activity.activityEnd"></el-input>
        </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="dialogActivityVisible = false">取 消</el-button>
      <el-button type="primary" @click="submitActivityForm">确认发布</el-button>
    </div>
    </el-dialog>

    <!-- 发布菜品弹窗 -->
    <el-dialog title="发布菜品" :visible.sync="dialogDishVisible" :before-close="handleClose2" center>
      <el-form>
        <el-form-item label="菜品名" required>
          <el-input v-model="dish.dishName"></el-input>
        </el-form-item>
        <el-form-item label="菜品价格" required>
          <el-input v-model="dish.dishPrice" ></el-input>
        </el-form-item>
        <el-form-item label="菜品图片" required>
          <el-upload action="https://jsonplaceholder.typicode.com/posts/" :limit="1" list-type="picture-card" :auto-upload="false"
					:on-change='handleUpload2' :on-preview="handlePictureCardPreview" :on-remove="handleRemove" :file-list="fileList2">
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
							<span v-if="!disabled" class="el-upload-list__item-delete" @click="handleRemove(file, fileList2)">
								<i class="el-icon-delete"></i>
							</span>
						</span>
          </div>
          </el-upload>
        </el-form-item>
        <el-form-item label="菜品简介" required>
          <el-input
            type="textarea"
            :rows="3"
            placeholder="请输入内容，一百字以内。"
            v-model="dish.dishBrief">
          </el-input>
        </el-form-item>
        <el-form-item label="菜品口味" >
          <el-input type="text" v-model="dish.dishTaste"></el-input>
        </el-form-item>
        <el-form-item label="菜品原料">
          <el-input type="text" v-model="dish.dishRaw"></el-input>
        </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="dialogDishVisible = false">取 消</el-button>
      <el-button type="primary" @click="submitForm2">确认发布</el-button>
    </div>
    </el-dialog>
  </div>
</template>

<script>
import myheader from "./../app/header";
import myfooter from "./../app/footer";
import { getMerChantByID } from "@/api/merchants";
import FavoriteButton from "../app/favoriteButton";
import slider from "./../index/slider";
import hotDishes from './../index/hotDishes'
import {postActivity, postDish} from "../../api/merchants";

export default {
  name: "merchantPage",
  components: {
    FavoriteButton,
    myheader,
    myfooter,
    slider,
    hotDishes
  },
  data() {
    return {
      id: -1,
      info: {
        merchantName: '学一食堂xx窗口',
        merchantPortrait: '../../../static/images/userPortrait.png',
        merchantPhone: '123456789',
        merchantStars: 5.0,
        merchantAddr: '和一楼四楼清真食堂左手第一个窗口',
        merchantOpen: '9:00',
        merchantClose: '19:00',
        merchantFollowerCnt: 0,
      },
      isMerchant: true,
      dialogActivityVisible: false,
      dialogDishVisible: false,
      activity: {
        activityName: '',
        activityBrief: '',
        activityBegin: '',
        activityEnd: '',
        activityHeadPhoto: null,
        activityContent: '',
      },
      fileList: [],
      dish: {
        dishName: '',
        dishPrice: 0,
        dishPicture: null,
        dishRaw: '',
        dishBrief: '',
        dishTaste: '',
      },
      fileList2: [],
      disabled: false,
    }
  },
  methods: {
    getData() {
      console.log(this.$route.params.id);
      this.id = this.$route.params.id;
      if (this.$route.params.id) {
        getMerChantByID(this.$route.params.id).then((response) => {
          this.info=response.data.data;
        }).catch (function(error){
          console.log(error);
        })
      }
    },
    handleClose() {
      this.dialogActivityVisible = false;
    },
    handleClose2() {
      this.dialogDishVisible =false;
    },
    submitForm1() {
      let param = new FormData(); // 创建form对象
      param.append("activityName", this.activity.activityName);
      param.append("activityBrief", this.activity.activityBrief);
      param.append("activityContent", this.activity.activityContent);
      param.append("activityHeadPhoto", this.activity.activityHeadPhoto);
      param.append("activityBegin", this.activity.activityBegin);
      param.append("activityEnd", this.activity.activityEnd);
      if (this.userinfo) {
        param.append("activityOrganizer", this.userinfo.username);
        console.log(param);
        postActivity(param).then((response)=>{
          alert('提交成功');
          this.$router.go(0);
        }).catch(function(error) {
          alert('提交失败');
          console.log(JSON.stringify(error));
        })
      } else {
        // 逻辑上用不到
        alert('您尚未登录，请先登录后再来发布活动！');
      }
      this.dialogActivityVisible = false;
    },
    submitForm2() {
      let param = new FormData();  // 创建form对象
      param.append("dishName", this.dish.dishName);
      param.append("dishPrice", this.dish.dishPrice);
      param.append("dishPicture", this.dish.dishPicture);
      param.append("dishRaw", this.dish.dishRaw);
      param.append("dishTaste", this.dish.dishRaw);
      if (this.userinfo) {
        param.append("dishSeller", this.userinfo.username);
        console.log(param);
       postDish (param).then((response)=>{
          alert('提交成功');
          this.$router.go(0);
        }).catch(function(error) {
          alert('提交失败');
          console.log(JSON.stringify(error));
        })
      } else {
        // 逻辑上用不到
        alert('您尚未登录，请先登录后再来发布活动！');
      }
      this.dialogDishVisible = false;
    },
    handleRemove(file, fileList) {
			this.fileList = fileList.slice(-3);
			console.log(file, fileList);
		},
		handlePictureCardPreview(file) {
			console.log(file.raw);
			this.activity.activityHeadPhoto = file.raw;
		},
		handleUpload(file) {
			this.activity.activityHeadPhoto = file.raw;
			console.log(file);
    },
    handlePictureCardPreview2(file) {
			console.log(file.raw);
			this.dish.dishPicture = file.raw;
		},
		handleUpload2(file) {
			this.dish.dishPicture = file.raw;
			console.log(file);
    },
  },
  created() {
    if (this.$store.state.userinfo) {
      this.isMerchant = this.$store.state.userinfo.isMerchant;
    }
    this.getData();
  }
}
</script>

<style scoped>
  .vpage {
    margin-top: 10vh;
  }
</style>
