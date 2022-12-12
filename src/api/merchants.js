import request from '@/utils/request'
// 封装请求的方式

// 获取轮播内容
export function getHotMerChants() {
  return request({
    url: '/hotmerchants/',
    method: 'get',
  })
}

export function getMerChantByID(id) {
  return request({
    url: '/merchant/' + id + '/',
    method: 'get',
  })
}

export function getCanteenByID(id) {
  return request({
    url: '/canteen/' + id + '/',
    method: 'get',
  })
}

export function signUp(data) {
  return request({
    url: '/merchants/',
    method: 'post',
    data, //上传图片的信息
    cache: false, //不必须不从缓存中读取
    processData: false,//必须处理数据 上传文件的时候，则不需要把其转换为字符串，因此要改成false
    contentType: false,//必须 发送数据的格式
  })
}

/* 图片上传参考 https://blog.csdn.net/m0_54625720/article/details/115265768  */


export function getMerchantActivities(id) {
  return request({
    url: '/merchant/' + id + '/activities/',
    method: 'get'
  })
}

export function getMerchantDishes(id) {
  return request({
    url: '/merchant/' + id + '/dishes/',
    method: 'get'
  })
}

export function deleteMerchantDish(id) {
  return request({
    url: '/merchant/1/dishes/' + id,
    method: 'delete'
  })
}

/* 只有登录的商家才能删除自己发布的菜品，请把1替换成登录的商家 */

export function deleteMerchantActivity(id) {
  return request({
    url: '/merchant/1/activities/' + id,
    method: 'delete'
  })
}

/* 说明同上一条 */

export function postDish(data) {
  return request({
    url: '/merchant/1/dishes',
    method: 'post',
    data
  })
}

export function postActivity(data) {
  return request({
    url: '/merchant/1/activities',
    method: 'post',
    data
  })
}
