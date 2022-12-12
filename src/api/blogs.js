import request from '@/utils/request'
// 封装请求的方式

// 获取逛逛页面的blog
export function getVisitBlogs() {
  return request({
    url: '/visitorblogs/',
    method: 'get',
  })
}

export function getBlogByID(id) {
  return request({
    url: '/blog/' + id + '/',
    method: 'get',
  })
}

export function sendBlog(data) {
  return request({
    url: '/blog/',
    method: 'post',
    data
  })
}

export function getBlogRemark(id) {
  return request({
    url: '/blog/' + id + '/remark/',
    method: 'get',
  })
}

export function postBlogRemark(id, data) {
  return request({
    url: '/blog/' + id + '/remark/',
    method: 'post',
    data
  })
}

export function favoriteBlog(id, data) {
  return request({
    url: '/blog/' + id + '/favorite/',
    method: 'post',
    data
  })
}
