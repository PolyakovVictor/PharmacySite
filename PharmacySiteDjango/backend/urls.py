from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homeView, name='home'),
    path('order/', views.process_order_form, name='order_medicine'),
    path('api/pharmacies/', views.get_pharmacies, name='get_pharmacies'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
