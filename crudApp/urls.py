from django.urls import path
from . import views
#urls patterns
urlpatterns =[
    path("",views.retrieve),
    path("Create/",views.creating),
    path("update/<int:id>",views.update),
    path("delete/<int:id>",views.deleting)
    
]