from django.urls import path,include
from . import views
urlpatterns = [
    path('register/',views.UserFormView.as_view(),name="userform"),
    path('',views.genres_view.as_view(),name="genres"),
    path('<pk>/',views.details.as_view(),name="details"),
]