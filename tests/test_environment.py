"""Verifica que el ambiente de desarrollo está configurado correctamente.

Este test corre en CI desde la semana 1. Si pasa, el ambiente está listo.
No modifiques este archivo — es la línea de base del proyecto.
"""

from pathlib import Path


def test_dependencias_principales():
    """Las librerías del curso están instaladas con versiones mínimas."""
    import pandas as pd
    import pandera  # noqa: F401
    import sklearn

    assert tuple(int(x) for x in pd.__version__.split(".")[:2]) >= (2, 2), (
        f"pandas >= 2.2 requerido, instalado: {pd.__version__}"
    )
    assert tuple(int(x) for x in sklearn.__version__.split(".")[:2]) >= (1, 4), (
        f"scikit-learn >= 1.4 requerido, instalado: {sklearn.__version__}"
    )


def test_estructura_del_proyecto():
    """Los directorios del proyecto existen."""
    root = Path(__file__).parent.parent
    directorios = [
        root / "src" / "analytics",
        root / "tests",
        root / "data" / "raw",
        root / "data" / "processed",
        root / "models",
        root / "notebooks",
    ]
    for directorio in directorios:
        assert directorio.exists(), f"Directorio faltante: {directorio}"


def test_paquete_importable():
    """El paquete analytics es importable desde src/."""
    import analytics  # noqa: F401
