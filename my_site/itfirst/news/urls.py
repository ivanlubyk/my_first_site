from . import views
from django.urls import path

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.create, name='create'),  # Add a trailing slash for consistency
    path('<int:pk>/', views.NewsDetail.as_view(), name='news_detail'),  # Add a trailing slash for consistency
    path('<int:pk>/update/', views.NewsUpdate.as_view(), name='news_update'),  # Add a trailing slash for consistency
    path('<int:pk>/delete/', views.NewsDelete.as_view(), name='news_delete'),
]
