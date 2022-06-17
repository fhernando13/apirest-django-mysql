from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Persona
import json


# Create your views here.

class PersonaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            personas=list(Persona.objects.filter(id=id).values())
            if len(personas) > 0 :
                persona=personas[0]
                datos= {'Message':'Success', 'persona':persona}
            else:
                datos= {'Message':'Not found!!'}
            return JsonResponse(datos)
        else:
            personas=list(Persona.objects.values())
            if len(personas) > 0:
                datos={'Message':'Success', 'Personas':personas}
            else:
                datos= {'Message':'Not found!!'}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Persona.objects.create(nombre =jd['nombre'], apellido=jd['apellido'], edad=jd['edad'],email=jd['email'])
        datos= {'Message':'Persona insertada'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        personas=list(Persona.objects.filter(id=id).values())
        if len(personas) > 0 :
            persona=Persona.objects.get(id=id)
            persona.nombre =jd['nombre']
            persona.apellido=jd['apellido']
            persona.edad=jd['edad']
            persona.email=jd['email']
            persona.save()
            datos= {'Message':'Persona actualizada'}
        else:
            datos= {'Message':'Not found!!'}
        return JsonResponse(datos)

    def delete(self, request, id):
        personas=list(Persona.objects.filter(id=id).values())
        if len(personas) > 0 :
            Persona.objects.filter(id=id).delete()
            datos= {'Message':'Persona eliminada'}
        else:
            datos= {'Message':'Not found!!'}
        return JsonResponse(datos)