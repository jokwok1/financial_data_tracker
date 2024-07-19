from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response 
from .models import Entry
from rest_framework import generics, status
from .serializers import UserSerializer, EntrySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from rest_framework.views import APIView
from .utils import process_csv_file, generate_chart_json, save_csv_file

# Create your views here.
class CreateUserView(generics.CreateAPIView): 
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

class UploadCSVView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EntrySerializer

    def post(self, request, *args, **kwargs):
        try:
            if 'file' in request.FILES:
                csv_file = request.FILES['file']
                # Save CSV File
                file_path = save_csv_file(csv_file, self.request.user)
                # Process the data and persist the Entry in the database
                data_entries = process_csv_file(file_path, self.request.user)
                return JsonResponse({'message': 'File uploaded and processed successfully'}, status=200)
            else:
                return JsonResponse({'error': 'No file found in request'}, status=400)
        except Exception as e:
            print("Exception", e)
            return JsonResponse({'error': f'Error processing CSV file: {str(e)}'}, status=500)

class GenerateChartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data_entries = self.get_user_entries(request.user)
        chart_json = generate_chart_json(data_entries)
        serialized_data = EntrySerializer(data_entries, many=True).data
        print('chart_json ', chart_json)
        return Response({'chart_json': chart_json, 'data': serialized_data})

    def get_user_entries(self, user):
        # Fetch all entries made by the authenticated user
        user_entries = Entry.objects.filter(author=user)
        return user_entries
    
class UserEntriesView(generics.ListAPIView):
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return entries for the authenticated user
        user = self.request.user
        return Entry.objects.filter(author=user)