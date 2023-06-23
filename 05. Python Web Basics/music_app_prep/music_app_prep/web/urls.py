from django.urls import path

from music_app_prep.web import views

urlpatterns = [
    path('', views.index, name='home page'),
    path('album/add/', views.add_album, name='add album page'),
    path('album/details/<int:pk>/', views.album_details, name='album details page'),
    path('album/edit/<int:pk>/', views.edit_album, name='edit album page'),
    path('album/delete/<int:pk>', views.delete_album, name='delete album page'),
    path('profile/details/', views.profile_details, name='profile details page'),
    path('profile/delete/', views.delete_profile, name='delete profile page'),
]
