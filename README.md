# 🚀 Proyecto de Automatización QA -- SauceDemo

Automatización UI + API con Selenium, Pytest y Requests

## 📌 Descripción del Proyecto

Este proyecto forma parte del trabajo final del curso **Tester QA
Automation**.\
El objetivo es automatizar pruebas funcionales sobre el sitio
**https://www.saucedemo.com**, aplicando buenas prácticas y simulando
situaciones reales de un usuario final.

Las pruebas incluyen flujos completos de login, interacción con
inventario, carrito de compras y automatización de API utilizando
**Reqres**.

El proyecto está desarrollado en **Python**, estructurado bajo el patrón
**Page Object Model (POM)** y con generación automática de reportes,
logs y capturas de pantalla.

## 🎯 Objetivos

-   Validar el correcto funcionamiento del **login**.\
-   Verificar la redirección a la página principal luego de iniciar
    sesión.\
-   Probar el comportamiento del **carrito de compras**.\
-   Ejecutar pruebas automatizadas de **API REST**.\
-   Generar reportes HTML, logs y evidencias.\
-   Mantener un proyecto escalable y con arquitectura profesional.

## 🛠 Tecnologías Utilizadas

-   Python 3.x\
-   Selenium WebDriver\
-   Pytest\
-   Requests\
-   Faker\
-   CSV / JSON\
-   Logging nativo de Python

## 📁 Arquitectura del Proyecto (POM)

La estructura está basada en Page Object Model:

    📦 Proyecto-Automation
     ┣ 📂 datos
     ┃ ┣ datos_usuarioValido.csv
     ┃ ┗ productos.json
     ┣ 📂 logs
     ┃ ┗ suite.log
     ┣ 📂 pages
     ┣ 📂 reportes
     ┣ ┣ 📂 reportes_html (Historial de reportes por fecha y hora de finalizacion)
     ┣ ┗ 📂 screenshots
     ┣ 📂 tests
     ┣ 📂 utils
     ┣ conftest.py
     ┣ run_test.py
     ┣ report.html (Ultimo reporte realizado)
     ┗ README.md

## 📊 Reportes, Logs y Capturas

### ✔ Reportes HTML automáticos

Se genera un nuevo reporte en:

    reportes/reportes_html/

Formato:

    report_YYYY-MM-DD_HH-MM-SS.html

### ✔ Log de ejecución

    logs/suite.log

### ✔ Capturas de pantalla

    reportes/screenshots/

## ⚙️ Configuración para pruebas de API (Reqres)

1.  Registrate en https://reqres.in/ y obtené tu API Key.
2.  Reemplazá tu clave en `conftest.py`:

``` python
@pytest.fixture
def header_request():
    return {"Authorization": "Bearer TU_API_KEY_AQUI"}
```

3.  Descomentá en `run_test.py`:

``` python
# "test/test_api_request.py",
```

4.  Ejecutá:

```{=html}
<!-- -->
```
    python run_test.py

## ▶️ Cómo ejecutar el proyecto

### 1️⃣ Instalar dependencias

    pip install selenium pytest requests faker

### 2️⃣ Ejecutar todas las pruebas

    python run_test.py

## 🧪 Pruebas incluidas

### UI --- Login

-   Login exitoso\
-   Login fallido\
-   Login con Faker

### UI --- Inventario / Carrito

-   Validación de productos\
-   Agregar/eliminar productos\
-   Contador del carrito

### API --- Reqres

-   GET Users\
-   POST Create User\
-   DELETE User\
-   Validación de códigos y JSON

## 📦 Manejo de Datos Externos

-   `datos_usuarioValido.csv`\
-   `productos.json`

## ✔ Conclusión

Este proyecto aplica conceptos fundamentales y avanzados de
automatización QA con una arquitectura escalable y profesional.

python pip install -r requirements.txt