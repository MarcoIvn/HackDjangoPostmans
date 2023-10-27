from django.shortcuts import render
from app.models import *
import openai

def search_crimes(request):
    query = request.GET.get('query', '')  # Obtener la consulta del formulario

    # Clave de API a OpenAI
    api_key = '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'
    openai.api_key = api_key

    # Texto a pasar
    prompt = f"Convertir el texto '{query}' a una consulta SQL para buscar en la base de datos llamada 'Crimes' que tiene los campos: id,Año,Clave_Ent, Entidad, Bien_juridico_afectado, Tipo_de_delito, Subtipo_de_delito, Modalidad, Enero, Febrero, Marzo, Abril, Mayo, Junio, Agosto, Septiembre, Octubre, Noviembre, Diciembre. ."

    # Llamada a gpt-3
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )

    sql_query = response.choices[0].text.strip()
    print(sql_query)
    #results = Crime.objects.raw(sql_query)
    results = Crime.objects.all()
    return render(request, 'app/search.html', {'results': results})