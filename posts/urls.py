from django.urls import re_path, path

from . import views

app_name = 'blog'

urlpatterns = [
    re_path('detail/(?P<slug>[\w\d-]+)$', views.BlogDetail.as_view(), name='detail_blog'),
    re_path('category/(?P<slug>[\w\d-]+)$', views.PostCategories.as_view(), name='category'),
    path('list-categories', views.ListCategories.as_view(), name='list_categories'),
    path('', views.BlogList.as_view(), name='bloglist')
]
