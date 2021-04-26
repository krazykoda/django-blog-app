from django.urls import path
from .views import blog_index, blog_detail, create

urlpatterns = [
	path('', blog_index, name="blog"),
	path('<int:pk>', blog_detail, name="detail" ),
	path('create', create, name="create")
]
