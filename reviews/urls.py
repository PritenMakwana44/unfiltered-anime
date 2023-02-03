from . import views
from django.urls import path
from .views import AddReview, DeleteCommentView, ReviewDetail




urlpatterns = [
  path('', views.ReviewList.as_view(), name='home'),
  path('add_review/', AddReview.as_view(), name="add_review"),
  path('edit_review/<slug:slug>', views.review_edit, name='edit_review'),
  path('review/<slug:slug>/delete/', views.delete_review,
       name='review_delete'),
  path('review/<str:slug>/', ReviewDetail.as_view(), name='review_detail'),
  path('review/<str:slug>/delete_comment/', DeleteCommentView.as_view(), name='delete_comment'),
  path('upvotes/<slug:slug>', views.ReviewUpvotes.as_view(),
       name='review_upvotes'),
  path('downvotes/<slug:slug>', views.ReviewDownVotes.as_view(),
       name='review_downvotes'),
  path('watch_later/add/<int:review_id>/', views.add_to_watch_later,
       name='add_to_watch_later'),
  path('watch_later/', views.watch_later_list, name='watch_later_list'),
  path('watch_later/remove/<int:watch_id>/', views.remove_from_watch_later,
       name='remove_from_watch_later'),
  path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
]
