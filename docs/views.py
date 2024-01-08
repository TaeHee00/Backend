from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Docs
from .serializers import Serializer
class DocsList(APIView):
    def get(self, request): # 문서 조회
        docs = Docs.objects.filter(is_deleted=False)  # is_deleted가 False인 객체만 조회
        serializer = Serializer(docs, many=True)
        return Response(serializer.data)

class DocsDetail(APIView): # Docs의 detail을 보여주는 역할
    def get_object(self, pk):  # Docs 객체 가져오기
        try:
            return Docs.objects.get(pk=pk, is_deleted=False)  # is_deleted가 False인 객체만 조회
        except Docs.DoesNotExist:
            raise Http404
    def get(self, request, pk): # 문서 상세 조회
        doc = self.get_object(pk)
        serializer = Serializer(doc)
        return Response(serializer.data)

