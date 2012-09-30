from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from ptg.apps.appptg.models import Persona
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.authorization import Authorization

class MyModelResource(ModelResource):
    class Meta:
        queryset = Persona.objects.all()
        allowed_methods = ['get','post']
        resource_name = 'persona'
        authorization= Authorization()
