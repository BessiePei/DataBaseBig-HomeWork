import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  count: 10,
  /* imgUrl: "", */
  imgUrl: "http://localhost:8000/",
  userinfo: localStorage["userinfo"]?
    JSON.parse(localStorage["userinfo"]):null,
}

/* 同步处理 */
const mutations = {
  saveUser(state, value) {
    state.userinfo = value;
    localStorage.setItem('userinfo', value)
  },
  delUser(state) {
    console.log(" start delUser");
    state.userinfo = null;
    localStorage.clear(); // 清除本地缓存
    // 清除全部cookie
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie =
          name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
      }
      if (cookies.length > 0) {
        for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i];
          var eqPos = cookie.indexOf("=");
          var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
          var domain = location.host.substr(location.host.indexOf("."));
          document.cookie =
            name +
            "=;expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=" +
            domain;
        }
      }
  },
}

/* 异步处理 */
const actions = {
  saveUser(context, value) {
    return context.commit('saveUser',value)
  },
  delUser(context) {
    return context.commit('delUser')
  },
}

const getters = {
  userinfo(state) {
    localStorage.setItem("userinfo", JSON.stringify(state.userinfo));
    return state.userinfo;
  },
  imgUrl(state) {
    return state.imgUrl;
  }

}

const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})

// store对象导出
export default store
