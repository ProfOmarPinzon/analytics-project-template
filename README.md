# Analytics Project — Analítica de Datos, UPB

Repositorio del semestre para el curso **Analítica de Datos**.
Cada laboratorio agrega un módulo Python a `src/analytics/`.
Al final del semestre tienes un producto de software — no una colección de notebooks.

## Inicio rápido

```bash
# 1. Clonar el repositorio (o hacer fork desde GitHub Classroom)
git clone <URL-del-repositorio>
cd analytics-project

# 2. Instalar uv (si no lo tienes)
pip install uv

# 3. Crear entorno e instalar dependencias
uv sync --all-groups

# 4. Verificar que todo está en orden
uv run pytest

# 5. Verificar calidad de código
uv run ruff check .
uv run ruff format --check .
```

Si los tres comandos pasan, el ambiente está listo.

## Estructura del proyecto

```
analytics-project/
├── pyproject.toml              # Configuración del proyecto (uv, ruff, pytest)
├── .python-version             # Versión de Python fijada (3.12)
├── .github/workflows/ci.yml   # CI: corre ruff + pytest en cada push
│
├── src/analytics/              # Código de producción — testeado y reutilizable
│   ├── __init__.py
│   ├── extract.py              # Lab 2: ingesta de datos (CSV, APIs, BD)
│   ├── quality.py              # Lab 2: validación de schemas con pandera
│   ├── transform.py            # Lab 3: transformaciones reproducibles
│   ├── eda.py                  # Lab 3: funciones de exploración
│   ├── train.py                # Lab 4: sklearn Pipeline completo
│   ├── evaluate.py             # Lab 4: métricas y reporte de evaluación
│   ├── segment.py              # Lab 5: clustering y reducción de dimensionalidad
│   ├── pipeline.py             # Lab 6: pipeline end-to-end
│   └── api.py                  # Lab 6: endpoint FastAPI para inferencia
│
├── tests/                      # Pruebas unitarias — deben pasar en CI
│   ├── conftest.py             # Fixtures compartidos
│   ├── test_environment.py     # Verifica el ambiente (no modificar)
│   ├── test_extract.py         # Lab 2
│   ├── test_quality.py         # Lab 2
│   ├── test_transform.py       # Lab 3
│   ├── test_train.py           # Lab 4
│   └── test_segment.py         # Lab 5
│
├── notebooks/                  # Solo exploración — nunca van a producción
│   ├── 01-eda-olist.ipynb      # Lab 3
│   └── 02-segmentacion.ipynb   # Lab 5
│
├── data/
│   ├── raw/                    # Datos originales — NO modificar, NO versionar
│   └── processed/              # Datos transformados — NO versionar
│
└── models/                     # Pipelines serializados con joblib
```

## Reglas del proyecto

| Regla | Razón |
|-------|-------|
| `data/` **nunca** va en Git | Los CSV de Olist son 45 MB — usa la carpeta compartida del curso |
| Los notebooks son desechables | La lógica reutilizable va en módulos Python con tests |
| Un lab que no pasa CI no está entregado | "Funciona en mi máquina" no es criterio de entrega |
| Commits frecuentes con mensajes descriptivos | El historial de Git es parte de la evaluación |

## Comandos útiles

```bash
# Ejecutar todos los tests
uv run pytest

# Ejecutar tests de un módulo específico
uv run pytest tests/test_extract.py -v

# Ver cobertura de tests
uv run pytest --cov=analytics --cov-report=term-missing

# Corregir formato automáticamente
uv run ruff format .

# Ver errores de lint
uv run ruff check .

# Corregir errores de lint automáticamente (cuando es posible)
uv run ruff check --fix .

# Abrir Jupyter
uv run jupyter notebook notebooks/
```

## Módulos del semestre

| Lab | Módulo | Qué construyes |
|-----|--------|----------------|
| 1 | `pyproject.toml` + CI | Setup del proyecto y ambiente |
| 2 | `extract.py` + `quality.py` | Ingesta y validación del dataset Olist |
| 3 | `transform.py` + `eda.py` | Transformaciones y análisis exploratorio |
| 4 | `train.py` + `evaluate.py` | Pipeline de modelado supervisado |
| 5 | `segment.py` | Segmentación de clientes con clustering |
| 6 | `pipeline.py` + `api.py` | Orquestación y endpoint de inferencia |

## Dataset

El curso usa el dataset **Olist Brazilian E-commerce** durante todo el semestre.
Descárgalo desde el enlace del campus virtual y coloca los CSV en `data/raw/`.

No lo agregues a Git — ya está en `.gitignore`.
