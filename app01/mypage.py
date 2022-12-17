from rest_framework.pagination import PageNumberPagination


class MyPage(PageNumberPagination):
    page_size = 1  # 每页显示的数量
    max_page_size = 5  # 最多能设置的每页显示数量
    page_size_query_param = 'size'  # 每页显示数量的参数名称
    page_query_description = 'page'  # 页码的参数名称
