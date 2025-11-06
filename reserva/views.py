from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Reserva, Mesa
from .forms import ReservaForm

# ------------------------
# Páginas abertas a qualquer usuário
# ------------------------
def fazer_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva enviada com sucesso! Aguarde confirmação.')
            return redirect('fazer_reserva')
    else:
        form = ReservaForm()
    return render(request, 'fazer_reserva.html', {'form': form})

def minhas_reservas(request):
    reservas = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        reservas = Reserva.objects.filter(nome__iexact=nome, email__iexact=email)
        if not reservas.exists():
            messages.warning(request, "Nenhuma reserva encontrada com essas informações.")
    return render(request, 'minhas_reservas.html', {'reservas': reservas})

# ------------------------
# Login/Logout
# ------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:  # só permite staff
                login(request, user)
                return redirect('lista_reservas')
            else:
                messages.error(request, "Você não tem permissão para acessar o painel.")
        else:
            messages.error(request, "Usuário ou senha incorretos")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# ------------------------
# Páginas do painel (só staff)
# ------------------------
@staff_member_required
def lista_reservas(request):        
    hoje = timezone.now().date()
    reservas_futuras = Reserva.objects.filter(data__gte=hoje).order_by('data', 'hora')
    reservas_passadas = Reserva.objects.filter(data__lt=hoje).order_by('-data', 'hora')
    
    return render(request, 'lista_reserva.html', {
        'reservas_futuras': reservas_futuras,
        'reservas_passadas': reservas_passadas
    })
    
@staff_member_required
def atualizar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva atualizada!')
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'editar_reserva.html', {'form': form})

@staff_member_required
def alterar_status(request, id, novo_status):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.status = novo_status
    reserva.save()
    messages.success(request, f"Status da reserva de {reserva.nome} alterado para {novo_status}.")
    return redirect('lista_reservas')

@staff_member_required
def deletar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    messages.success(request, 'Reserva removida.')
    return redirect('lista_reservas')

# ------------------------
# Páginas do painel (só staff)
# ------------------------
@staff_member_required
def fazer_reserva_admin(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.status = 'Confirmada'  # já confirma no momento do cadastro
            reserva.save()
            messages.success(request, f"Reserva de {reserva.nome} cadastrada com sucesso!")
            return redirect('lista_reservas')
    else:
        form = ReservaForm()

    return render(request, 'fazer_reserva_admin.html', {'form': form})

# ------------------------
# Locação de Mesas
# ------------------------  

@staff_member_required
def lista_mesas(request):
    hoje = timezone.localdate()  # data atual
    mesas = Mesa.objects.all()

    # reservas confirmadas do dia atual
    reservas = Reserva.objects.filter(
        data=hoje,
        status='Confirmada'
    ).order_by('hora')

    return render(request, "locacao_mesas.html", {"mesas": mesas, "reservas": reservas, "now": timezone.now()})


@staff_member_required
def alterar_status_mesa(request, id):
    mesa = get_object_or_404(Mesa, id=id)

    if request.method == 'POST':
        reserva_id = request.POST.get('reserva')

        # se uma reserva for selecionada → ocupar mesa
        if reserva_id:
            reserva = get_object_or_404(Reserva, id=reserva_id)
            mesa.reserva = reserva
            mesa.status = 'Ocupada'
            messages.success(request, f"Mesa {mesa.numero} ocupada por {reserva.nome}.")
        else:
            # se não houver reserva → liberar mesa
            mesa.reserva = None
            mesa.status = 'Disponível'
            messages.info(request, f"Mesa {mesa.numero} foi liberada.")

        mesa.save()

    return redirect('locacao_mesas')
