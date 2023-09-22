from django.urls import path
from .import views
urlpatterns = [
   path("",views.index, name="index"),
   path("python",views.python,name="python"),
   path("django",views.django,name="python"),
   
]
