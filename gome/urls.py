
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import RedirectView
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/', views.app01),

]