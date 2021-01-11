from django.urls import path

from .views import IndexPageView, ProductDetailView, SendEmailView

urlpatterns = [

    path('', IndexPageView.as_view(), name="index"),
    path('<slug:slug>/', ProductDetailView.as_view(), name="product_detail"),
    path('send_email', SendEmailView.as_view(), name="send_email"),

]
