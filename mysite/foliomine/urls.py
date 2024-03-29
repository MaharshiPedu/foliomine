from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_profile', views.create_profile, name='create_profile'),
    path('<int:profile_id>', views.displayProfile, name='display_profile'),
    path('edit/<int:profile_id>', views.edit_profile, name='edit_profile'),
    path('delete/<int:profile_id>', views.delete_profile, name='delete_profile')
]