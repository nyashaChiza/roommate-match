from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from roommaterequests.models import RoommateRequest
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm  # assume we have these forms
from django.shortcuts import get_object_or_404, render, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.conf import settings    
from roommaterequests.forms import RoommateRequestReviewForm
from django.contrib.auth import get_user_model


User = get_user_model()

@login_required
def add_profile_questions(request):
    QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=3, max_num=3, validate_max=True)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, queryset=Question.objects.none())
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
            return redirect('profile')  # or wherever you want to redirect
    else:
        formset = QuestionFormSet(queryset=Question.objects.none())

    return render(request, 'questionaire/create.html', {'formset': formset})


# List Questions
class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'questionaire/question_list.html'

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)




@login_required
def answer_questions_for_profile(request, pk):
    # The profile whose questions will be answered
    user = get_object_or_404(User, pk=pk)

    # Prevent answering own questions
    if user == request.user:
        return render(request, '403.html', status=403)

    # Fetch the first 3 questions from the profile
    questions = list(user.questions.all()[:3])
    questionnaire = []

    for question in questions:
        existing_answer = question.answers.filter(user=request.user).first()
        questionnaire.append({
            "question": question.text,
            "answer": existing_answer.answer_text if existing_answer else "",
            "question_id": question.id
        })

    if request.method == 'POST':
        for question in questions:
            answer_text = request.POST.get(f'answer_{question.id}', '').strip()
            if answer_text:
                Answer.objects.update_or_create(
                    user=request.user,
                    question=question,
                    defaults={'answer_text': answer_text}
                )
        # Optionally, you can also create a RoommateRequest here
        roommate_request = RoommateRequest.objects.create(
            sender=request.user,
            receiver=user,
        )
        roommate_request.save()
        messages.success(request, "Your answers have been submitted.")
        return redirect('profile_detail', pk=user.profile.pk)

    return render(request, 'que/answer_form.html', {
        'profile': user,
        'questions': questions,
        'questionnaire': questionnaire,
    })


# List Answers
class AnswerListView(LoginRequiredMixin, ListView):
    model = Answer
    context_object_name = 'answers'
    template_name = 'answer_list.html'

    def get_queryset(self):
        return Answer.objects.filter(user=self.request.user)
