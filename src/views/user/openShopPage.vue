<template>
  <c-color-mode-provider>
  <c-theme-provider>

      <c-reset />
  <div class="openShopPage">
      <div class="content">
    <c-box>
			<c-heading text-align='center' as="h1" size="xl" mb="10px">
				快来注册开店吧！
			</c-heading>
      <p>请先填写以下信息，进行注册！</p>
		</c-box>
    <c-form-control :is-required="isRequired" w="500px" m="auto" :model="ruleForm" ref="ruleForm">
      <c-form-label mt="4px">窗口名</c-form-label>
      <c-input :isRequired="isRequired" v-model="ruleForm.username" placeholder="请输入注册窗口名"/>
      <c-form-label mt="4px">登录密码</c-form-label>
      <c-input :isRequired="isRequired"
          pr="4.5rem"
          :type="show ? 'text' : 'password'"
          placeholder="请输入登录密码"
          v-model="ruleForm.password"
      />
      <c-form-label mt="4px">联系电话</c-form-label>
      <c-input :isRequired="isRequired" v-model="ruleForm.phone" placeholder="请输入窗口联系电话"/>
      <c-form-label mt="4px">窗口地址</c-form-label>
      <c-input :isRequired="isRequired" v-model="ruleForm.addr" placeholder="请用文字描述窗口地址"/>
      <c-form-label mt="4px">营业开始时间</c-form-label>
      <c-input :isRequired="isRequired" v-model="ruleForm.openTime" placeholder="请输入窗口开始营业时间。例如：09:00"/>
      <c-form-label mt="4px">营业结束时间</c-form-label>
      <c-input :isRequired="isRequired" v-model="ruleForm.closeTime" placeholder="请输入窗口结束营业时间。例如：19:00"/>
      <c-form-label>窗口所属的食堂</c-form-label>
      <c-select :isRequired="isRequired" v-model="ruleForm.head" placeholder="请选择窗口所属的食堂" >
        <option v-for="item in options" :key="item" :label="item" :value="item" />
      </c-select>
      <c-form-label>窗口头像上传</c-form-label>
      <el-upload action="https://jsonplaceholder.typicode.com/posts/" :limit="1" list-type="picture-card" :auto-upload="false"
					:on-change='handleUpload' :on-preview="handlePictureCardPreview" :on-remove="handleRemove" :file-list="fileList">
					<i slot="default" class="el-icon-plus"></i>
          <template #tip>
            <div class="el-upload__tip">只能上传一张图片</div>
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
      <!-- 超过数目上传按钮隐藏，见https://blog.csdn.net/thingir/article/details/124802295 -->
    </c-form-control>
    <c-button-group mt="10px" :spacing="4">
      <router-link :to="{path: '/'}"><c-button>返回首页</c-button></router-link>
      <c-button variant-color="orange" @click="openDialog">注册窗口</c-button>
    </c-button-group>
        <c-alert-dialog
      :is-open="isOpen"
      :least-destructive-ref="$refs.cancelRef"
      :on-close="closeDialog"
    >
      <c-alert-dialog-overlay />
      <c-alert-dialog-content>
        <c-alert-dialog-header font-size="lg" font-weight="bold">
          提交注册信息
        </c-alert-dialog-header>
        <c-alert-dialog-body>
          您确定要提交注册信息吗？提交信息后不可以更改。
        </c-alert-dialog-body>
        <c-alert-dialog-footer>
          <c-button ref="cancelRef" @click="closeDialog">
            取消
          </c-button>
          <c-button variantColor="orange" @click="submit" ml="3">
            确认注册
          </c-button>
        </c-alert-dialog-footer>
      </c-alert-dialog-content>
    </c-alert-dialog>
    </div>
    <myfooter></myfooter>
  </div>

  </c-theme-provider>
  </c-color-mode-provider>
</template>

<script>
import {CThemeProvider,CReset,CColorModeProvider,CButton,
	CHeading,CText,CFlex,CLightMode,CFormControl,CFormLabel,CInput,CBox,CSelect,
  CInputRightElement,CInputGroup,CButtonGroup,
  CAlertDialog,
  CAlertDialogHeader,
  CAlertDialogBody,
  CAlertDialogFooter,
  CAlertDialogOverlay,
  CAlertDialogContent,
  CAlertDialogCloseButton
} from "@chakra-ui/vue"
import myfooter from "./../app/footer";
import {signUp} from "../../api/merchants";

export default {
  name: "openShop",
  components: {
    myfooter,
    CHeading,
    CThemeProvider,
	  CColorModeProvider,
	  CBox,
    CReset,
    CButton,
    CText,
    CFlex,
	  CLightMode,
	  CFormControl,CFormLabel,CInput,
    CSelect,
    CButtonGroup,
    CAlertDialog,
  CAlertDialogHeader,
  CAlertDialogBody,
  CAlertDialogFooter,
  CAlertDialogOverlay,
  CAlertDialogContent,
  CAlertDialogCloseButton
  },
  data() {
    return {
      isRequired: true,
      ruleForm: {
        username: '',
        password: '',
        phone: '',
        addr: '',
        openTime: '',
        closeTime: '',
        head: "",
        portrait: null
      },
      fileList:[],
      show: false,
      disabled: false,
      isOpen: false,
      options: ["学一食堂","学二食堂","学三食堂","学四食堂"]
    }
  },
  methods: {
      handleRemove(file, fileList) {
				this.fileList = fileList.slice(-3);
				console.log(file, fileList);
			},
			handlePictureCardPreview(file) {
				console.log(file.raw);
				this.ruleForm.portrait = file.raw;
			},
			handleUpload(file) {
				this.ruleForm.portrait = file.raw;
				console.log(file);
			},
      closeDialog() {
      this.isOpen = false
    },
    openDialog() {
      this.isOpen = true
    },
    submit() {
      var that = this;
      let param = new FormData();  // 创建form对象
      param.append("merchantName", this.ruleForm.username);
      param.append("merchantPassword", this.ruleForm.password);
      param.append("merchantPortrait", this.ruleForm.portrait);
      param.append("merchantPhone", this.ruleForm.phone);
      param.append("merchantAddr", this.ruleForm.addr);
      param.append("merchantOpen", this.ruleForm.openTime);
      param.append("merchantClose", this.ruleForm.closeTime);
      param.append("merchantHead", this.ruleForm.head);
      signUp(
        param
      )
        .then((Response) => {
          console.log(Response);
          if (Response.status === 201) {
            //保存数据到本地存储
            console.log(Response.data);
            /*
            //同时保存到vuex
            // this.saveUser(Response.data);
            // localStorage.setItem('user',{'token':Response.data.token,'id':Response.data.id,'username':Response.data.username});
            localStorage.setItem("minfo", Response.data);
            this.$store.dispatch("saveMerchant", Response.data);
            // console.log(this.$store.user.id);
            this.$router.push("/"); //跳转到首页
            */
            this.$router.push("/");
            alert('注册成功，请返回首页进行登录');
          }
        })
        .catch(function (error) {
          if ("username" in error) {
            that.err_username2 = error.username[0];
          } else if ("password" in error) {
            that.err_password2 = error.password[0];
          } else {
            alert("注册失败");
          }
        });
    }
  },
}
</script>

<style scoped>
  @import "../../../static/css/openShopPage.css";
</style>
