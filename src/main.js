// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// 引入路由，回去寻找router目录下的配置文件index.js
import router from './router'
import store from './vuex/store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import Chakra, { CThemeProvider, CColorModeProvider, CReset } from '@chakra-ui/vue'
// 关闭生产模式下的提示
Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(Chakra);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  // 在框架中使用路由功能
  router,
  store,
  components: { App },
  template: '<App/>',
  render: (h) => h(CColorModeProvider, [
    h(CThemeProvider, [
      h(CReset),
      h(App)
    ])
  ])
}).$mount()
