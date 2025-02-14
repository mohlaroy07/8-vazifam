from django.urls import path

from .views import home_page, detail_page, add_news, edit_news, delete_news

urlpatterns = [
    path("", home_page, name="home_page"),
    path("detail/<int:pk>/", detail_page, name="detail_page"),
    path("add-news/", add_news, name="add_news"),
    path("edit-news/<int:pk>/", edit_news, name="edit_news"),
    path("delete-news/<int:pk>/", delete_news, name="delete_news"),
]