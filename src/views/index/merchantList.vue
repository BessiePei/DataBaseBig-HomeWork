<template>
  <div id="merchantList">
    <h1> 热门商家 </h1>
    <div class="merchants">
      <el-card shadow="hover" v-for="merchant in lists" :key="merchant.merchantId">
        <router-link :to="{name: 'merchantPage', params: {id: merchant.merchantId}}">
          <p>商家排名：{{merchant.merchantRank}}</p>
          <p>商家名：{{merchant.merchantName}}</p>
        </router-link>
      </el-card>
    </div>
  </div>
</template>

<script>
import { getHotMerChants } from "@/api/merchants"
export default {
  name: "merchantList",
  components: {
    getHotMerChants
  },
  data() {
    return {
      lists: [{
        merchantId: 999,
        merchantName: '学一食堂xx窗口',
        merchantRank: '100',
      }],
    }
  },
  methods: {
    getData() {
      getHotMerChants()
        .then((response) => {
          //console.log(response.data);
          this.lists = response.data.data;
          console.log("hotMerChants: " + JSON.stringify(this.lists));
        })
        .catch(function (error) {
          console.log(error);
        });
      console.log(this.lists);
    },
  },
  created() {
    this.getData();
  },
}
</script>

<style scoped>

</style>
