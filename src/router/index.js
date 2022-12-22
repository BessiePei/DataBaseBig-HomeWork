import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('@/views/index/index'),
      meta: {
        title: "首页"
      }
    },
    {
      path: '/helloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/reg',
      name: 'reg',
      component: () => import('@/views/user/reg'),
      meta: {
        title: "用户登录/注册"
      }
    },
    {
      path: '/openShopPage',
      name: 'openShopPage',
      component: () => import('@/views/user/openShopPage'),
      meta: {
        title: "开店界面"
      }
    },
    {
      path: '/search/:content',
      name: 'searchPage',
      component: () => import('@/views/search/searchPage'),
      meta: {
        title: "搜索结果"
      }
    },
    {
      path: '/activity/:id',
      name: 'activityPage',
      component: () => import('@/views/activity/activityPage'),
      meta: {
        title: "活动界面"
      }
    },
    {
      path: '/visit',
      name: 'visitPage',
      component: () => import('@/views/visit/visitPage'),
      meta: {
        title: "逛逛"
      }
    },
    {
      path: '/merchant/:id',
      name: 'merchantPage',
      component: () => import('@/views/merchant/merchantPage'),
      meta: {
        title: "窗口主页"
      }
    },
    {
      path: '/dish/:id',
      name: 'dishPage',
      component: () => import('@/views/dish/dishPage'),
      meta: {
        title: "菜品主页"
      }
    },
    {
      path: '/blog/:id',
      name: 'blogPage',
      component: () => import('@/views/visit/blogPage'),
      meta: {
        title: "帖子主页"
      }
    },
    {
      path: '/profile',
      name: 'personPage',
      component: () => import('@/views/user/personPage'),
      meta: {
        title: "个人主页"
      }
    }
  ]
})
