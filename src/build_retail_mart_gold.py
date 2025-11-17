from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from config import paths

spark = SparkSession.builder.appName("BuildRetailMartGold").getOrCreate()

bronze_pos = spark.read.format("delta").load(paths.bronze_pos)

fact_sales = (
    bronze_pos
    .withColumn("sale_date", to_date(col("transaction_time")))
    .select(
        col("transaction_id").alias("sales_id"),
        col("store_id"),
        col("product_id"),
        col("customer_id"),
        col("sale_date"),
        col("quantity"),
        col("net_amount").alias("sales_amount"),
        col("currency")
    )
)

(
    fact_sales.write.mode("overwrite")
    .format("delta")
    .partitionBy("sale_date")
    .save(paths.gold_fact_sales)
)

print(f"Wrote fact_sales to {paths.gold_fact_sales}")
