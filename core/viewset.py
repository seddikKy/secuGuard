from .mixins import StaffEditorPermissionsMixins
from .models import Product
from .serializer import SiteSerializer
from rest_framework import mixins, viewsets

class ProductViewSets(
    StaffEditorPermissionsMixins,
    viewsets.ModelViewSet):
    # get -> list -> QuerySet
    # get -> retreive
    # post -> create
    # put -> update
    # patch -> partial-update
    # delete -> destroy
    
    queryset = Product.objects.all()
    serializer_class = SiteSerializer

class ProductListRetreiveViewSet(
    viewsets.GenericViewSet, 
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = SiteSerializer

