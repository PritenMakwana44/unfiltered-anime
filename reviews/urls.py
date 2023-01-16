from . import views
from django.urls import path

urlpatterns = [
  path('', views.ReviewList.as_view(), name='home'),
  path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
  path('upvotes/<slug:slug>', views.ReviewUpvotes.as_view(), name='review_upvotes'),
  path('downvotes/<slug:slug>', views.ReviewDownVotes.as_view(), name='review_downvotes'),
]