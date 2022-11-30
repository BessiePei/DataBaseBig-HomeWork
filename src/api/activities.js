import request from '@/utils/request'
// 封装请求的方式

// 获取轮播内容
export function getSlide() {
  return request({
    url: '/slider/',
    methods: 'get',
  })
}

export function getActivityById(id) {
  return request({
    url: '/activity/' + id + '/',
    method: 'get',
  })
}
