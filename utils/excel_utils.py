import pandas as pd

def export_to_excel(teas, filename: str):
    """Export tea varieties to an Excel file"""
    df = pd.DataFrame([tea.__dict__ for tea in teas])
    df.to_excel(filename, index=False)