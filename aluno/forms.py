from django import forms

class AlunoForm(forms.Form):
    nome = forms.CharField(max_length=200)
    data_nascimento = forms.DateField()
    cpf = forms.CharField(max_length=11)
    email = forms.EmailField(max_length=100)
    curso = forms.CharField(max_length=200)