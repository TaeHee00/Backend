from django.urls import is_valid_path
from .models import Docs, User
from .serializer import DocsSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# from django.shortcuts import get_object_or_404, get_list_or_404


@api_view(['POST'])
def docs_create(request):

    if request.method == 'POST':
        request.data['user_id'] = User.objects.filter(id=1).first().id
        request.data['title'] = 'Default Title'
        request.data['content'] = 'Default Content'
        request.data['language'] = 'Default Language'

        serializer = DocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
