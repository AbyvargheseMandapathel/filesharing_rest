from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileListSerializer
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser

def home(request):
    return render(request, 'home.html')

def download(request,uid):
    return render(request, 'download.html',context={'uid':uid})

class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = FileListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'File Success',
                    'data':serializer.data
                })

            # If the serializer is not valid, return a response with error details
            return Response({
                'status': 400,
                'message': 'File Failure',
                'data': serializer.errors
            })

        except Exception as e:
            # Handle exceptions and return an error response
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'error': str(e)
            })
