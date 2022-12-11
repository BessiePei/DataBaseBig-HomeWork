<template>
  <div id="merchantList">
    <h1 class="title"> 热门商家 </h1>
    <div class="merchants">
      <el-card :body-style="{ padding: '0px' }" shadow="hover" v-for="merchant in lists" :key="merchant.merchantId">
        <router-link :to="{name: 'merchantPage', params: {id: merchant.merchantId}}">
          <div class="card-content">
            <div class="rank">{{merchant.merchantRank}}</div>
          <div class="mName">{{merchant.merchantName}}</div>
          </div>
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
  #merchantList {
    width: 20%;
    height: 2.2rem;
    box-shadow: 1px 1px #8c939d;
    border-radius: 20px 0;
    background-image: linear-gradient(90deg, var(--orange) 0%, var(--lightorange) 74%);
  }

  .title {
    font-size: 1.5rem;
  }

  .card-content {
    margin: 0;
    line-height: 10px;
    display: table;
  }

  .rank {
    float: left;
    background-image: linear-gradient(90deg, var(--orange) 0%, var(--lightorange) 74%);
    font-size: 1rem;
    font-weight: bold;
    color: white;
    margin: 5px;
    padding: 5px;
  }

  .mName {
    float: right;
    margin: 5px;
    padding: 5px;
  }
</style>
