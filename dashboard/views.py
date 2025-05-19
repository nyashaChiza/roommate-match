from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from accounts.forms import ProfileForm
from accounts.models import Profile
from django.shortcuts import get_object_or_404, render, redirect
from accounts.forms import ProfileForm
from django.contrib import messages
from roommaterequests.helpers import MatchService, get_user_match_score

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['form'] = ProfileForm()
          service = MatchService(user=self.request.user)
          context['roommates'] = service.get_ranked_matches(min_score=0.01)
          return context
    


def profile_view(request):
    if hasattr(request.user, 'profile'):
        return redirect('dashboard') 

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile created successfully!")
            return redirect('dashboard')  # Redirect after successful creation
    else:
        form = ProfileForm()

    return render(request, 'dashboard/index.html', {'form': form})

@login_required
def profile_detail_view(request, pk):
    profile = Profile.objects.get(pk=pk)
    profile = get_user_match_score(base_user=request.user, other_user=profile.user)
    return render(request, 'account/detail.html', {'profile': profile})