from django.urls import path 

from . import views 

app_name = 'dashboard'


urlpatterns = [
    path('', views.index_dashboard, name='dashboard_index'),
    path('add-blog', views.AddBlog.as_view(), name='add_blog'),
    path('logout', views.logout_user, name='logout'),
    path('edit-blog/<int:pk>', views.UpdateBLog.as_view(), name='edit_blog'),
    path('list-blog', views.ListsBlog.as_view(), name='lists_blog'),
    path('delete-blog/<int:pk>', views.DeleteBlog.as_view(), name='delete_blog'),
    path('<int:pk>/update-profile', views.Profile.as_view(), name='profile'),
    path('change-password', views.ChangePassword.as_view(), name='change_password'),
    path('upload-image', views.UploadImage.as_view(), name='upload_image'),
    path('list-images', views.ListImages.as_view(), name='list_images')
]