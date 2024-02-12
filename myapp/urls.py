from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    # path('home/', views.logout_view, name='logout'),
    path('registration/', views.registration, name='login'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('private/', views.user_in, name='private'),
    path('edit/<int:pk>', views.edit_recipe, name='edit'),
    path('all_recipes/', views.all_recipes, name='all'),
    path('full/<int:pk>', views.full_recipe, name='full'),
    path('my_recipes', views.user_in, name='my')
]