from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.urls import reverse_lazy
from .models import AzobeojMainPost, CarouselMainPicture,LastAzobeojMainPost,Contactvideo
from .models import AzobeojProjectsMainPost,TeamsMainPost


# The main HomeView page
class HomeView(ListView): 
    model = CarouselMainPicture 
    template_name = 'azobeoj/home.html'
    context_object_name = 'carousel_posts'  # Name for the model data in the template

    # This method adds additional context data to the template
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
        # Add additional data to the context if needed
        context['azobeojposts'] = AzobeojMainPost.objects.all()  # Example of another model data
        context['lastazobeojposts'] = LastAzobeojMainPost.objects.all() 
        return context


 #The first Deus Magnus Video ArticleDetailView page
class ArticleDetailView(DetailView):
    model = AzobeojMainPost
    template_name = 'azobeoj/article_detail.html'
    def ArticleDetailView(request, pk): 
        object = get_object_or_404(AzobeojMainPost, pk=pk)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        return render(request, 'article_detail.html', {'detail': object})
    

 #The last Azobeoj Video ArticleDetailView page
class LastArticleDetailView(DetailView):
    model = LastAzobeojMainPost
    template_name = 'azobeoj/last_article_detail.html'
    def LastArticleDetailView(request, pk): 
        object = get_object_or_404(LastAzobeojMainPost, pk=pk)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        return render(request, 'last_article_detail.html', {'last_detail': object})
    
#AboutAzobeoj 
def AboutAzobeoj (request):
    return render (request,'azobeoj/AboutAzobeoj.html')

def OurServicesAzobeoj (request):
    return render (request,'azobeoj/services.html')

# The Contact view been implemented
class ContactView(ListView):
    model = Contactvideo
    template_name = 'azobeoj/contact_us.html'

    def get(self, request):
        videos = Contactvideo.objects.all()
        return render(request, self.template_name, {'object_list': videos,})

    def post(self, request):
        if request.method == 'POST':
            message_name = request.POST['message-name']
            message_email = request.POST['message-email']
            message_subject = request.POST['message-subject']
            message = request.POST['message']
            # Process the form (e.g., send an email)
            messages.success(request, f'Your email was Successfully {message_name}..')
            return render(request, 'azobeoj/message.html', {'message_name': message_name})
        else:
            # If the form is not valid, render the template again with the form errors
            videos = Contactvideo.objects.all()
            return render(request, self.template_name, {'object_list': videos,})
        
        
# The Contact view been implemented    


    # This method adds additional context data to the template
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
        # Add additional data to the context if needed
        context['azobeojposts'] = AzobeojMainPost.objects.all()  # Example of another model data
        context['lastazobeojposts'] = LastAzobeojMainPost.objects.all() 
        return context
    
#This is the projects services category of deus magnus
class ProjectsView(ListView):
    model = AzobeojProjectsMainPost
    template_name = 'azobeoj/projects.html'
    
#The projects article of the blog project of Deus Magnus
class ProjectsViewArticleDetail(DetailView):
    model = AzobeojProjectsMainPost
    template_name = 'azobeoj/project_article_detail.html'

    def ProjectsViewArticleDetail(request, pk):  
        object = get_object_or_404(AzobeojProjectsMainPost, pk=pk)
        return render(request, 'azobeoj/project_article_detail.html', {'projects_detail': object})
    
    
class TeamsView(ListView):
    model = TeamsMainPost
    template_name = 'azobeoj/teams.html'