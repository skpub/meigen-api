from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import HttpResponse

from .auth import (NormalAuthentication, JWTAuthentication)

from meigen_app.models import User

class Login(APIView):
    authentication_classes = [NormalAuthentication,]

    def post(self, request, *args, **kwargs):
        return Response({"token": request.user})

class MeigenAPI(APIView):
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get(self, request, *args, **kwargs):
        return Response({'data':  'test'})

def index(request):
    return HttpResponse("Hello")


def add_user(request):
    username = request._request.POST.get("username")
    password = request._request.POST.get("password")

    User.objects.create(name=username, hspw=password)
