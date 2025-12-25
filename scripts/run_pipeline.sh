#!/bin/bash

spark-submit spark/ingestion/ingest_tlc_data.py
spark-submit spark/preprocessing/preprocess_trips.py
spark-submit spark/feature_engineering/build_features.py
spark-submit spark/modeling/train_demand_model.py
