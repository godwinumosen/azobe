from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,LastArticleDetailView,ContactView,ProjectsView
from .views import ProjectsViewArticleDetail,TeamsView


urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('about/', views.AboutAzobeoj, name='about'),
    path('our_services/', views.OurServicesAzobeoj, name='our_services'),
    #path('contact/', views.Contact_Us, name='contact'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    path('last_article/<int:pk>/', LastArticleDetailView.as_view(), name="last_detail"),
    #path('carousel/', CarouselPicture.as_view(), name="carousel"),
    path('contact/', ContactView.as_view(), name='contact'),
    path('teams/', TeamsView.as_view(), name='teams'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects_detail/<int:pk>/', ProjectsViewArticleDetail.as_view(), name="projects_detail"),
    
] 