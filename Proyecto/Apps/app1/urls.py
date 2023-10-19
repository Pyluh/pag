from django.urls import path 
from . import views 
urlpatterns = [ 
    path('', views.home) 
]
from django.contrib import admin  
from django.urls import path, include  
urlpatterns = [ 
path('admin/', admin.site.urls), 
path('', include('Apps.app1.urls'))  # <---------- Agregar esto  
]

urlpatterns = [ 
    path('', views.home), 
    path('eliminarFact/<fact_text>',views.eliminarFact), 
    path('edicionFact/<fact_text>',views.edicionFact), 
    path('editarFact/<fact_text>/', views.editarFact, name='editar_fact'),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('django.contrib.urls')) 
]
