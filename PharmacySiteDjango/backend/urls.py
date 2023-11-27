from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homeView, name='home'),
    path('order/', views.process_order_form, name='order_medicine'),
    path('about-us/', views.about_page_view, name='about-us'),
    path('maps/', views.maps_page_view, name='maps'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
