import os
from chromadb.config import Settings

#Define chroma settings
chroma_settings = Settings(
    chroma_db_impl = 'duckdb+parquet',
    persist_directory = "db",
    anonymized_telemetry = False
)


