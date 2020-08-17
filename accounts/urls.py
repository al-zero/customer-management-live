from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home_view,
    product_view,
    customer_view,
    createOrder,
    updateOrder,
    deleteOrder,
    register_view,
    login_view,
    logoutUser,
    userPage,
    accountSettings,
)

urlpatterns = [
    path('products/', product_view, name='products'),
    path('customer/<str:pk>/', customer_view, name='customer'),
    path('user/', userPage, name='user-page'),
    path('', home_view, name='home'),

    path('account', accountSettings, name='account'),

    # CRUD
    path('create_order/<str:pk>', createOrder, name='create_order'),
    path('update_order/<str:pk_test>/', updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', deleteOrder, name='delete_order'),

    # Registration and Login
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logoutUser, name='logout'),

    # Password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_complete'),
]
