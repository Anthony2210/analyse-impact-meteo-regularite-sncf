from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
FIGURES_DIR = PROJECT_DIR / "figures"
WEATHER_REGION_DIR = RAW_DIR / "open_meteo_daily_by_region"

TER_RAW_PATH = RAW_DIR / "sncf_ter_regularite_mensuelle.csv"
TRANSILIEN_RAW_PATH = RAW_DIR / "sncf_transilien_regularite_mensuelle.csv"
INTERCITES_RAW_PATH = RAW_DIR / "sncf_intercites_regularite_mensuelle.csv"
GARES_RAW_PATH = RAW_DIR / "sncf_gares_voyageurs.csv"
FREQUENTATION_RAW_PATH = RAW_DIR / "sncf_frequentation_gares.csv"
GEO_REGIONS_CACHE_PATH = RAW_DIR / "geo_api_current_regions_reference.csv"
GEO_DEPARTEMENTS_CACHE_PATH = RAW_DIR / "geo_api_departements_reference.csv"
WEATHER_CACHE_PATH = RAW_DIR / "open_meteo_daily_current_regions.csv"

TER_CLEAN_PATH = PROCESSED_DIR / "sncf_ter_regularite_mensuelle_clean.csv"
TER_MONTHLY_PATH = PROCESSED_DIR / "ter_current_regions_monthly.csv"
WEATHER_MONTHLY_PATH = PROCESSED_DIR / "weather_current_regions_monthly.csv"
TRANSILIEN_MONTHLY_PATH = PROCESSED_DIR / "transilien_monthly.csv"
INTERCITES_MONTHLY_PATH = PROCESSED_DIR / "intercites_monthly.csv"
MODE_COMPARISON_PATH = PROCESSED_DIR / "rail_mode_comparison_monthly.csv"
REGION_CONTEXT_PATH = PROCESSED_DIR / "rail_region_context.csv"
MERGED_PATH = PROCESSED_DIR / "ter_weather_current_regions_monthly.csv"
REGIONS_GEOJSON_PATH = RAW_DIR / "regions_2025_1000m.geojson"
REGIONS_GEOJSON_URL = "https://object.data.gouv.fr/contours-administratifs/2025/geojson/regions-1000m.geojson"

METRO_REGION_NAMES = {
    "Auvergne-Rhône-Alpes",
    "Bourgogne-Franche-Comté",
    "Bretagne",
    "Centre-Val de Loire",
    "Corse",
    "Grand Est",
    "Hauts-de-France",
    "Île-de-France",
    "Normandie",
    "Nouvelle-Aquitaine",
    "Occitanie",
    "Pays de la Loire",
    "Provence-Alpes-Côte d'Azur",
}

NUMERIC_TER_COLUMNS = [
    "nombre_de_trains_programmes",
    "nombre_de_trains_ayant_circule",
    "nombre_de_trains_annules",
    "nombre_de_trains_en_retard_a_l_arrivee",
    "taux_de_regularite",
]

NUMERIC_INTERCITES_COLUMNS = [
    "nombre_de_trains_programmes",
    "nombre_de_trains_ayant_circule",
    "nombre_de_trains_annules",
    "nombre_de_trains_en_retard_a_l_arrivee",
    "taux_de_regularite",
]

STRESS_COMPONENTS = {
    "heavy_rain_days": "Pluie forte",
    "very_heavy_rain_days": "Pluie très forte",
    "snow_days": "Neige",
    "strong_wind_days": "Vent fort",
    "heat_days": "Chaleur",
    "frost_days": "Gel",
    "storm_days": "Orage",
}

SNCF_REGION_ALIASES = {
    "Alsace": "Grand Est",
    "Lorraine": "Grand Est",
    "Champagne Ardenne": "Grand Est",
    "Aquitaine": "Nouvelle-Aquitaine",
    "Limousin": "Nouvelle-Aquitaine",
    "Poitou Charentes": "Nouvelle-Aquitaine",
    "Auvergne": "Auvergne-Rhône-Alpes",
    "Rhône Alpes": "Auvergne-Rhône-Alpes",
    "Rhone Alpes": "Auvergne-Rhône-Alpes",
    "Bourgogne": "Bourgogne-Franche-Comté",
    "Franche Comté": "Bourgogne-Franche-Comté",
    "Languedoc Roussillon": "Occitanie",
    "Midi Pyrénées": "Occitanie",
    "Midi Pyrenees": "Occitanie",
    "Basse Normandie": "Normandie",
    "Haute Normandie": "Normandie",
    "Nord Pas de Calais": "Hauts-de-France",
    "Picardie": "Hauts-de-France",
    "Etoile Amiens": "Hauts-de-France",
    "Centre": "Centre-Val de Loire",
    "Centre Val-de-Loire": "Centre-Val de Loire",
    "Pays-de-la-Loire": "Pays de la Loire",
    "Loire Océan": "Pays de la Loire",
    "Loire Ocean": "Pays de la Loire",
    "Nouvelle Aquitaine": "Nouvelle-Aquitaine",
    "Sud Azur": "Provence-Alpes-Côte d'Azur",
    "Provence Alpes Cote d'Azur": "Provence-Alpes-Côte d'Azur",
    "Ile de France": "Île-de-France",
    "Ile-de-France": "Île-de-France",
    "PACA": "Provence-Alpes-Côte d'Azur",
}

