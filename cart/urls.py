from django.urls import path
from . import views

urlpatterns = [
    path("", views.CartView.as_view(), name="cart_detail"),
    path("add/<int:product_id>/", views.AddToCartView.as_view(), name="add_to_cart"),
    path("update/<int:item_id>/", views.UpdateCartView.as_view(), name="update_cart"),
    path(
        "remove/<int:item_id>/",
        views.RemoveFromCartView.as_view(),
        name="remove_from_cart",
    ),
]
