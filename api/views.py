from django.shortcuts import render
from rest_framework import authentication, generics, mixins
from .serializer import EmployeeSerializer, SiteSerializer, TagHeaderSerializer, ZoneSerializer
from .mixins import StaffEditorPermissionsMixins
from core.models import Employee, Site, TagHeader, Zone


# Site Api
class SiteMixinViews(
    StaffEditorPermissionsMixins,
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin):

    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    lookup_field = 'pk'
    
    def perform_create(self, serializer):
        serializer.save()
    
    def perform_update(self, serializer):
        serializer.save()
    
    # Retreive Site
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        # return List Sites
        return self.list(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


# Zone Api
class ZoneMixinViews(
    StaffEditorPermissionsMixins,
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin):

    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    lookup_field = 'pk'
    
    def perform_create(self, serializer):
        serializer.save()
    
    def perform_update(self, serializer):
        serializer.save()
    
    # Retreive Zone
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        # return List Zones
        return self.list(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


# Employee Api
class EmployeeMixinViews(
    StaffEditorPermissionsMixins,
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    
    def perform_create(self, serializer):
        serializer.save()
    
    def perform_update(self, serializer):
        serializer.save()
    
    # Retreive Employee
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        # return List Employees
        return self.list(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


# TagHeader Api
class TagHeaderMixinViews(
    StaffEditorPermissionsMixins,
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin):

    queryset = TagHeader.objects.all()
    serializer_class = TagHeaderSerializer
    lookup_field = 'pk'
    
    def perform_create(self, serializer):
        serializer.save()
    
    def perform_update(self, serializer):
        serializer.save()
    
    # Retreive Site
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        # return List Sites
        return self.list(request, *args, **kwargs)