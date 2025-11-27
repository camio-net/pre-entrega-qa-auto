import requests
import pytest

#Obtener usuarios de la API
def test_get_users(url_base,header_request):
    response = requests.get(f"{url_base}/2", headers=header_request)
    
    #Validacion de status code y contenido
    assert response.status_code == 200
    data = response.json()
    
    assert data["data"]["id"] == 2


#Crear un nuevo usuario
def test_create_user(url_base,header_request):
    payload = {
        "name": "Damian",
        "job": "Tester Auto"
    }
    response = requests.post(url_base, json=payload, headers=header_request)
    
    #Validacion de status code y contenido
    assert response.status_code == 201
    data = response.json()
    
    #Validar que los datos enviados son correctos
    assert data["name"] == "Damian"
    assert data["job"] == "Tester Auto"


#Eliminar un usuario
def test_delete_user(url_base,header_request):
    response = requests.delete(f"{url_base}/2", headers=header_request)
    
    #Validacion de status code
    assert response.status_code == 204
    