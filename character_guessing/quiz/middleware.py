from .models import Question

class QuestionViewsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if 'question_id' in request.session:
            question_id = request.session['question_id']
            question = Question.objects.get(pk=question_id)
            question.views += 1
            question.save()
        return response