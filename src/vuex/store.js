import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  count: 10,
  userinfo: localStorage["userinfo"]?
    JSON.parse(localStorage["userinfo"]):[],
}

const mutations = {
  saveUser(state, value) {
    state.userinfo = value;
    localStorage.setItem('userinfo', value)
  },
  delUser(state) {
    state.userinfo = null;
  },
}

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
}

const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})

// store对象导出
export default store
