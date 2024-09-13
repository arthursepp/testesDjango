
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("gerenciar/", admin.site.urls),
    
    # path("produtos/", include("produtos.urls")),
    path('', include('produtos.urls')),
]
