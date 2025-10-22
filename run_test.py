from datetime import datetime
import pytest
import os

# Crear carpeta "reportes" si no existe
os.makedirs("reportes", exist_ok=True)

# Generar nombre único con fecha y hora (válido para Windows)
fecha_hora = datetime.now().strftime("%d-%m-%y_%H.%M.%S")
reporte_nombre = f"report_{fecha_hora}.html"
ruta_reporte = os.path.join("reportes", reporte_nombre)

# Lista de pruebas a ejecutar
test_cases = [
    "test/test_login.py",
    "test/test_inventory.py"
]

# Argumentos de pytest con el nombre dinámico del reporte
pytest_args = test_cases + [
    f"--html={ruta_reporte}",
    "--self-contained-html",
    "-v"
]

# Ejecutar pytest
pytest.main(pytest_args)
