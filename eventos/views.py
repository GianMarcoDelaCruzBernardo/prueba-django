from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Evento, Usuario, RegistroEvento
from .forms import EventoForm, UsuarioForm, RegistroEventoForm


def lista_eventos(request):
    eventos = Evento.objects.all().select_related('organizador')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})


def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    registros = evento.registros.filter(estado='CONFIRMADO').select_related('usuario')
    return render(request, 'eventos/detalle_evento.html', {
        'evento': evento,
        'registros': registros,
        'total_registrados': registros.count(),
    })


def crear_evento(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_eventos')
    return render(request, 'eventos/form_evento.html', {'form': form, 'titulo': 'Crear Evento'})


def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    form = EventoForm(request.POST or None, instance=evento)
    if form.is_valid():
        form.save()
        return redirect('detalle_evento', pk=pk)
    return render(request, 'eventos/form_evento.html', {'form': form, 'titulo': 'Editar Evento'})


def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    return render(request, 'eventos/confirmar_eliminar.html', {'objeto': evento, 'tipo': 'evento'})


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'eventos/lista_usuarios.html', {'usuarios': usuarios})


def crear_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
    return render(request, 'eventos/form_usuario.html', {'form': form})


def registrar_usuario(request):
    form = RegistroEventoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_eventos')
    return render(request, 'eventos/form_registro.html', {'form': form})


def eliminar_registro(request, pk):
    registro = get_object_or_404(RegistroEvento, pk=pk)
    if request.method == 'POST':
        evento_pk = registro.evento.pk
        registro.delete()
        return redirect('detalle_evento', pk=evento_pk)
    return render(request, 'eventos/confirmar_eliminar.html', {'objeto': registro, 'tipo': 'registro'})


def consultas_avanzadas(request):
    from django.db.models import Count
    ahora = timezone.now()

    eventos_con_conteo = Evento.objects.annotate(
        total_usuarios=Count('registros')
    ).order_by('-total_usuarios')

    eventos_este_mes = Evento.objects.filter(
        fecha_inicio__year=ahora.year,
        fecha_inicio__month=ahora.month
    ).count()

    usuarios_activos = Usuario.objects.annotate(
        total_registros=Count('registros')
    ).order_by('-total_registros')[:5]

    eventos_por_organizador = Usuario.objects.annotate(
        eventos_organizados_count=Count('eventos_organizados')
    ).order_by('-eventos_organizados_count')

    return render(request, 'eventos/consultas.html', {
        'eventos_con_conteo': eventos_con_conteo,
        'eventos_este_mes': eventos_este_mes,
        'usuarios_activos': usuarios_activos,
        'eventos_por_organizador': eventos_por_organizador,
    })
