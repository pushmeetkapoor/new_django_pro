from django.shortcuts import render
from stacked_economizer.models import StackedEconomizer
from stacked_economizer.serializers import StackedEconomizerSerializer
# from clients.serializers import UserSerializer
from django.contrib.auth.models import User

from clients.permissions import IsOwnerOrReadOnly

from rest_framework import filters, generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

import django_filters

class StackedEconomizerFilter(django_filters.FilterSet):
    class Meta:
        model = StackedEconomizer
        fields = ['client']

# Create your views here.
class StackedEconomizerViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        filter_backends = (filters.DjangoFilterBackend,)
        filter_class = StackedEconomizerFilter
        queryset = StackedEconomizer.objects.all()
        serializer_class = StackedEconomizerSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerOrReadOnly)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
