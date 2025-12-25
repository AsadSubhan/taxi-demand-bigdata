from config.spark_config import get_spark_session
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

spark = get_spark_session("Model_Training")

df = spark.read.parquet("data/processed/features")

assembler = VectorAssembler(
    inputCols=["pickup_hour", "pickup_day", "PULocationID"],
    outputCol="features"
)

data = assembler.transform(df).select("features", "trip_count")

train, test = data.randomSplit([0.8, 0.2])

rf = RandomForestRegressor(
    featuresCol="features",
    labelCol="trip_count",
    numTrees=20
)

model = rf.fit(train)

predictions = model.transform(test)

evaluator = RegressionEvaluator(
    labelCol="trip_count",
    predictionCol="prediction",
    metricName="rmse"
)

rmse = evaluator.evaluate(predictions)
print(f"📉 RMSE: {rmse}")

model.save("data/processed/demand_model")

print("✅ Model training completed")
