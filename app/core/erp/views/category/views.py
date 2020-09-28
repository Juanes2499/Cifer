from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from core.erp.models import *
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


def category_list(request):
    data = {
        'title': 'Listado de categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

#Listas basadas en clase
class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html' 
    #Se tiene que cambiar el for como object_list

    #def get_queryset(self):
    #    return Category.objects.filter(name__startswith='L')

    @method_decorator(csrf_exempt)
    #@method_decorator(login_required) #valida si un user esta logeado
    def dispatch(self, request, *args, **kwargs):
        #if request.method=='GET':
        #    return redirect('category_list2')
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = { }
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    #Sobre escibrimos los métodos que nos da esa vista para poder enviar un diccionario   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorías'
        return context

class CategoryCreateView(CreateView):
    model = Category
    #form_class