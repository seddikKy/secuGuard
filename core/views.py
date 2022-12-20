from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.contrib.auth.models import User
from .models import Employee, Entreprise, Site,TagHeader, Zone
from .forms import EmployeeFrom, EntrepriseFrom, SiteFrom,TagHeaderForm, ZoneFrom
from django.core.paginator import Paginator
from django.contrib import messages


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'secu_guard/home.html',{})

#Entreprise
def add_entreprise(request, *args, **kwargs):
    submitted = False
    if request.method == "POST":
        form = EntrepriseFrom(request.POST)

        if form.is_valid() :
            form.save()
            messages.success(request,("Entreprise ajoutée avec succès!!"))
            #return HttpResponseRedirect('/add_entreprise?submitted=True') #?submitted=True: pass the variable to the web page add_entreprise.html
            return redirect('list_entreprises')
    else:
        form = EntrepriseFrom
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'secu_guard/entreprise/add_entreprise.html',{"form": form, 'submitted':submitted})


def update_entreprise(request, *args, **kwargs):
    entreprise = Entreprise.objects.get(pk=kwargs['entreprise_id'])
    form = EntrepriseFrom(request.POST or None, request.FILES or None, instance=entreprise)  #request.POST or None: use this form to POST data or doing nothing
                                                            #instance=entreprise: set data to the form
    if form.is_valid():
        form.save()
        return redirect('list_entreprises')
    return render(request, 'secu_guard/entreprise/update_entreprise.html', {'entreprise': entreprise, 'form': form})


def delete_entreprise(request, *args, **kwargs):
    entreprise = Entreprise.objects.get(pk=kwargs['entreprise_id'])
    if request.user.is_superuser:
        entreprise.delete()
        messages.success(request,("Entreprise supprimée avec succès!!"))
        return redirect('list_entreprises')
    else:
        messages.success(request,("Vous n'etes pas autorisé à supprimer cette entreprise!!"))
        return redirect('list_entreprises')


class ListEntreprises(View):
    def get(self, request, *args, **kwargs):
        entreprises_list = Entreprise.objects.all().order_by('name')
        #Set up pagination
        p = Paginator(entreprises_list,6) 
        page = request.GET.get('page')
        entreprises = p.get_page(page)

        #Number of pages - we will replace the "a" by the number of page in the template
        nums = "a" * entreprises.paginator.num_pages

        return render(request, 'secu_guard/entreprise/list_entreprises.html', {"entreprises":entreprises, "nums": nums})


class ShowEntreprise(View):
    def get(self, request, *args, **kwargs):
        entreprise = Entreprise.objects.get(pk=kwargs['entreprise_id'])
        return render(request, 'secu_guard/entreprise/show_entreprise.html', {"entreprise":entreprise})


#Sites
def add_site(request, *args, **kwargs):
    submitted = False
    if request.method == "POST":
        form = SiteFrom(request.POST)

        if form.is_valid() :
            form.save()
            messages.success(request,("Site ajouté avec succès!!"))
            #return HttpResponseRedirect('/add_entreprise?submitted=True') #?submitted=True: pass the variable to the web page add_entreprise.html
            return redirect('list_sites')
    else:
        form = SiteFrom
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'secu_guard/site/add_site.html',{"form": form, 'submitted':submitted})


def update_site(request, *args, **kwargs):
    site = Site.objects.get(pk=kwargs['site_id'])
    form = SiteFrom(request.POST or None, request.FILES or None, instance=site)  #request.POST or None: use this form to POST data or doing nothing
                                                            #instance=entreprise: set data to the form
    if form.is_valid():
        form.save()
        return redirect('list_sites')
    return render(request, 'secu_guard/site/update_site.html', {'sites': site, 'form': form})


def delete_site(request, *args, **kwargs):
    site = Site.objects.get(pk=kwargs['site_id'])
    if request.user.is_superuser:
        site.delete()
        messages.success(request,("Site supprimé avec succès!!"))
        return redirect('list_sites')
    else:
        messages.success(request,("Vous n'etes pas autorisé à supprimer ce site!!"))
        return redirect('list_sites')

class ListSites(View):
    def get(self, request, *args, **kwargs):
        sites_list = Site.objects.all().order_by('name')
        #Set up pagination
        p = Paginator(sites_list,6) 
        page = request.GET.get('page')
        sites = p.get_page(page)

        #Number of pages - we will replace the "a" by the number of page in the template
        nums = "a" * sites.paginator.num_pages

        return render(request, 'secu_guard/site/list_sites.html', {"sites":sites, "nums": nums})


class ShowSite(View):
    def get(self, request, *args, **kwargs):
        site = Site.objects.get(pk=kwargs['site_id'])
        return render(request, 'secu_guard/site/show_site.html', {"site":site})


# Zones
def add_zone(request, *args, **kwargs):
    submitted = False
    if request.method == "POST":
        form = ZoneFrom(request.POST)

        if form.is_valid() :
            form.save()
            messages.success(request,("zone ajouté avec succès!!"))
            #return HttpResponseRedirect('/add_entreprise?submitted=True') #?submitted=True: pass the variable to the web page add_entreprise.html
            return redirect('list_zones')
    else:
        form = ZoneFrom
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'secu_guard/zone/add_zone.html',{"form": form, 'submitted':submitted})


def update_zone(request, *args, **kwargs):
    zone = Zone.objects.get(pk=kwargs['zone_id'])
    form = ZoneFrom(request.POST or None, request.FILES or None, instance=zone)  #request.POST or None: use this form to POST data or doing nothing
                                                            #instance=entreprise: set data to the form
    if form.is_valid():
        form.save()
        return redirect('list_zones')
    return render(request, 'secu_guard/zone/update_zone.html', {'zones': zone, 'form': form})


