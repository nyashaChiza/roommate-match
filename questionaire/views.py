from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm  # assume we have these forms

# Create Question
class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'questionaire/create.html'
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
