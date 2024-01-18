from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import Question
from .mixins import QuizStatsMixin
from .forms import AddQuestionForm

class QuizView(QuizStatsMixin, View):
    def get(self, request):
        question = self.get_random_question()
        request.session['question_id'] = question.id
        question.views += 1
        question.save()
        return render(request, 'quiz/quiz.html', {'question': question, 'stats': self.get_quiz_stats()})

    def post(self, request):
        question_id = request.POST.get('question_id')
        user = request.user
        question = Question.objects.get(pk=question_id)

        if 'like' in request.POST:
            liked = question.like_question(user)
        elif 'unlike' in request.POST:
            unliked = question.unlike_question(user)

        if 'submit_answer' in request.POST:
            user_answer = request.POST.get('user_answer')
            correct_answer = question.correct_answer
            if user_answer == correct_answer:
                request.user.journal.correct_answers += 1
            else:
                request.user.journal.incorrect_answers += 1

            request.user.journal.total_tests += 1
            request.user.journal.save()
        return redirect('quiz')

    def get_random_question(self):
        return random.choice(Question.objects.all())

class UserProfileView(LoginRequiredMixin, QuizStatsMixin, View):
    def get(self, request):
        return render(request, 'quiz/profile.html', {'stats': self.get_quiz_stats()})

class AddQuestionView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddQuestionForm()
        return render(request, 'quiz/add_question.html', {'form': form})

    def post(self, request):
        form = AddQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save()
            question.likes.add(request.user)
            return redirect('quiz')
        return render(request, 'quiz/add_question.html', {'form': form})

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'quiz/change_password.html'
    success_url = reverse_lazy('profile')
