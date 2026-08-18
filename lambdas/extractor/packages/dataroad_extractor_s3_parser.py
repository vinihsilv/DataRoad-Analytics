import pandas as pd
import openpyxl


class DataroadExtractorS3Parser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_csv_to_dataframe(self) -> pd.DataFrame:
        if self.file_path.endswith(".csv"):
            return pd.read_csv(
                self.file_path, encoding="utf-8", delimiter=",", dtype=str
            )
        elif self.file_path.endswith(".xlsx"):
            return pd.read_excel(self.file_path, engine="openpyxl", dtype=str)
        else:
            raise ValueError(
                "Unsupported file format. Only CSV and XLSX are supported."
            )
