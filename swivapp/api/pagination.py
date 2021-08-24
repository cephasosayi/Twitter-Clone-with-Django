from rest_framework import pagination


class StandardResultsPagination(pagination.PageNumberPagination):
	page_size =10
	page_size_query = 'page_size'
	max_page_size= 1000
