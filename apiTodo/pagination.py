#from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class SmallPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "sayfa"


class LargePageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "sayfa"

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = "sayfadaki_eleman_sayisi"
    offset_query_param = "sayfanin_baslangic_elemani"

class MyCursorPagination(CursorPagination):
    ordering = "updateDate"
    #page_size = 10