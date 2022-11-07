from django.shortcuts import render
from django.http import HttpResponse


def Datos_papa(request):
    return  render( request, "Papa.html",{ "Nombre":"Jose Carlos Villalba","Edad":"45", "Fecha":"30/03/1977"} )

def Datos_mama(request):
    return  render( request, "Mama.html",{ "Nombre":"Estela Cruz","Edad":"40", "Fecha":"30/03/1982"} )



def Datos_hermano_mayor(request):
    return  render( request, "Hermanomaoyr.html",{ "Nombre":"German Cruz Villalba","Edad":"17", "Fecha":"30/03/2005"} )


def Datos_Perro(request):
    return  render( request, "Perro.html",{ "Nombre":"Kira Cruz Villalba","Edad":"3", "Fecha":"30/03/2019"} )







