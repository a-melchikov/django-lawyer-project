from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("", ArticleListView.as_view(), name="article_list"),
]
