from Resource.models import ResourceType, ResourceContent
from Resource.serializers import ResourceTypeSerializer, ResourceContentSerializer

from rest_framework import generics
from rest_framework.filters import SearchFilter

from Reference.Pagination import OwnPagination


class ResourceTypeList(generics.ListCreateAPIView):
    serializer_class = ResourceTypeSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'alias']
    queryset = ResourceType.objects.all()


class ResourceTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer


class ResourceContentList(generics.ListCreateAPIView):
    serializer_class = ResourceContentSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'filename']

    def get_queryset(self):
        queryset = ResourceContent.objects.all()

        m_type = self.request.query_params.get('resource_type', None)
        if m_type:
            return queryset.filter(resource_type=m_type)

        item_id = self.request.query_params.get('item', None)
        if item_id:
            return queryset.filter(item__id=item_id)

        return queryset


class ResourceContentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResourceContentSerializer
    queryset = ResourceContent.objects.all()