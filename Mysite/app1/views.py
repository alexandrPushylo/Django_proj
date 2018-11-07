from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response#
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm#
from django.contrib.auth import logout, authenticate, login

from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.views.generic import ListView

from django.contrib.auth.models import User

from app1.models import Person
from app1.locator import convert_adres, haversine
from app1.forms import LocForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.shortcuts import render, redirect





class LogoutView(View):
        def get(self, request):
                logout(request)
                return HttpResponseRedirect('/')
                pass

class UserRegistrationForm(FormView):
        form_class = UserCreationForm
        template_name = 'app1/signup.html'
        success_url = '/'
        def form_valid(self, form):
                form.save()
                return super(UserRegistrationForm, self).form_valid(form)
                pass

class LoginFormView(FormView):
        form_class = AuthenticationForm
        template_name = 'app1/signin.html'
        success_url = '/'

        def form_valid(self, form):
                self.user = form.get_user()
                login(self.request, self.user)
                return super(LoginFormView, self).form_valid(form)
                pass

method_decorator(login_required)
def UserProfile(request, id):
        user = get_object_or_404(User, id=id)

        if request.method == 'POST':
                form = LocForm(request.POST)
                if form.is_valid():
                        full_location = '{},{},{},{}'.format(form.cleaned_data['country'], 
                                                        form.cleaned_data['city'],
                                                        form.cleaned_data['street'],
                                                        form.cleaned_data['building'])
                        point_coords = convert_adres(full_location)
                        home_coords = '{},{},{},{}'.format(user.person.home_country,
                                                        user.person.home_city,
                                                        user.person.home_street,
                                                        user.person.home_building,)
                        home = convert_adres(home_coords)
                        dlina = haversine(float(home['latitude']), float(home['longitude']), point_coords['latitude'], point_coords['longitude'])
                        return HttpResponseRedirect("/accounts/{}".format(id))
        else:
                form = LocForm()
                return render(request, 'app1/myaccount.html',{'form':form})
                pass

