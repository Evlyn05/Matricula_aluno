from django.shortcuts import render
from .forms import AlunoForm
from .models import Aluno

def cadastrar_aluno(request):

    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            data_nascimento = form.cleaned_data[' data_nascimento']
            cpf = form.cleaned_data['cpf']
            email = form.cleaned_data['email']
            curso = form.cleaned_data['curso']
           
            Aluno.objects.create(nome=nome, data_nascimento=data_nascimento, cpf=cpf, email=email,curso=curso,)
    else:
        print("->>>>>>>>>> entrou primeiro aqui")
        form = AlunoForm()

    return render(request, 'cadastrar_aluno.html', {'form': form})
