from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from TODO_app.models import RegisterLogo, Register

class FirstResource(ModelResource):
    class Meta:
        collection_name = "todo_title"
        queryset = RegisterLogo.objects.all()
        resource_name = Authorization()

class SecondResource(ModelResource):
    class Meta:
        collection_name = "todo_fields"
        queryset = Register.objects.all()
        resource_name = 'register1'
        authorization = Authorization()

