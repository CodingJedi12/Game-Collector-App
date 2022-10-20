from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index' ),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/played_on/', views.played_on, name='played_on'),
    path('systems/', views.SystemList.as_view(), name='systems_index'),
    path('systems/<int:pk>/', views.SystemDetail.as_view(), name='systems_detail'),
    path('systems/create/', views.SystemCreate.as_view(), name='systems_create'),
    path('systems/<int:pk>/update/', views.SystemUpdate.as_view(), name='systems_update'),
    path('systems/<int:pk>/delete/', views.SystemDelete.as_view(), name='systems_delete'),
    path('games/<int:game_id>/assoc_system/<int:system_id>/', views.assoc_system, name='assoc_system'),
]