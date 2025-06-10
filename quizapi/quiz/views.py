from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import QuizSerializer
import random
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import VideoSerializer
from .models import Category
from .serializers import CategorySerializer

class QuizAPIView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        if not videos:
            return Response({"error": "No videos available"}, status=404)
        video = random.choice(videos)
        serializer = QuizSerializer(video, context={'request': request})
        return Response(serializer.data)

class AllVideosAPIView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class SingleVideoAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'id'

class VideosByCategoryAPIView(APIView):
    def get(self, request):
        category_id = request.query_params.get('category_id')
        if category_id:
            videos = Video.objects.filter(category__id=category_id)
        else:
            videos = Video.objects.all().order_by('?')  # return random if no category selected
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)


