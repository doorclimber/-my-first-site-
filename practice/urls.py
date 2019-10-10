from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.getAccountInfo, name='name'),
    path('thanks/', views.thanks, name='thanks'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.lout, name='logout'),
    path('follow/', views.followUsers, name='follow'),
    path('reviews/', views.reviews, name='reviews'),
    path('pleaselogin/', views.pleaselogin, name='pleaselogin'),

    path('reviews/ridgefieldlibrary/', views.ridgefieldlibrary, name='ridgefieldlibrary'),
]
