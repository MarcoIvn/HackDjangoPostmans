from django.shortcuts import render
from app.models import *
import openai
from django.http import JsonResponse
import requests


def search_crimes(request):
    query = request.GET.get('query', '') 
    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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",
    }
    # Datos de la solicitud
    data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": f"En django tengo un modelo 'Crime', usando esto: Crime.objects.filter(), dame lo que iría en los paréntesis de la función en base a esta búsqueda: {query}, la tabla tiene los campos: id, Año, Clave_Ent, Entidad, Bien_juridico_afectado, Tipo_de_delito, Subtipo_de_delito, Modalidad, Enero, Febrero, Marzo, Abril, Mayo, Junio, Agosto, Septiembre, Octubre, Noviembre, Diciembre. Mandame unicamente lo que va en el parentesis, no mandes ninguna explicacion de ningun tipo ni nada, ya que la respuesta que mandes sera usada en codigo"
        },
        {
            "role": "user",
            "content": "Hello!"
        }
      ]
    }

    response = requests.post(openai_url, headers=headers, json=data)
    print(response.json())
   
    #results = Crime.objects.raw(sql_query)
    results = Crime.objects.all()
    return render(request, 'app/search.html', {'results': results})