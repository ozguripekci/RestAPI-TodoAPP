#from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination

class SmallPageNumberPegination(PageNumberPagination):
    page_size = 1
    page_query_param = "sayfa"


class LargePageNumberPegination(PageNumberPagination):
    page_size = 4
    page_query_param = "sayfa"