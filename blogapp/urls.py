from django.urls import path
from . import views
from .views import(
     PostListView, 
     PostDetailsView, 
     PostCreateView, 
     PostUpdateView,
     PostDeleteView,
     PostListUserView
)


urlpatterns = [
    # Why we are writing this name here as blog-home
    # it to clearify that we are talking about blog home not other apps home
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailsView.as_view(), name="post-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('post/user/<int:author>', PostListUserView.as_view(), name="post-delete"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('about/', views.about, name="blog-about")
]