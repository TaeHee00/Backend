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
        request.data['title'] = "OPGC (Open Source Project's Github Contributions)"
        request.data['content'] = """## 프로젝트 소개

OPGC 프로젝트는 Github 프로필을 분석하여 사용자의 기여를 추적하고 랭킹을 매기는 서비스입니다.

### 기술스택

- Framework: Django REST framework
- Django, Django REST framework
- Django Filter
- Cacheops
- django-ckeditor, sentry-sdk

## 기능 소개

OPGC 프로젝트는 다음과 같은 기능을 제공합니다.

- 깃헙 유저 프로필 정보를 조회할 수 있는 기능
- 깃헙 유저의 조직, 저장소, 언어 정보를 조회할 수 있는 기능
- 깃헙 유저와 관련된 랭킹을 조회할 수 있는 기능
- 공지사항 관리를 위한 기능

## 핵심 기능

### 1. 깃헙 유저 프로필 조회

깃헙 유저의 프로필 정보를 조회할 수 있으며, 프로필에는 유저의 조직, 저장소, 언어 정보가 포함되어 있습니다. 또한, 유저의 프로필은 일정 주기로 업데이트되며, 프로필을 업데이트한 날짜를 기준으로 하루가 지나야지 다시 업데이트할 수 있는 로직이 있습니다.

### 2. 랭킹 조회

깃헙 유저들의 랭킹을 조회할 수 있는 기능이 제공됩니다. 또한, 특정 유형에 따라 랭킹을 필터링 할 수 있습니다. 랭킹 조회 시 사용자 수와 랭킹을 함께 제공합니다.

### 3. 공지사항 관리

관리자가 공지사항을 작성하고 조회할 수 있는 기능을 제공합니다. 공지사항은 제목과 내용을 포함하고 있습니다.

## 주요 기능

### GithubUserViewSet

깃헙 유저 프로필 정보를 조회하고 업데이트하는 기능을 담당합니다. `retrieve` 메서드를 통해 깃헙 유저의 프로필 정보를 조회하고, `update` 메서드를 통해 프로필 정보를 업데이트합니다. 또한, `can_update` 메서드를 통해 프로필을 업데이트할 수 있는 조건을 체크합니다. 마지막으로 `tag` 액션은 OPGC 프로필 svg tag를 반환하는 기능입니다.

### RankViewSet

랭킹을 조회하는 기능을 담당합니다. `list` 메서드를 통해 특정 유형에 따라 랭킹을 필터링하여 조회할 수 있습니다.

### NoticeViewSet

공지사항을 조회하는 기능을 담당합니다.

### UserViewSet

유저 정보를 조회하는 기능을 담당합니다. 특정 유저의 username을 기반으로 조회할 수 있습니다

### 기타 기능

그 외에도 조직, 저장소, 언어, 랭킹 등 관련된 정보를 조회하는 기능들이 모두 흩어져 있습니다.

## 프로젝트 구조

- apps
    - githubs: Github 사용자, 저장소, 언어 정보 모델 및 API
    - notices: 공지사항 모델 및 API
    - ranks: 랭킹 모델 및 API
    - reservations: 사용자 정보 업데이트 대기열 모델
    - users: 사용자 모델 및 API
- core: 공통 모듈 및 모델

각 앱은 자체적인 모델과 API를 구성하고 있으며, 기능별로 분리되어 관리되고 있습니다.

위와 같은 기능들은 Django REST framework를 사용하여 구현되었으며, 캐싱을 위해 cacheops를, 에러 로깅을 위해 sentry-sdk를 사용하고 있습니다. 또한, front-end와 연계하여 쉽게 사용할 수 있도록 API를 제공하고 있습니다."""
        request.data['language'] = 'KOR'

        serializer = DocsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.response(data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
