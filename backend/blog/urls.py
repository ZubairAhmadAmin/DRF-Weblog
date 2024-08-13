from django.urls import path

from .views import ArticaleList, ArticaleDetail

app_name = 'blog'

urlpatterns = [
    path('', ArticaleList.as_view(), name='artiale-list'),
    path('<slug:slug>/', ArticaleDetail.as_view(), name='artiale-detail'),
    
]