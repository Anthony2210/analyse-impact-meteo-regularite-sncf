import math
import re
import textwrap
import unicodedata
from typing import Iterable

import numpy as np
import pandas as pd

from config import (
    DISPLAY_MODE_NAMES,
    DISPLAY_REGION_NAMES,
    FIGURES_DIR,
    PROCESSED_DIR,
    RAW_DIR,
    SNCF_REGION_ALIASES,
    WEATHER_REGION_DIR,
)


def ensure_directories() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    WEATHER_REGION_DIR.mkdir(parents=True, exist_ok=True)


def normalize_text(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    ascii_text = text.encode("ascii", "ignore").decode("ascii")
    ascii_text = ascii_text.replace("-", " ").replace("'", " ").replace("/", " ").replace("?", " ")
    return " ".join(ascii_text.split()).lower()


def normalize_columns(columns: Iterable[str]) -> list[str]:
    return [normalize_text(column).replace(" ", "_") for column in columns]


def to_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def weighted_average(values: pd.Series, weights: pd.Series) -> float:
    mask = values.notna() & weights.notna()
    if not mask.any():
        return math.nan
    return float(np.average(values[mask], weights=weights[mask]))


def add_monthly_gap(df: pd.DataFrame, value_col: str, group_cols: list[str] | None = None) -> pd.Series:
    group_cols = list(group_cols or [])
    grouping = group_cols + ["month"] if group_cols else ["month"]
    baseline = df.groupby(grouping)[value_col].transform("mean")
    return df[value_col] - baseline


def zscore_by_region_month(series: pd.Series) -> pd.Series:
    std = float(series.std(ddof=0))
    if math.isclose(std, 0.0) or np.isnan(std):
        return pd.Series(np.zeros(len(series)), index=series.index)
    return (series - float(series.mean())) / std


def shorten_comment(text: object, width: int = 140) -> str:
    if pd.isna(text) or not str(text).strip():
        return "Pas de commentaire SNCF disponible."
    clean = " ".join(str(text).split())
    return textwrap.shorten(clean, width=width, placeholder="...")


def clean_uic(value: object) -> str | None:
    text = str(value or "").strip()
    if not text or text.lower() == "nan":
        return None
    digits = re.sub(r"\D", "", text)
    return digits or None


def extract_department_code_from_commune(value: object) -> str | None:
    text = str(value or "").strip().upper().replace(" ", "")
    if not text or text == "NAN":
        return None
    if text.startswith(("97", "98")):
        return text[:3]
    if text.startswith(("2A", "2B")):
        return text[:2]
    if text.startswith("20"):
        return "20"
    return text[:2]


def extract_department_code_from_postal(value: object) -> str | None:
    text = re.sub(r"\D", "", str(value or ""))
    if not text:
        return None
    if len(text) >= 5 and text.startswith("20"):
        return "20"
    if text.startswith(("97", "98")):
        return text[:3]
    return text[:2]


def slugify(value: object) -> str:
    return normalize_text(value).replace(" ", "_")


def build_region_lookup(region_reference: pd.DataFrame) -> dict:
    lookup = {
        normalize_text(region_name): region_name
        for region_name in region_reference["region_current"].dropna().unique()
    }
    lookup.update({normalize_text(old): new for old, new in SNCF_REGION_ALIASES.items()})
    return lookup


CANONICAL_REGION_BY_NORMALIZED = {
    normalize_text(display_name): key for key, display_name in DISPLAY_REGION_NAMES.items()
}
CANONICAL_REGION_BY_NORMALIZED.update({normalize_text(key): key for key in DISPLAY_REGION_NAMES})


def canonical_region(value: object) -> str:
    raw = str(value or "").strip()
    return CANONICAL_REGION_BY_NORMALIZED.get(normalize_text(raw), raw)


def display_region(value: object) -> str:
    key = canonical_region(value)
    return DISPLAY_REGION_NAMES.get(key, str(value))


def canonical_mode(value: object) -> str:
    raw = str(value or "").strip()
    normalized = normalize_text(raw)
    if normalized.startswith("intercit"):
        return "Intercites"
    if normalized == "ter":
        return "TER"
    if normalized == "transilien":
        return "Transilien"
    return raw


def display_mode(value: object) -> str:
    key = canonical_mode(value)
    return DISPLAY_MODE_NAMES.get(key, str(value))
