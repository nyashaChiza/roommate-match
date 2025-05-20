from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm  # assume we have these forms
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required

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


# Create Answer
class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'answer_create.html'
    success_url = reverse_lazy('answer_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# List Answers
class AnswerListView(LoginRequiredMixin, ListView):
    model = Answer
    context_object_name = 'answers'
    template_name = 'answer_list.html'

    def get_queryset(self):
        return Answer.objects.filter(user=self.request.user)
