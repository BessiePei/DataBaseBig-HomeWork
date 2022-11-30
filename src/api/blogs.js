import request from '@/utils/request'
// 封装请求的方式

// 获取逛逛页面的blog
export function getVisitBlogs() {
  return request({
    url: '/visitorblogs/',
    methods: 'get',
  })
}

export function getBlogByID(id) {
  return request({
    url: '/blog/' + id + '/',
    methods: 'get',
  })
}

