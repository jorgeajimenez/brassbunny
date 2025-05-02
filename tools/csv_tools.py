# tools/csv_tools.py

from server import mcp
from utils.file_reader import read_csv_summary
import pandas as pd


@mcp.tool()
def summarize_csv_file(filename: str) -> str:
    """
    Summarize a CSV file by reporting its number of rows and columns.
    Args:
        filename: Name of the CSV file in the /data directory (e.g., 'sample.csv')
    Returns:
        A string describing the file's dimensions.
    """
    return read_csv_summary(filename)


@mcp.tool()
def sample_csv_file(filename: str) -> pd.DataFrame:
    """
    Read a CSV file and randomly sample 10% of its rows.
    Args:
        filename: Name of the CSV file in the /data directory (e.g., 'sample.csv')
    Returns:
        A string representing the sampled rows.
    """
    df = pd.read_csv(f"data/{filename}")
    return df
