# dbfrontend

> A Vue.js Project for DataBase Big Homework.

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

# 说明

最初版：mainPages v0只有基础属性展示，不涉及关联关系，没有写弹窗（表单提交），没有进行设计美化，页面所缺功能已在相应界面标注

## 页面功能新增说明



- [x] 首页：通过返回值isMerchant判断是否是商家，商家个人主页直接进入商家主页

- [x] 登录/注册

- [x] 开店

- [x] 个人主页：我的菜品、我的活动、我发布的帖子、我收藏的帖子、修改个人信息、修改密码（前四项都可以删除）

- [x] 搜索结果：==后端要返回什么样的结果？==只查找菜品

- [x] 活动界面：参加活动按钮（用户加入我的活动列表，商家加入商家参与活动列表，公用按钮传了userinfo）

- [x] 逛逛：发帖按钮+弹窗

- [x] 窗口主页：发布活动、发布菜品、活动列表（删除按钮仅对对商家显示）、菜品列表（删除按钮仅对对商家显示）

- [ ] ~~食堂主页：食堂下属窗口列表~~<font color='red'>设计不出入口先不要了</font>

- [x] 菜品主页：收藏按钮、发布评论、显示评论（仅自己可以删除）

- [x] 帖子主页：收藏按钮、发布评论、显示评论（仅自己可以删除）

  

## 页面组件设计

- [x] header 返回首页加了一个popover
- [x] 评论组件remark 参数source【String], id[number]主要用于区分获取不同的数据
- [x] 收藏按钮组件favoriteButton:参数source【String], id[number]主要用于区分获取不同的数据
- [x] 活动显示组件slider
- [x] 菜品显示组件hotDishes
- [x] header设计
- [x] footer
- [x] mainPage=slider+hotDishes+merchantList+userShow已完成
- [x] reg=login/signUp
- [x] openShopPage
- [ ] 评论remark
- [ ] 活动主页
- [ ] 菜品主页
- [ ] 帖子主页
- [ ] 商家主页
- [ ] 逛逛
- [x] 搜索结果界面：实现分页/筛选/排序
- [ ] 个人主页
