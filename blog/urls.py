from django.urls import path
from . import views
from blog.apps import BlogConfig
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

app_name = BlogConfig.name


urlpatterns = [
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    # path('contacts/', ContactsListView.as_view(), name='contacts'),
]


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('contacts/', views.contacts, name='contacts'),
#     path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
# ]