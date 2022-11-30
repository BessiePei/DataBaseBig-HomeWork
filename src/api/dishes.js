import request from '@/utils/request'
// 封装请求的方式

//首页获取热门菜品
export function getHotDishes() {
  return request({
    url: '/hotdishes/',
    methods: 'get',
  })
}

export function getDishByID(id) {
  return request({
    url: '/dish/' + id + '/',
    methods: 'get',
  })
}

