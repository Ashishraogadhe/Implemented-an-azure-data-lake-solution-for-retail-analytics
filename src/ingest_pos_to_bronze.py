from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
from config import paths

spark = SparkSession.builder.appName("IngestRetailPOS").getOrCreate()

source_path = "/mnt/raw/retail/pos/*.csv"

df_pos = (
    spark.read.option("header", True)
    .option("inferSchema", True)
    .csv(source_path)
    .withColumn("ingested_at_utc", current_timestamp())
)

(
    df_pos.write.mode("overwrite")
    .format("delta")
    .save(paths.bronze_pos)
)
