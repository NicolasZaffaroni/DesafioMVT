from django.shortcuts import render


def Datos_papa(request):
    return  render ( request"papa.html"  {"nombre":"Jose Carlos","edad":"45", "fecha de nacimiento": "30/03/1997"} )

