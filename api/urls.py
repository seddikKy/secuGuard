from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth', obtain_auth_token, name='auth'),
    
    # Site API
    path('site/list-create/', views.SiteMixinViews.as_view(), name='list_create_site'),
    path('site/<int:pk>/', views.SiteMixinViews.as_view(), name='detail_site'),
    # path('site/<int:pk>/update', views.SiteMixinViews.as_view(), name='update_site'),
    # path('site/<int:pk>/delete', views.SiteMixinViews.as_view(), name='delete_site'),

    # Zone API
    path('zone/list-create/', views.ZoneMixinViews.as_view(), name='list_create_zone'),
    path('zone/<int:pk>/', views.ZoneMixinViews.as_view(), name='detail_zone'),
    # path('zone/<int:pk>/update', views.ZoneMixinViews.as_view(), name='update_zone'),
    # path('zone/<int:pk>/delete', views.ZoneMixinViews.as_view(), name='delete_zone'),

    # Employee API
    path('employee/list-create/', views.EmployeeMixinViews.as_view(), name='list_create_employee'),
    path('employee/<int:pk>/', views.EmployeeMixinViews.as_view(), name='detail_employee'),
    # path('employee/<int:pk>/update', views.EmployeeMixinViews.as_view(), name='update_employee'),
    # path('employee/<int:pk>/delete', views.EmployeeMixinViews.as_view(), name='delete_employee'),


    # tag_header API
    path('tag_header/list-create/', views.TagHeaderMixinViews.as_view(), name='list_create_tag_header'),
    path('tag_header/<int:pk>/', views.TagHeaderMixinViews.as_view(), name='detail_tag_header'),
]