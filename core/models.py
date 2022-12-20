from django.db import models



class Entreprise(models.Model):
    name = models.CharField('Nom de l\'entreprise', max_length=120)
    address = models.CharField('addresse', max_length=120)
    email = models.EmailField('Email', blank=True)
    phone = models.CharField('Numéro de téléphone', max_length=25, blank=True, null=True)
    RC = models.CharField('Registre de commerce', max_length=50, blank=True, null=True) 
    NIF = models.CharField('Num Ident fisc', max_length=50, blank=True, null=True)
    created_at = models.DateTimeField('Créer le', auto_now=True)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField('Nom du site', max_length=120)
    id_entreprise = models.ForeignKey(Entreprise,on_delete=models.CASCADE)
    address = models.CharField('addresse', max_length=120 )
    email = models.EmailField('Email', blank=True)
    phone = models.CharField('Numéro de téléphone', max_length=25, blank=True, null=True)
    RC = models.CharField('Registre de commerce', max_length=50, blank=True, null=True) 
    NIF = models.CharField('Num Ident fisc', max_length=50, blank=True, null=True)
    created_at = models.DateTimeField('Créer le', auto_now=True)

    def __str__(self):
        return self.name + f" ({self.id_entreprise.name})"


class Zone(models.Model):
    name = models.CharField('Nom de la zone', max_length=120)
    id_site = models.ForeignKey(Site,on_delete=models.CASCADE)
    created_at = models.DateTimeField('Créer le', auto_now=True)

    def __str__(self):
        return self.name + f" ({self.id_site.name} - {self.id_site.id_entreprise.name})"



class Employee(models.Model):
    name = models.CharField('Nom de l\'employée', max_length=120)
    id_site = models.ForeignKey(Site,on_delete=models.CASCADE)
    address = models.CharField('addresse', max_length=120 )
    email = models.EmailField('Email', blank=True)
    phone = models.CharField('Numéro de téléphone', max_length=25, blank=True, null=True)
    created_at = models.DateTimeField('Créer le', auto_now=True)

    def __str__(self):
        return self.name


class TagHeader(models.Model):

    id_zone = models.ForeignKey(Zone,on_delete=models.CASCADE)
    code_nfc = models.CharField('NFC', max_length=120)
    name = models.CharField('Nom du TAG', max_length=120)
    order = models.PositiveIntegerField('Ordre', blank=True, null=True)
    observation = models.CharField('Observation', max_length=120)
    created_at = models.DateTimeField('Créer le', auto_now=True)
    
    def __str__(self):
        return self.name
    


class TagDetail(models.Model):
    id_tag = models.ForeignKey(TagHeader,on_delete=models.CASCADE)
    memo_path = models.CharField('Lien de la memo', max_length=120,blank=True, null=True)
    image_path = models.ImageField(null=True, blank=True, upload_to="images/")
    anomaly = models.TextField('Anomalie', blank=True, null=True)
    is_checked = models.BooleanField('tag visité',default=False)
    created_at = models.DateTimeField('Créer le', auto_now=True)

    def __str__(self):
        return self.id_tag.name