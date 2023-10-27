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
            "content": f"En django tengo un modelo 'Crimes', usando esto: Crimes.objects.filter(), dame la función con los parentesis rellenados en base a esta búsqueda: {query}, la tabla tiene los campos: id, Año, Clave_Ent, Entidad, Bien_juridico_afectado, Tipo_de_delito, Subtipo_de_delito, Modalidad, Enero, Febrero, Marzo, Abril, Mayo, Junio, Agosto, Septiembre, Octubre, Noviembre, Diciembre. Los campos de 'Enero' a 'Diciembre' indican el numero de delitos ocurridos en ese mes. Mandame unicamente lo que iria en el parentesis de la funcion, no mandes ninguna explicacion, ya que la respuesta que mandes sera usada en código. Además, cualquier string debe iniciar con mayúscula."
        },
        {
            "role": "user",
            "content": "Hello!"
        }
      ]
    }

    response = requests.post(openai_url, headers=headers, json=data)
   
    results = response.json()['choices'][0]['message']['content']
    print(results)

    queryCode = None 
    try:
        queryCode = eval(results)
    except Exception as e:
        print(f"Error al ejecutar el código: {e}")
    return render(request, 'app/search.html', {'query': queryCode})