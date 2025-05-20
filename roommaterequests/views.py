# accounts/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from roommaterequests.forms import RoommateRequestForm, RoommateRequestReviewForm
from .models import RoommateRequest
from django.views.generic import  UpdateView
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db import IntegrityError
from django.conf import settings


User = get_user_model()

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


    
def create_request_view(request, pk):
    receiver = get_object_or_404(User, pk=pk)
    if receiver:
        try:
            roommate_request = RoommateRequest.objects.create(
                    sender=request.user,
                    receiver=receiver,
                )
            roommate_request.save()
               
            messages.success(request, 'Roommate request created successfully!')
        except IntegrityError:
            messages.warning(request, 'A roommate request to this user already exists.')
    settings.LOGGER.info(f"Roommate request created from {request.user.username} to {receiver.username}")
    return redirect('profile_detail', pk=request.user.profile.pk)


@login_required
def roommate_request_review(request, pk):
    roommate_request = get_object_or_404(RoommateRequest, pk=pk)

    # Restrict access to only the receiver
    if request.user != roommate_request.receiver:
        return render(request, '403.html', status=403)

    questions = list(request.user.questions.all()[:3])
    questionnaire = []

    for i, question in enumerate(questions, 1):
        answer_qs = question.answers.filter(user=roommate_request.sender).first()
        answer = answer_qs.answer_text if answer_qs else "No answer provided"
        questionnaire.append({
            f'question': question.text,
            f'answer': answer,
        })

    if request.method == 'POST':
        form = RoommateRequestReviewForm(request.POST, instance=roommate_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Roommate request reviewed successfully!')
            return redirect('roommate_requests_index')
        else:
            messages.error(request, 'There was an error reviewing the request.')
            settings.LOGGER.warning(f"Error reviewing roommate request: {form.errors}")
    else:
        form = RoommateRequestReviewForm(instance=roommate_request)

    return render(request, 'requests/detail.html', {
        'form': form,
        'roommate_request': roommate_request,
        'questionnaire': questionnaire,
    })
    

def delete_request_view(request, pk):
    roommate_request = get_object_or_404(RoommateRequest, pk=pk)
    roommate_request.delete()
    messages.success(request, 'Roommate request deleted successfully!')
    return redirect('roommate_requests_index')
    