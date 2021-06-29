from .models import News
from rest_framework import generics, permissions
from . import serializers


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [permissions.IsAuthenticated]