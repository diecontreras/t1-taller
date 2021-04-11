from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('breaking_bad/<int:id>/', views.breaking_bad, name='breaking_bad'),
    path('better_call_saul/<int:id>/', views.better_call_saul, name='better_call_saul'),

    path('episode/<int:id>/', views.episode, name='episode'),
    path('character/<str:name>/', views.character, name='character'),

    path('searchs/', views.search, name='search'),

]
