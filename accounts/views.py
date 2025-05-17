from django.shortcuts import get_object_or_404, render
from accounts.models import User
from django.views.generic import ListView
from django.contrib import messages
from django.shortcuts import redirect


class UserListView(ListView):
    model = User
    template_name = 'account/index.html'  # Specify your template name here
    context_object_name = 'users'  # This will be the context variable in the template

    def get_queryset(self):
        return User.objects.all()  # You can customize this queryset as needed
    
def user_delete_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('user_list')  # Redirect to the user list after deletion
    