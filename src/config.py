from dataclasses import dataclass

@dataclass
class RetailPaths:
    base: str = "abfss://retail@yourstorageaccount.dfs.core.windows.net"
    bronze_pos: str = f"{base}/bronze/pos"
    silver_sales: str = f"{base}/silver/sales"
    silver_customers: str = f"{base}/silver/customers"
    silver_products: str = f"{base}/silver/products"
    gold_fact_sales: str = f"{base}/gold/fact_sales"

paths = RetailPaths()
