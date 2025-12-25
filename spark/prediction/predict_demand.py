from config.spark_config import get_spark_session
from pyspark.ml.regression import RandomForestRegressionModel
from pyspark.ml.feature import VectorAssembler

spark = get_spark_session("Demand_Prediction")

model = RandomForestRegressionModel.load("data/processed/demand_model")

input_data = spark.createDataFrame([
    (5, 3, 237)
], ["pickup_hour", "pickup_day", "PULocationID"])

assembler = VectorAssembler(
    inputCols=["pickup_hour", "pickup_day", "PULocationID"],
    outputCol="features"
)

input_features = assembler.transform(input_data)

prediction = model.transform(input_features)
prediction.show()
