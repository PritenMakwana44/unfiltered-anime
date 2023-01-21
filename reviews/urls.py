from . import views
from django.urls import path
from .views import AddReview

urlpatterns = [
  path('', views.ReviewList.as_view(), name='home'),
  path('add_review/', AddReview.as_view(), name="add_review"),
  #path('edit_review/<slug:slug>', ReviewEdit.as_view(), name='edit_review'),
  path('upvotes/<slug:slug>', views.ReviewUpvotes.as_view(), name='review_upvotes'),
  path('downvotes/<slug:slug>', views.ReviewDownVotes.as_view(), name='review_downvotes'),
  path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
  
]