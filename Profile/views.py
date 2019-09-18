from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .forms.add_profile_user import AddProfileUser, ChoseProductUser
from .models import ProfileUser, UserFood


class ProfileFormView(CreateView):
    template_name = "profile_user.html"

    def get(self, request, *args, **kwargs):
        user_current_name = ProfileUser.objects.filter(username__username=request.user.username)
        user_product_history = UserFood.objects.filter(username__username=request.user.username)
        user_chose_product = ChoseProductUser()
        person_form = AddProfileUser()
        context = {
            'person_form': person_form,
            'profile_current_user': user_current_name,
            'profile_product_user': user_product_history,
            'user_chose_product': user_chose_product,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = AddProfileUser(request.POST, request.FILES)
        if user_form.is_valid():
            profile = ProfileUser()
            profile.username_id = request.user.id
            profile.height = user_form.cleaned_data['height']
            profile.weight = user_form.cleaned_data['weight']
            profile.date_born = user_form.cleaned_data['date_born']
            profile.photo = user_form.cleaned_data['photo']
            profile.save()
            return HttpResponseRedirect('/profile/')
        else:
            return HttpResponseRedirect('/')
