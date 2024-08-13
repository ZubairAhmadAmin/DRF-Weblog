
from django.urls import path
from api.views import ArticaleList, ArticaleDetail, UserList, UserDetail

app_name = 'api'

urlpatterns = [
    path('articale/', ArticaleList.as_view(), name='list'),
    path('articale/<slug:slug>', ArticaleDetail.as_view(), name='detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]