def delete_zone(request, *args, **kwargs):
    zone = Zone.objects.get(pk=kwargs['zone_id'])
    if request.user.is_superuser:
        zone.delete()
        messages.success(request,("zone supprimé avec succès!!"))
        return redirect('list_zones')
    else:
        messages.success(request,("Vous n'etes pas autorisé à supprimer cette zone!!"))
        return redirect('list_zones')

class ListZones(View):
    def get(self, request, *args, **kwargs):
        zones_list = Zone.objects.all().order_by('name')
        #Set up pagination
        p = Paginator(zones_list,6) 
        page = request.GET.get('page')
        zones = p.get_page(page)

        #Number of pages - we will replace the "a" by the number of page in the template
        nums = "a" * zones.paginator.num_pages

        return render(request, 'secu_guard/zone/list_zones.html', {"zones":zones, "nums": nums})


class ShowZone(View):
    def get(self, request, *args, **kwargs):
        zone = Zone.objects.get(pk=kwargs['zone_id'])
        return render(request, 'secu_guard/zone/show_zone.html', {"zone":zone})


# Employee
def add_employee(request, *args, **kwargs):
    submitted = False
    if request.method == "POST":
        form = EmployeeFrom(request.POST)

        if form.is_valid() :
            form.save()
            messages.success(request,("Agent ajoutée avec succès!!"))
            #return HttpResponseRedirect('/add_employee?submitted=True') #?submitted=True: pass the variable to the web page add_employee.html
            return redirect('list_employees')
    else:
        form = EmployeeFrom
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'secu_guard/employee/add_employee.html',{"form": form, 'submitted':submitted})


def update_employee(request, *args, **kwargs):
    employee = Employee.objects.get(pk=kwargs['employee_id'])
    form = EmployeeFrom(request.POST or None, request.FILES or None, instance=employee)  #request.POST or None: use this form to POST data or doing nothing
                                                            #instance=employee: set data to the form
    if form.is_valid():
        form.save()
        return redirect('list_employees')
    return render(request, 'secu_guard/employee/update_employee.html', {'employee': employee, 'form': form})


def delete_employee(request, *args, **kwargs):
    employee = Employee.objects.get(pk=kwargs['employee_id'])
    if request.user.is_superuser:
        employee.delete()
        messages.success(request,("employee supprimée avec succès!!"))
        return redirect('list_employees')
    else:
        messages.success(request,("Vous n'etes pas autorisé à supprimer cette employee!!"))
        return redirect('list_employees')

class ListEmployees(View):
    def get(self, request, *args, **kwargs):
        employees_list = Employee.objects.all().order_by('name')
        #Set up pagination
        p = Paginator(employees_list,6) 
        page = request.GET.get('page')
        employees = p.get_page(page)

        #Number of pages - we will replace the "a" by the number of page in the template
        nums = "a" * employees.paginator.num_pages

        return render(request, 'secu_guard/employee/list_employees.html', {"employees":employees, "nums": nums})


class ShowEmployee(View):
    def get(self, request, *args, **kwargs):
        employee = Employee.objects.get(pk=kwargs['employee_id'])
        return render(request, 'secu_guard/employee/show_employee.html', {"employee":employee})

    

# tag_header
def add_tag_header(request, *args, **kwargs):
    submitted = False
    if request.method == "POST":
        form = TagHeaderForm(request.POST)

        if form.is_valid() :
            form.save()
            messages.success(request,("Agent ajoutée avec succès!!"))
            #return HttpResponseRedirect('/add_tag_header?submitted=True') #?submitted=True: pass the variable to the web page add_tag_header.html
            return redirect('list_tag_headers')
    else:
        form = TagHeaderForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'secu_guard/tag_header/add_tag_header.html',{"form": form, 'submitted':submitted})


def update_tag_header(request, *args, **kwargs):
    tag_header = TagHeader.objects.get(pk=kwargs['tag_header_id'])
    form = TagHeaderForm(request.POST or None, request.FILES or None, instance=tag_header)  #request.POST or None: use this form to POST data or doing nothing
                                                            #instance=tag_header: set data to the form
    if form.is_valid():
        form.save()
        return redirect('list_tag_headers')
    return render(request, 'secu_guard/tag_header/update_tag_header.html', {'tag_header': tag_header, 'form': form})


def delete_tag_header(request, *args, **kwargs):
    tag_header = TagHeader.objects.get(pk=kwargs['tag_header_id'])
    if request.user.is_superuser:
        tag_header.delete()
        messages.success(request,("Tag supprimée avec succès!!"))
        return redirect('list_tag_headers')
    else:
        messages.success(request,("Vous n'etes pas autorisé à supprimer cette tag_header!!"))
        return redirect('list_tag_headers')


class ListTagHeaders(View):
    def get(self, request, *args, **kwargs):
        tag_headers_list = TagHeader.objects.all().order_by('name')
        #Set up pagination
        p = Paginator(tag_headers_list,6) 
        page = request.GET.get('page')
        tag_headers = p.get_page(page)

        #Number of pages - we will replace the "a" by the number of page in the template
        nums = "a" * tag_headers.paginator.num_pages

        return render(request, 'secu_guard/tag_header/list_tag_headers.html', {"tag_headers":tag_headers, "nums": nums})


class ShowTagHeader(View):
    def get(self, request, *args, **kwargs):
        tag_header = TagHeader.objects.get(pk=kwargs['tag_header_id'])
        return render(request, 'secu_guard/tag_header/show_tag_header.html', {"tag_header":tag_header})

    