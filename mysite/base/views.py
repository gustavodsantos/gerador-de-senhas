import random
import string

from django.shortcuts import render

app_name = 'base'


def gerador_senha(request):
    # Define os critérios padrão
    comprimento = int(request.GET.get('length', 12))  # Comprimento padrão
    caracteres = string.ascii_lowercase  # Letras minúsculas

    if request.GET.get('uppercase'):
        caracteres += string.ascii_uppercase
    if request.GET.get('numbers'):
        caracteres += string.digits
    if request.GET.get('special'):
        caracteres += string.punctuation

    # Gerar senha
    senha = ''.join(random.choices(caracteres, k=comprimento))

    return render(request, 'base/gerador_senha.html', {'senha': senha})
