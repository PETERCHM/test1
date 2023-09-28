from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name='landing_page'),
    path('contact/', views.contact_page, name='contact_page'),  
    path('grammarly/', views.grammarly_page, name='grammarly_page'),
    path('pricing/', views.pricing_page, name='pricing_page'),  
    path('run-selenium/', views.run_selenium, name='run_selenium'),

]




