from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor, Receta, Comentario
from .forms  import AutorForm, RecetaForm, ComentarioForm


def lista_recetas(request):
    recetas = Receta.objects.select_related('autor').all()
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})


def detalle_receta(request, pk):
    receta      = get_object_or_404(Receta, pk=pk)
    comentarios = receta.comentarios.all()
    form        = ComentarioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        c = form.save(commit=False)
        c.receta = receta
        c.save()
        return redirect('recetas:detalle', pk=pk)
    return render(request, 'recetas/detalle_receta.html', {
        'receta': receta, 'comentarios': comentarios, 'form': form
    })


def nueva_receta(request):
    form = RecetaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('recetas:lista')
    return render(request, 'recetas/form_receta.html', {'form': form, 'titulo': 'Nueva Receta'})


def editar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    form   = RecetaForm(request.POST or None, instance=receta)
    if form.is_valid():
        form.save()
        return redirect('recetas:detalle', pk=pk)
    return render(request, 'recetas/form_receta.html', {'form': form, 'titulo': 'Editar Receta'})


def eliminar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == 'POST':
        receta.delete()
        return redirect('recetas:lista')
    return render(request, 'recetas/confirmar_eliminar.html', {'objeto': receta})


def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'recetas/lista_autores.html', {'autores': autores})


def nuevo_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('recetas:autores')
    return render(request, 'recetas/form_autor.html', {'form': form})
