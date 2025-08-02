from django.shortcuts import render,redirect
from ekart.forms import SignUpForm ,SignInForm
from django.contrib.auth.models import User
from django.views.generic import CreateView,TemplateView,FormView,DetailView
from django.contrib import messages
from django.views import View
from django.contrib.auth import login,logout,authenticate
from admindash.models import Product







# Create your views here.

class Home(TemplateView):
    template_name='index.html'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['products']=Product.objects.all()
        return context

class SignUpView(CreateView):
    form_class=SignUpForm
    model = User
    template_name='register.html'
    
    def form_valid(self,form):
        User.objects.create_user(**form.cleaned_data)
        messages.success(self.request,'Registration succesfull')
        return redirect('home')
    def form_invalid(self,form):
        messages.warning(self.request,'Invalid inputs')
        return redirect('register.html')  
    
class SignInView(FormView):  
    form_class=SignInForm
    template_name='signin.html' 
    
    def post(self,request,*args,**kwargs):
        uname=request.POST.get("username")  
        pswd=request.POST.get("password")  
        user=authenticate(request,username=uname,password=pswd)
        if user:
            if user.is_superuser == 1:
                return render(request,"dashboard.html")
        
            else:
                login(request,user)
                messages.success(request,'Login Successful')
                return redirect('home')
        else:
            messages.warning(request,'Invalid inputs')
            return redirect('signin')    
        
        
class SignOutView(View):
    def get(self,request):
        logout(request)
        return redirect('signin_view')        
    
    
class ProductDetailView(DetailView):
    model=Product
    pk_url_kwarg='id'
    template_name='productdetail.html'
    context_object_name='product'  
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       current_product = self.get_object()  #Fetches the current product being viewed (based on URL like /detail/1), using Django’s built-in get_object() method from the DetailView.
       context['related_products'] = Product.objects.filter(
           category=current_product.category
       ).exclude(id=current_product.id)[:4]  #thisLimit to 4 related products
       return context  


    