from django.shortcuts import get_object_or_404
from .models import Journal

class QuizStatsMixin:
    def get_quiz_stats(self):
        user = self.request.user
        journal = get_object_or_404(Journal, user=user)
        return {
            'total_tests': journal.total_tests,
            'total_correct_answers': journal.correct_answers,
            'total_incorrect_answers': journal.incorrect_answers
        }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            journal = get_object_or_404(Journal, user=user)
            context['quiz_stats'] = {
                'total_tests': journal.total_tests,
                'total_correct_answers': journal.correct_answers,
                'total_incorrect_answers': journal.incorrect_answers
            }
        return context
