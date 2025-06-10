import yfinance as yf
import pandas as pd


def download_gold_data(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Descarga datos históricos del oro (XAU/USD) desde Yahoo Finance.

    Args:
        start_date (str): Fecha de inicio en formato 'YYYY-MM-DD'
        end_date (str): Fecha de fin en formato 'YYYY-MM-DD'

    Returns:
        pd.DataFrame: Datos históricos con columnas OHLCV
    """

    # 'GC=F' es el ticker de futuros del oro en Yahoo Finance
    gold_data = yf.download(
        "GC=F", start=start_date, end=end_date, interval="1d"
    )

    # Validación básica: asegura que se ha descargado la información
    if gold_data.empty:
        raise ValueError(
            "No se encontraron datos para el rango de fechas indicado."
        )

    # Renombrar las columnas para mayor claridad
    gold_data = gold_data.rename(
        columns={
            "Open": "open_price",
            "High": "high_price",
            "Low": "low_price",
            "Close": "close_price",
            "Adj Close": "adj_close_price",
            "Volume": "volume",
        }
    )

    # Añadir columna de fecha como índice explícito
    gold_data.reset_index(inplace=True)

    return gold_data
