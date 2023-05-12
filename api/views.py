from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Picture
from .serializers import PictureSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/picture/',
		'Detail View':'/picture/<str:pk>/',
		'Create':'/picture-create/',
		'Update':'/picture-update/<str:pk>/',
		'Delete':'/picture-delete/<str:pk>/',
    }
    return Response(api_urls)


#list picture
@api_view(['GET'])
def getPicture(request):
    search_query = request.GET.get('search', '')
    # print(search_query)
    if search_query:
        pictures = Picture.objects.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    else:
        pictures = Picture.objects.all()
    
    serializer = PictureSerializer(pictures, many=True)
    return Response(serializer.data)

#view picture
@api_view(['GET'])
def viewPicture(request,pk):
    picture=Picture.objects.get(id=pk)
    serializer=PictureSerializer(picture,many=False)
    return Response(serializer.data)

#create picture
@api_view(['POST'])
def createPicture(request):
    print(request.data)
    serializer=PictureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('success')
    else:
        return Response(serializer.error_messages)    
    

#update picture
@api_view(['POST'])
def updatePicture(request,pk):
    picture=Picture.objects.get(id=pk)
    serializer=PictureSerializer(instance=picture,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response(serializer.error_messages)   


#delete picture
@api_view(['DELETE'])
def deletePicture(request,pk):
    picture=Picture.objects.get(id=pk)
    picture.delete()
    return Response('Picture succesfully delete!')



