from django.urls import path

from .views import ContainerListView

urlpatterns = [
    path('', ContainerListView.as_view(), name='home'),
]
