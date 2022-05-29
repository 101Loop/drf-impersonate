from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ImpersonateView(APIView):
    def post(self, request, format=None):
        return Response(status=status.HTTP_200_OK)
