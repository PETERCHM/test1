from django.urls import path
from . import views

urlpatterns = [
    path("", views.frontpage, name='frontpage'),
    path('landing/', views.landing_page, name='landing_page'),
    path('landing/contact/', views.contact_page, name='contact_page'),  
    path('landing/grammarly/', views.grammarly_page, name='grammarly_page'),
    path('landing/pricing/', views.pricing_page, name='pricing_page'),  
    path('landing/run-selenium/', views.run_selenium, name='run_selenium'),
    path('landing/run_cliffnote/', views.run_cliffnote, name='run_cliffnote'),
    path('landing/run_quillbot/', views.run_quillbot, name='run_quillbot'),
    path('landing/run_studypool/', views.run_studypool, name='run_studypool'),
    path('register/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
]


