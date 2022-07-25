from django.urls import path

from .views import (
    ShipmentListView,
    ShipmentUpdateView,
    ShipmentDetailView,
    ShipmentDeleteView,
)
    

urlpatterns = [
    path('<int:pk>/edit/', ShipmentUpdateView.as_view(), name='shipment_edit'),
    path('<int:pk>/', ShipmentDetailView.as_view(), name='shipment_detail'),
    path('<int:pk>/delete/', ShipmentDeleteView.as_view(), name='shipment_delete'),
    path('', ShipmentListView.as_view(), name='shipment_list'),
]
