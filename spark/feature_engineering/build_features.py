from config.spark_config import get_spark_session
from pyspark.sql.functions import count

spark = get_spark_session("Feature_Engineering")

df = spark.read.parquet("data/processed/clean_trips")

features_df = (
    df.groupBy("PULocationID", "pickup_hour", "pickup_day")
    .agg(count("*").alias("trip_count"))
)

features_df.write.mode("overwrite").parquet("data/processed/features")

print("✅ Feature engineering completed")
