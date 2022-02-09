from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/profile
    path('profile', views.UserPostsView.as_view(), name='profile'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('likepost', views.LikePost, name="like")
 
]