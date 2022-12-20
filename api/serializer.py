from rest_framework import serializers
from rest_framework.reverse import reverse
from core.models import Employee, Site, TagHeader, Zone

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('id','name','id_entreprise', 'address','email','phone','RC','NIF')

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ('id', 'name','id_site')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','name','id_site', 'address','email','phone')


class TagHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagHeader
        fields = ('id', 'id_zone','code_nfc', 'name','order', 'observation')
