from django.shortcuts import render, redirect
from django.views.generic import CreateView
from pickuphockey.forms import SignUp, LoginForm, CustomPasswordResetForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth import login
from django.core.mail import send_mail




def baseview(request):
    return render(request, 'base.html')

def homepage(request):
    return render(request, 'home.html')




class SignUp(CreateView):
    form_class = SignUp
    success_url = reverse_lazy('home')
    template_name = 'sign_up.html'

    def form_valid(self, form):
        request = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return request 
    
class CustomLogin(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('OrgDash:player_dash')
    



class PasswordReset(PasswordResetView):
    template_name = 'registration/reset_password.html'
    form_class = CustomPasswordResetForm
    

class PasswordResetSent(PasswordResetDoneView):
    template_name = 'registration/password_reset_sent.html'
   

class PasswordResetFormView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_form.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'registration/password_reset_done.html'

def Thanks(request):
    return render(request, 'thanks.html')
def MessageSent(request):
    return render(request, 'message_sent.html')

def Contact(request):
    if request.method == 'POST':
        from_email = request.POST.get('inputemail')
        message = request.POST.get('message')
        name = request.POST.get('name')
        confirm_message = "<h1>Thank you for reaching out</h1><br><p>We are currently reviewing your message and will respond as soon as we can</p><br><h2>Your message:</h2><br> " + message
        inbound_message = "<h1>Message from " + name + "<h1><br><h2>Email: " + from_email + "<br><h2>Message: " + message
        # email to site
        send_mail("Contact form recieved from " + name, 'message' , from_email,  ['pickuphockey1@gmail.com'], html_message=inbound_message)
        # email copy for sender
        send_mail("Hi " + name +" thanks for your message,", 'message', 'pickuphockey1@gmail.com' ,  [from_email], html_message=confirm_message)
       
        return redirect('message_sent')
    else:
        return render(request, 'contact.html')
    
def HowItWorks(request):
    return render(request, 'how_it_works.html')




   



