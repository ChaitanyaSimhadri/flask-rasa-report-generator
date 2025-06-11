import pandas as pd
from datetime import datetime

def generate_sales_report():
    """Generates a sample sales report."""
    data = {'Product': ['A', 'B', 'C'],
            'Sales': [100, 150, 120]}
    df = pd.DataFrame(data)
    filename = f"reports/sales_report_{datetime.now().strftime('%Y-%m-%d')}.csv"
    df.to_csv(filename, index=False)
    return filename
