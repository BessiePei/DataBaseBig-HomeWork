import request from '@/utils/request'
// 封装请求的方式

// 获取轮播内容
export function getSlide() {
  return request({
    url: '/slider/',
    method: 'get',
  })
}

export function getActivityById(id) {
  return request({
    url: '/activity/' + id + '/',
    method: 'get',
  })
}

export function joinIn(id, data) {
  return request({
    url: '/activity/' + id + '/join/',
    method: 'post',
    data
  })
}

export function getActivityRemark(id) {
  return request({
    url: '/activity/' + id + '/remark/',
    method: 'get',
  })
}

export function postActivityRemark(id, data) {
  return request({
    url: '/activity/' + id + '/remark/',
    method: 'post',
    data
  })
}

