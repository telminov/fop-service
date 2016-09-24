from rest_framework import views
from rest_framework.response import Response


class Index(views.APIView):
    def get(self, request):
        return Response({'message': 'hello!'})

index = Index.as_view()
