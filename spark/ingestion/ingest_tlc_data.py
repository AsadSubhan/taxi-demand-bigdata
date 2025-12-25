from config.spark_config import get_spark_session

spark = get_spark_session("TLC_Ingestion")

input_path = "data/raw/yellow_tripdata_2023-01.csv"
output_path = "data/processed/trips_parquet"

df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(input_path)
)

df.write.mode("overwrite").parquet(output_path)

print("✅ Data ingestion completed")
