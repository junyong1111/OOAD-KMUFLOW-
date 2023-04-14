from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Question
from .models import Answer
import requests
import openai


OPENAI_API_KEY = "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"
YOUR_ORG_ID = "org-XCtzChIw6qhPLKieEBLSQhka"

openai.api_key = OPENAI_API_KEY
openai.organization = YOUR_ORG_ID
model = "gpt-3.5-turbo"

# Create your views here.


def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content =request.POST.get('content'),
                               create_date = timezone.now())
    return redirect('kmuflow:detail', question_id=question_id)


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'kmuflow/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'kmuflow/question_detail.html', context)


def search(request):
    query = "취업 어떻게 해야해?"
    
    messages = [
        {"role": "system", "content": "You are a helpful computerscience."},
        {"role": "user", "content": query}
    ]
    
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages
    )   
    answer = response['choices'][0]['message']['content']
    return HttpResponse(answer)

