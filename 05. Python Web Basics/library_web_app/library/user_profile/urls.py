from django.urls import path, include

from library.user_profile import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile/', include([
        path('', views.profile_page, name='profile_page'),
        path('edit/', views.edit_profile, name='edit_profile'),
        path('delete/', views.delete_profile, name='delete_profile'),
    ])),
]
