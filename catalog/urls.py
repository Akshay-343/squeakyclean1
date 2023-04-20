from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import AddressListView, AddressCreateView, AddressUpdateView, AddressDeleteView
from .views import (
    address_create,
    address_update,
    address_delete,
    address_list,
)


from . import views

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', views.index, name='index'),
    path('aboutus/services', views.services, name='services'),
    path('aboutus/contactus', views.contactus, name='contactus'),
    path('aboutus/whoweare', views.whoweare, name='whoweare'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/signup/", views.signup, name="signup"),
    path('accounts/myaccount/', views.myaccount, name='myaccount'),
    path('accounts/delete/', views.delete_account, name='delete_account'),
    path('accounts/terms/', views.terms, name='terms'),

    path('list/', address_list, name='address_list'),
    path('new/', address_create, name='address_create'),
    path('<int:pk>/edit/', address_update, name='address_update'),
    path('<int:pk>/delete/', address_delete, name='address_delete'),
]
