from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('pdf', views.pdf_recieve, name='pdf_recieve'),
    path('del_pdf', views.delete_pdfs, name='delete_pdfs'),
    path('get_seniority', views.get_seniority, name='get_seniority'),
    path('get_name', views.get_name, name='get_name'),
    path('get_email', views.get_email, name='get_email'),
    path('get_faculty', views.get_faculty, name='get_faculty'),
    path('get_address', views.get_address, name='get_address'),
    path('get_pr_lang', views.get_pr_lang, name='get_pr_lang'),
    path('get_info', views.get_info, name='get_info'),
]