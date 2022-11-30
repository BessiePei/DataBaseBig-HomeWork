import request from '@/utils/request'
// 封装请求的方式

// 获取轮播内容
export function getHotMerChants() {
  return request({
    url: '/hotmerchants/',
    methods: 'get',
  })
}

export function getMerChantByID(id) {
  return request({
    url: '/merchant/' + id + '/',
    methods: 'get',
  })
}

export function getCanteenByID(id) {
  return request({
    url: '/canteen/' + id + '/',
    methods: 'get',
  })
}
