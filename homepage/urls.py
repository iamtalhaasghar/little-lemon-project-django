from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name=""),
    path("menu/", views.MenuItemListView.as_view(), name=""),
    path("menu/<int:pk>", views.MenuItemDetailView.as_view(), name=""),
]
