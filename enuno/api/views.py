from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import CorpSerializer, CustomTokenObtainPairSerializer
from .models import Corp


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CorpView(viewsets.ModelViewSet):
    serializer_class = CorpSerializer
    queryset = Corp.objects.all()
