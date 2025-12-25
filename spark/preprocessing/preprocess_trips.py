from config.spark_config import get_spark_session
from pyspark.sql.functions import col, hour, dayofweek

spark = get_spark_session("TLC_Preprocessing")

df = spark.read.parquet("data/processed/trips_parquet")

clean_df = (
    df
    .filter(col("trip_distance") > 0)
    .filter(col("fare_amount") > 0)
    .withColumn("pickup_hour", hour(col("tpep_pickup_datetime")))
    .withColumn("pickup_day", dayofweek(col("tpep_pickup_datetime")))
)

clean_df.write.mode("overwrite").parquet("data/processed/clean_trips")

print("✅ Preprocessing completed")
