from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.views import APIView

from advertising_project.settings import MEDIA_ROOT
from app.permissions import IsOwnerOrReadOnly


class Image(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, name, format=None):
        print('.............................................')
        print(request)
        with open(MEDIA_ROOT + '/' + name, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='content/image', )
            response['Content-Disposition'] = 'attachment; filename="%s"' % name
            return response
