from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='csvcrud-home'),
    path('addpg/', views.addpg, name='csvcrud-addpg'),
    path('add/', views.add, name='csvcrud-add'),

    path('displaypg/', views.displaypg, name='csvcrud-displaypg'),
    path('display/', views.display, name='csvcrud-display'),

    path('displayallpg/', views.displayallpg, name='csvcrud-displayallpg'),

    path('exportcsv/', views.exportcsv, name='csvcrud-exportcsv'),
    path('download_file/', views.download_file, name='csvcrud-download_file')

]
