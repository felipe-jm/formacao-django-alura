from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
  """Cadastra uma nova pessoa no sistema"""
  if request.method == 'POST':
    nome = request.POST['nome']
    email = request.POST['email']
    senha = request.POST['password']
    senha2 = request.POST['password2']
    if campo_vazio(nome):
      messages.error(request, 'O nome não pode ficar em branco!')
      return redirect('cadastro')
    if campo_vazio(email):
      messages.error(request, 'O email não pode ficar em branco!')
      return redirect('cadastro')
    if senha != senha2:
      messages.error(request, 'As senhas não são iguais!')
      return redirect('cadastro')
    if User.objects.filter(email=email).exists():
      messages.error(request, 'Usuário já cadastrado!')
      return redirect('cadastro')
    if User.objects.filter(username=nome).exists():
      messages.error(request, 'Usuário já cadastrado!')
      return redirect('cadastro')
    user = User.objects.create_user(
      email=email,
      password=senha,
      username=nome
    )
    user.save('Cadastro realizado com sucesso!')
    messages.success(request, 'As senhas não são iguais!')
    return redirect('login')
  else:
    return render(request, 'usuarios/cadastro.html')

def login(request):
  """Logga o usuário"""
  if request.method == 'POST':
    email = request.POST['email']
    senha = request.POST['senha']
    if campo_vazio(email) or campo_vazio(senha):
      messages.error(request, 'Os campos email e senha não podem ficar em branco')
      return redirect('login')
    if User.objects.filter(email=email).exists():
      nome = User.objects.filter(email=email).values_list('username', flat=True).get()
      user = auth.authenticate(request, username=nome, password=senha)
      if user is not None:
        auth.login(request, user)
    return redirect('dashboard')
  return render(request, 'usuarios/login.html')

def logout(request):
  """Deslogga o usuário"""
  auth.logout(request)
  return redirect('index')

def dashboard(request):
  """Retorna os dados do dashboard"""
  if request.user.is_authenticated:
    receitas = Receita.objects.order_by('-data_receita').filter(pessoa=request.user.id)
    dados = {
      'receitas': receitas
    }
    return render(request, 'usuarios/dashboard.html', context=dados)
  return redirect('index')

def campo_vazio(campo):
  """Verifica se um campo está vazio"""
  return not campo.strip()
