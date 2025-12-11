# 🚀 Proyecto de Automatización QA -- SauceDemo

Automatización **UI + API** utilizando **Selenium, Pytest y Requests**.

## 📌 Descripción del Proyecto

Este proyecto forma parte del trabajo final del curso **Tester QA
Automation**.\
El objetivo es automatizar pruebas funcionales sobre el sitio\
**https://www.saucedemo.com**, aplicando buenas prácticas y simulando
escenarios reales de uso.

Las pruebas cubren login, inventario, carrito de compras y
automatización de API con **Reqres**.\
El proyecto está desarrollado en **Python**, estructurado bajo **Page
Object Model (POM)** y cuenta con generación automática de reportes,
logs y capturas de pantalla.

------------------------------------------------------------------------

## 🎯 Objetivos

-   Validar el correcto funcionamiento del **login**.\
-   Verificar la redirección al **home** luego de iniciar sesión.\
-   Probar el comportamiento del **carrito de compras**.\
-   Ejecutar pruebas automatizadas de **API REST**.\
-   Generar reportes HTML, logs y evidencias.\
-   Mantener un proyecto escalable y con arquitectura profesional.

------------------------------------------------------------------------

## 🛠 Tecnologías Utilizadas

-   Python 3.x\
-   Selenium WebDriver\
-   Pytest\
-   Requests\
-   Faker\
-   CSV / JSON\
-   Logging nativo de Python

------------------------------------------------------------------------

## 📁 Arquitectura del Proyecto (POM)

    📦 Proyecto-Automation
     ┣ 📂 datos
     ┃ ┣ datos_usuarioValido.csv
     ┃ ┗ productos.json
     ┣ 📂 logs
     ┃ ┗ suite.log
     ┣ 📂 pages
     ┣ 📂 reports
     ┃ ┣ 📂 historial_report
     ┃ ┗ 📂 screenshots
     ┣ 📂 tests
     ┣ 📂 utils
     ┣ 📂 .github
     ┃ ┗ 📂 workflows
     ┃   ┗ ci.yml
     ┣ conftest.py
     ┣ run_test.py
     ┗ README.md

------------------------------------------------------------------------

## 📊 Reportes, Logs y Capturas

### ✔ Reportes HTML automáticos

Cada ejecución genera un reporte nuevo dentro de:

    reports/historial_report/

Formato:

    report_YYYY-MM-DD_HH-MM-SS.html

### ✔ Log de ejecución

    logs/suite.log

### ✔ Capturas de pantalla

    reports/screenshots/

------------------------------------------------------------------------

## ⚙️ Configuración para pruebas de API (Reqres)

1.  Registrate en **https://reqres.in** y obtené tu **API Key**.\
2.  Reemplazá tu clave en `conftest.py`:

``` python
@pytest.fixture
def header_request():
    return {"Authorization": "Bearer TU_API_KEY_AQUI"}
```

3.  Eliminá la etiqueta:

``` python
@pytest.mark.skip(reason="Solo para pruebas de API")
```

en cada prueba del archivo:

    tests/test_api_request.py

------------------------------------------------------------------------

## ▶️ Cómo ejecutar el proyecto

### 1️⃣ Instalar dependencias

    pip install -r requirements.txt

### 2️⃣ Ejecutar todas las pruebas

    python run_test.py

------------------------------------------------------------------------

## 🧪 Pruebas incluidas

### 🔹 UI --- Login

-   Login exitoso\
-   Login fallido\
-   Login utilizando Faker

### 🔹 UI --- Inventario / Carrito

-   Validación de productos\
-   Agregar y eliminar productos\
-   Validación del contador del carrito

### 🔹 API --- Reqres

-   GET Users\
-   POST Create User\
-   DELETE User\
-   Validación de códigos de estado y estructura JSON

------------------------------------------------------------------------

## 📦 Manejo de Datos Externos

-   `datos_usuarioValido.csv`\
-   `productos.json`

------------------------------------------------------------------------

## ✔ Conclusión

Este proyecto implementa conceptos fundamentales y avanzados de
automatización QA, aplicando buenas prácticas y una arquitectura
profesional basada en POM, generando reportes completos y permitiendo
escalabilidad para futuras mejoras.
