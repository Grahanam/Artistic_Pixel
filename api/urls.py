from django.urls import path 

from . import views
urlpatterns=[
    path('',views.apiOverview,name='api-overview'),
    path('getpicture/',views.getPicture,name='get-picture'),
    path('viewpicture/<str:pk>/',views.viewPicture,name='view-picture'),
    path('createpicture/',views.createPicture,name='create-picture'),
    path('updatepicture/<str:pk>/',views.updatePicture,name='update-picture'),
    path('deletepicture/<str:pk>/',views.deletePicture,name='delete-picture')
]