import request from '@/utils/request'
// 封装请求的方式
export function login(data) {
  return request({
    url: '/login/',
    method: 'post',
    data
  })
}

export function reg(data) {
  return request({
    url: '/users/',
    method: 'post',
    data
  })
}

export function getUsersByID() {
  return request({
    url: '/users/1/',
    method: 'get',
  })
}

export function updateUsers(data) {
  return request({
    url: '/users/1/',
    method: 'patch',
    data
  })
}

export function updatePwd(data) {
  return request({
    url: '/users/1/',
    method: 'patch',
    data
  })
}


/* 对于/1/后端需要获取当前登录用户信息进行修改，如果实现不了也可以让前端传id */

export function submitFeedBack(data) {
  return request({
    url: '/feedback/',
    method: 'post',
    data
  })
}
