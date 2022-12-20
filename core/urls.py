from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    #Entreprise path
    path('add_entreprise/', views.add_entreprise, name="add_entreprise"),
    path('update_entreprise/<entreprise_id>', views.update_entreprise, name="update_entreprise"),
    path('list_entreprises/', views.ListEntreprises.as_view(), name="list_entreprises"),
    path('delete_entreprise/<entreprise_id>', views.delete_entreprise, name="delete_entreprise"),
    path('show_entreprise/<entreprise_id>', views.ShowEntreprise.as_view(), name="show_entreprise"),

    #Site path
    path('add_site/', views.add_site, name="add_site"),
    path('update_site/<site_id>', views.update_site, name="update_site"),
    path('list_sites/', views.ListSites.as_view(), name="list_sites"),
    path('delete_site/<site_id>', views.delete_site, name="delete_site"),
    path('show_site/<site_id>', views.ShowSite.as_view(), name="show_site"),

    #Zone path
    path('add_zone/', views.add_zone, name="add_zone"),
    path('update_zone/<zone_id>', views.update_zone, name="update_zone"),
    path('list_zones/', views.ListZones.as_view(), name="list_zones"),
    path('delete_zone/<zone_id>', views.delete_zone, name="delete_zone"),
    path('show_zone/<zone_id>', views.ShowZone.as_view(), name="show_zone"),

    #Employee path
    path('add_employee/', views.add_employee, name="add_employee"),
    path('update_employee/<employee_id>', views.update_employee, name="update_employee"),
    path('list_employees/', views.ListEmployees.as_view(), name="list_employees"),
    path('delete_employee/<employee_id>', views.delete_employee, name="delete_employee"),
    path('show_employee/<employee_id>', views.ShowEmployee.as_view(), name="show_employee"),

    #Tagheader path
    path('add_tag_header/', views.add_tag_header, name="add_tag_header"),
    path('update_tag_header/<tag_header_id>', views.update_tag_header, name="update_tag_header"),
    path('list_tag_headers/', views.ListTagHeaders.as_view(), name="list_tag_headers"),
    path('delete_tag_header/<tag_header_id>', views.delete_tag_header, name="delete_tag_header"),
    path('show_tag_header/<tag_header_id>', views.ShowTagHeader.as_view(), name="show_tag_header"),

]