SNCF_DATASET_URLS = {
    TER_RAW_PATH: "https://ressources.data.sncf.com/explore/dataset/regularite-mensuelle-ter/download/?format=csv&timezone=Europe/Paris&lang=fr&use_labels_for_header=true&csv_separator=%3B",
    TRANSILIEN_RAW_PATH: "https://ressources.data.sncf.com/explore/dataset/ponctualite-mensuelle-transilien/download/?format=csv&timezone=Europe/Paris&lang=fr&use_labels_for_header=true&csv_separator=%3B",
    INTERCITES_RAW_PATH: "https://ressources.data.sncf.com/explore/dataset/regularite-mensuelle-intercites/download/?format=csv&timezone=Europe/Paris&lang=fr&use_labels_for_header=true&csv_separator=%3B",
    GARES_RAW_PATH: "https://ressources.data.sncf.com/explore/dataset/gares-de-voyageurs/download/?format=csv&timezone=Europe/Paris&lang=fr&use_labels_for_header=true&csv_separator=%3B",
    FREQUENTATION_RAW_PATH: "https://ressources.data.sncf.com/explore/dataset/frequentation-gares/download/?format=csv&timezone=Europe/Paris&lang=fr&use_labels_for_header=true&csv_separator=%3B",
}

HTTP_SOURCE_DETAILS = [
    {
        "source": "SNCF TER",
        "role": "Régularité mensuelle TER",
        "url": SNCF_DATASET_URLS[TER_RAW_PATH],
        "cache_path": TER_RAW_PATH,
    },
    {
        "source": "SNCF Transilien",
        "role": "Ponctualité mensuelle Transilien",
        "url": SNCF_DATASET_URLS[TRANSILIEN_RAW_PATH],
        "cache_path": TRANSILIEN_RAW_PATH,
    },
    {
        "source": "SNCF Intercités",
        "role": "Régularité mensuelle Intercités",
        "url": SNCF_DATASET_URLS[INTERCITES_RAW_PATH],
        "cache_path": INTERCITES_RAW_PATH,
    },
    {
        "source": "SNCF Gares",
        "role": "Référentiel gares de voyageurs",
        "url": SNCF_DATASET_URLS[GARES_RAW_PATH],
        "cache_path": GARES_RAW_PATH,
    },
    {
        "source": "SNCF Fréquentation",
        "role": "Fréquentation des gares",
        "url": SNCF_DATASET_URLS[FREQUENTATION_RAW_PATH],
        "cache_path": FREQUENTATION_RAW_PATH,
    },
    {
        "source": "geo.api.gouv.fr / regions",
        "role": "Régions officielles",
        "url": "https://geo.api.gouv.fr/regions",
        "cache_path": GEO_REGIONS_CACHE_PATH,
    },
    {
        "source": "geo.api.gouv.fr / departements",
        "role": "Départements officiels",
        "url": "https://geo.api.gouv.fr/departements?fields=nom,code,region",
        "cache_path": GEO_DEPARTEMENTS_CACHE_PATH,
    },
    {
        "source": "Open-Meteo Archive",
        "role": "Historique météo quotidien",
        "url": "https://archive-api.open-meteo.com/v1/archive",
        "cache_path": WEATHER_CACHE_PATH,
    },
]

DISPLAY_REGION_NAMES = {
    "Auvergne-Rhone-Alpes": "Auvergne-Rhône-Alpes",
    "Bourgogne-Franche-Comte": "Bourgogne-Franche-Comté",
    "Bretagne": "Bretagne",
    "Centre-Val de Loire": "Centre-Val de Loire",
    "Grand Est": "Grand Est",
    "Hauts-de-France": "Hauts-de-France",
    "Ile-de-France": "Île-de-France",
    "Normandie": "Normandie",
    "Nouvelle-Aquitaine": "Nouvelle-Aquitaine",
    "Occitanie": "Occitanie",
    "Pays de la Loire": "Pays de la Loire",
    "Provence-Alpes-Cote d'Azur": "Provence-Alpes-Côte d'Azur",
}

DISPLAY_MODE_NAMES = {
    "TER": "TER",
    "Transilien": "Transilien",
    "Intercites": "Intercités",
}

MAP_LABELS = {
    "Auvergne-Rhone-Alpes": "AURA",
    "Bourgogne-Franche-Comte": "BFC",
    "Bretagne": "Bret.",
    "Centre-Val de Loire": "CVL",
    "Grand Est": "GE",
    "Hauts-de-France": "HdF",
    "Ile-de-France": "IDF",
    "Normandie": "Norm.",
    "Nouvelle-Aquitaine": "NAq",
    "Occitanie": "Occ.",
    "Pays de la Loire": "PDL",
    "Provence-Alpes-Cote d'Azur": "PACA",
}

MONTH_ORDER = list(range(1, 13))
MONTH_LABELS = {
    1: "Jan",
    2: "Fev",
    3: "Mar",
    4: "Avr",
    5: "Mai",
    6: "Jun",
    7: "Jul",
    8: "Aou",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}
STRESS_BUCKET_ORDER = ["Mois calmes", "Mois intermediaires", "Mois chocs meteo"]
