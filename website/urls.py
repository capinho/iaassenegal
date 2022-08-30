
from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home ,name='home'),
    path('contact/', views.contact ,name='contact'),
    path('about-our-company/', TemplateView.as_view(template_name='about-our-company.html'),name='about-our-company'),
    path('financial-advisory-services/', TemplateView.as_view(template_name='financial-advisory-services.html'),name='financial-advisory-services'),
    path('audit-services/', TemplateView.as_view(template_name='audit-services.html'),name='audit-services'),
    path('mission-values/', TemplateView.as_view(template_name='mission-values.html'),name='mission-values'),
    path('assistance-technique-et-comptable/', TemplateView.as_view(template_name='assistance-technique-et-comptable.html'),name='assistance-technique-et-comptable'),
    path('tax-and-legal-advisory-services/', TemplateView.as_view(template_name='tax-and-legal-advisory-services.html'),name='tax-and-legal-advisory-services'),
    path('digital-advisory-services/', TemplateView.as_view(template_name='digital-advisory-services.html'),name='digital-advisory-services'),
    path('human-capital-advisory-services/', TemplateView.as_view(template_name='human-capital-advisory-services.html'),name='human-capital-advisory-services'),
]

