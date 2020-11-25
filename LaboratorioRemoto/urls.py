from django.contrib import admin
from django.urls import path, include
from Usuarios.views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from Usuarios.models import *
from Usuarios.serializers import *


router = routers.DefaultRouter()
router.register(r'entradas', EntradaViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista_inicio),

    #Links de seccion usuarios
    path('miembros', area_miembros),

    path('register', register),
    path('login', login),
    path('logout', logout),
    path('entradas', entrada_list, name='entrada_list'),
    path('entrada/<int:pk>/', entrada_detail, name='entrada_detail'),
    path('entrada/new', entrada_new, name='entrada_new'),
    path('entrada/<int:pk>/edit/', entrada_edit, name='entrada_edit'),
    path('api-auth/', include('rest_framework.urls')),
    path('api', include(router.urls)),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
