from django.urls import re_path, path

from . import views

app_name = 'blog'

urlpatterns = [
    re_path('detail/(?P<slug>[\w-]+)$', views.BlogDetail.as_view(), name='detail_blog'),
    path('', views.BlogList.as_view(), name='bloglist')
]
