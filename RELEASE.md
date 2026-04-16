# Release Guide — Suma de números (CLI)

Este documento describe cómo **descargar, instalar y ejecutar** el proyecto
**suma_numeros** utilizando únicamente la información disponible en este repositorio.

El objetivo es que **cualquier usuario externo** pueda reproducir el funcionamiento
del software sin contacto con el autor.

---

## 1. Requisitos

- Python 3.10 o superior  
- Sistema operativo: Windows, macOS o Linux  
- Gestor de dependencias:
  - Recomendado: `uv`
  - Alternativo: `pip` + `venv`

---

## 2. Descargar el proyecto

### Opción A: Clonar desde GitHub

```bash
git clone https://github.com/<usuario>/<repositorio>.git
cd suma_numeros
```

### Opción B: Descargar como ZIP

1. Ir al repositorio en GitHub
2. Clic en **Code → Download ZIP**
3. Descomprimir el archivo
4. Entrar a la carpeta `suma_numeros`

---

## 3. Instalación

### Opción recomendada: usando `uv`

Si no tienes `uv`, consulta la documentación oficial:
https://docs.astral.sh/uv/

Desde la **raíz del proyecto** (directorio que contiene `pyproject.toml`):

```bash
uv sync
```

---

### Opción alternativa: usando `pip` y entorno virtual

#### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 4. Ejecución del programa

> **Importante**  
> Todos los comandos deben ejecutarse desde la **raíz del proyecto**
> (`suma_numeros/`), es decir, el directorio que contiene el archivo
> `pyproject.toml`.  
> No se debe ejecutar el programa desde la carpeta `src/`.

El programa se ejecuta como **módulo de Python**, respetando la estructura `src/`.

### Ejemplo con enteros

```bash
uv run python main.py -n 1 2 3 4
```

Salida esperada:
```
10.0
```

### Ejemplo con flotantes

```bash
uv run python main.py -n 0.5 1.25
```

Salida esperada:
```
1.75
```

---

## 5. Manejo de errores

Si se proporcionan valores inválidos:

```bash
uv run python main.py -n 1 a 3
```

Salida esperada (stderr):
```
Solo se aceptan enteros y flotantes.
```

El programa termina con un código de salida distinto de 0.

---

## 6. Ejecución de pruebas automatizadas

Las pruebas están implementadas con `pytest` y se encuentran en la carpeta `tests/`.

Ejecutar desde la **raíz del proyecto**:

```bash
pytest   # o bien   uv run pytest
```

Todas las pruebas deben pasar para considerar el software correctamente liberado.

---

## 7. Estructura del proyecto

```text
suma_numeros/
├── README.md            # Documento de contexto
├── RELEASE.md           # Guía de liberación (este archivo)
├── LICENSE              # Licencia de uso
├── casos_prueba.md      # Casos de prueba en lenguaje natural
├── pyproject.toml       # Configuración y dependencias
│── main.py              # Implementación del programa
└── test_main.py         # Pruebas automatizadas
```

---

## 8. Licencia

Este proyecto se distribuye bajo la licencia indicada en el archivo `LICENSE`.
Consulta dicho archivo para conocer los términos de uso, modificación y distribución.


