from django.urls import path
from . import views

urlpatterns =[
    path('docs/', views.DocsList.as_view()), # get - 문서 내역 조회
    path('docs/<int:pk>/', views.DocsDetail.as_view()), # get - 문서 상세 내역 조회
]