import request from '@/utils/request'
// 封装请求的方式

//首页获取热门菜品
export function getHotDishes() {
  return request({
    url: '/hotdishes/',
    method: 'get',
  })
}

export function getDishByID(id) {
  return request({
    url: '/dish/' + id + '/',
    method: 'get',
  })
}

export function getDishRemark(id) {
  return request({
    url: '/dish/' + id + '/remark/',
    method: 'get',
  })
}

export function postDishRemark(id, data) {
  return request({
    url: '/dish/' + id + '/remark/',
    method: 'post',
    data
  })
}

export function favoriteDish(id, data) {
  return request({
    url: '/dish/' + id + '/favorite/',
    method: 'post',
    data
  })
}

