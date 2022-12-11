<template>
	<div class="footer">
		<!--<el-divider><i class="el-icon-more"></i></el-divider>-->
		<p class="text">© 2022 版权所有</p>
		<el-button class="el-button1" @click="dialogVisible = true">我要反馈</el-button>
		<el-dialog title="我要反馈" :visible.sync="dialogVisible" width="30%" :before-close="handleClose" append-to-body>
			<el-input type="textarea" placeholder="请输入内容" v-model="textarea" maxlength="30" show-word-limit>
			</el-input>
			<div slot="footer" class="dialog-footer">
				<c-theme-provider>
				<c-button :isLoading="btnloading"
					loading-text="Submitting"
					variant-color="blue"
					variant="solid"
					color="white !important" @click="submit()">提交</c-button>
				</c-theme-provider>
			</div>
		</el-dialog>
	</div>
</template>

<script>
	import { CThemeProvider,CButton } from '@chakra-ui/vue';
  import { submitFeedBack } from "../../api/users";

  export default {
		name: "footer",
		components: {
			CThemeProvider,CButton
		},
		data() {
			return {
				textarea: "",
				dialogVisible: false,
				btnloading: false
			};
		},
		methods: {
			handleClose(done) {
				done();
			},
			submit() {
				this.btnloading = true;
				let value = {
					category: 2,
					content: this.textarea
				};
				submitFeedBack(value).then((res) => {
					this.$message({
						message: "提交成功",
						type: "success",
					});
					this.btnloading = false;
					this.dialogVisible = false;
				}).catch ((err) => {
					console.log(err);
					this.$message({
						message: "提交失败" + err,
						type: "error",
					});
					this.btnloading = false;
				});

			},
		},
	}
</script>

<style scoped>
	.footer {
    display: block;
    margin-top: 15px;
		left: 0px;
    /* bottom: 0px;
    position: absolute;*/
		width: 100%;
		height: 36px;
		opacity: 1;
		background:  rgba(245, 245, 245, 1);
		overflow: hidden;
		padding: 0 4px;
		z-index: 3;
	}
	.text {
		display: inline;
		line-height: 36px;
		opacity: 1;
/** copyright */
		font-size: 14px;
		letter-spacing: 0px;
		color: rgba(166, 166, 166, 1);
		text-align: left;
		vertical-align: top;
	}

	.el-button1 {
		display: inline;
		position: absolute;
		right: 0;
		line-height: 36px;
		height: 36px;
		width: 100px;
		padding: 0;
		opacity: 1;
		/*background: white;*/
/** 我要反馈 */
		font-size: 16px;
		font-weight: 400;
		letter-spacing: 0px;
		color: rgba(128, 128, 128, 1);
		text-align: center;
		vertical-align: middle;
	}

	.el-button1:hover {
		background-color: rgba(224,224,224,1);
	}
</style>
