# accounts/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import RoommateRequest

@login_required
def roommate_requests_index(request):
    # Show requests received and sent by the user
    sent_requests = RoommateRequest.objects.filter(sender=request.user)
    received_requests = RoommateRequest.objects.filter(receiver=request.user)
    return render(request, 'requests/index.html', {
        'sent_requests': sent_requests,
        'received_requests': received_requests,
    })

@login_required
def roommate_request_detail(request, pk):
    request_obj = get_object_or_404(RoommateRequest, pk=pk)

    # Restrict view access to only the sender or receiver
    if request.user != request_obj.sender and request.user != request_obj.receiver:
        return render(request, '403.html', status=403)

    return render(request, 'requests/detail.html', {
        'request_obj': request_obj
    })
