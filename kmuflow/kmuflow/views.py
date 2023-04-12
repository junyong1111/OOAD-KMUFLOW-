from django.shortcuts import render
from django.http import HttpResponse
import requests
import openai

OPENAI_API_KEY = "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"
YOUR_ORG_ID = "org-XCtzChIw6qhPLKieEBLSQhka"

openai.api_key = OPENAI_API_KEY
openai.organization = YOUR_ORG_ID
model = "gpt-3.5-turbo"

# Create your views here.

def index(request):
    return HttpResponse("안녕하세요 kmuflow에 오신것을 환영합니다.")



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

