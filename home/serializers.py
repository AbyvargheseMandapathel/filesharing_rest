from rest_framework import serializers
from .models import *

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(max_length=10000, allow_empty_file=False, use_url=False)
    )
    
    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.get('files', [])  # Use get() to provide a default empty list

        files_objs = []  # Use a list to collect Files instances

        for file in files:
            file_obj = Files.objects.create(folder=folder, file=file)
            files_objs.append(file_obj)

        # Return data as a dictionary with files and folder UID
        return {'files': files_objs, 'folder': str(folder.uid)}
