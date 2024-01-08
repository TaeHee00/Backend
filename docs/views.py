from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Docs
from .serializers import Serializer
class DocsList(APIView):
    def get(self, request): # 문서 내역 목록 조회
        docs = Docs.objects.filter(is_deleted=False)  # is_deleted가 False인 객체만 조회
        serializer = Serializer(docs, many=True)
        return Response(serializer.data)

