from rest_framework.pagination import PageNumberPagination
# Create your views here.
class myPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'mypage'