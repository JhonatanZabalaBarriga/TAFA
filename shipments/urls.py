from django.urls import path

from .views import (
    ShipmentListView,
    ShipmentCreateView,
    ShipmentUpdateView,
    ShipmentDetailView,
    ShipmentDeleteView,
)
    

urlpatterns = [
    path('shipment/new/', ShipmentCreateView.as_view(), name='shipment_new'),
    path('<str:pk>/edit/', ShipmentUpdateView.as_view(), name='shipment_edit'),
    path('<str:pk>/', ShipmentDetailView.as_view(), name='shipment_detail'),
    path('<str:pk>/delete/', ShipmentDeleteView.as_view(), name='shipment_delete'),
    path('', ShipmentListView.as_view(), name='shipment_list'),
]
