from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from .forms.add_profile_user import AddProfileUser
from .models import ProfileUser, UserFood


class ProfileFormView(ListView):
    template_name = "profile_user.html"

    def get(self, request, *args, **kwargs):
        user_current_name = ProfileUser.objects.filter(username__username=request.user.username)
        user_product_history = UserFood.objects.filter(username__username=request.user.username)
        person_form = AddProfileUser()
        context = {
            'person_form': person_form,
            'profile_current_user': user_current_name,
            'profile_product_user': user_product_history
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = AddProfileUser(request.POST, request.FILES)
        if user_form.is_valid():
            user_form = ProfileUser(username=request.user.username, photo=request.FILES['photo'])
            user_form.save()
            return super(ProfileFormView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
