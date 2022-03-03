from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from url_shortner_api.models import Link
from url_shortner_api.serializers import LinkSerializer


class ShortenerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ShortenerCreateApiView(CreateAPIView):
    serializer_class = LinkSerializer

    # Over-riding the default create()
    # to skip creating short url for already existing long url
    def create(self, request, *args, **kwargs):

        link_obj = Link.objects.filter(original_link__exact=request.data["original_link"]).first()
        if link_obj:
            serializer = LinkSerializer(link_obj)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Redirector(View):
    def get(self, request, shortener_link, *args, **kwargs):
        shortener_link = settings.HOST_URL + "/" + self.kwargs["shortener_link"]
        redirect_link = Link.objects.filter(shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)
