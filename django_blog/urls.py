from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.shortcuts import render

def index_page(request):
    return render(request, 'main/index.html')

app_name = 'main'


urlpatterns = [
    path('', index_page, name='index_page'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls'), name='account'),
    path('blog/', include('posts.urls')),
    path('dashboard/', include('dashboard.urls'), name='dashboard'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)