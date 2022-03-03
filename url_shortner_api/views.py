from rest_framework.generics import CreateAPIView, ListAPIView

from url_shortner_api.models import Link
from url_shortner_api.serializers import LinkSerializer


class ShortenerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ShortenerCreateApiView(CreateAPIView):
    serializer_class = LinkSerializer
