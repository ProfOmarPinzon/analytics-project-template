"""Fixtures compartidos para todos los tests del proyecto."""

from pathlib import Path

import pytest


@pytest.fixture
def project_root() -> Path:
    """Raíz del repositorio."""
    return Path(__file__).parent.parent


@pytest.fixture
def data_raw(project_root: Path) -> Path:
    """Directorio data/raw/ — datos originales sin modificar."""
    return project_root / "data" / "raw"


@pytest.fixture
def data_processed(project_root: Path) -> Path:
    """Directorio data/processed/ — datos transformados listos para modelado."""
    return project_root / "data" / "processed"


@pytest.fixture
def models_dir(project_root: Path) -> Path:
    """Directorio models/ — pipelines serializados con joblib."""
    return project_root / "models"
