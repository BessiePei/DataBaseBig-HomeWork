import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/reg',
      name: 'reg',
      component: () => import('@/views/user/reg'),
      meta: {
        title: "用户注册"
      }
    }
  ]
})
