from django.urls import path
from .views import QuizAPIView, AllVideosAPIView, SingleVideoAPIView, AllCategoriesAPIView

urlpatterns = [
    path('quiz/', QuizAPIView.as_view(), name='quiz'),
    path('videos/', AllVideosAPIView.as_view(), name='all_videos'),
    path('videos/<int:id>/', SingleVideoAPIView.as_view(), name='single_video'),
    path('categories/', AllCategoriesAPIView.as_view(), name='all_categories'),
]
