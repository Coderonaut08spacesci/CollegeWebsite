from django.urls import path
from . import views

urlpatterns = [
    # CBV Routes
    path('notices/', views.NoticeListView.as_view(), name='notice-list'),
    path('notices/<int:pk>/', views.NoticeDetailView.as_view(), name='notice-detail'),  # URL parameter
    path('notices/new/', views.NoticeCreateView.as_view(), name='notice-create'),
    path('notices/<int:pk>/update/', views.NoticeUpdateView.as_view(), name='notice-update'),
    path('notices/<int:pk>/delete/', views.NoticeDeleteView.as_view(), name='notice-delete'),
    
    # FBV Routes
    path('search/', views.search_view, name='search'),  # Query parameter ?q=
    path('contact/', views.contact_view, name='contact'),
]