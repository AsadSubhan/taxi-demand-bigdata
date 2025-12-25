CREATE EXTERNAL TABLE taxi_trips (
    PULocationID INT,
    pickup_hour INT,
    pickup_day INT,
    trip_count INT
)
STORED AS PARQUET
LOCATION '/data/processed/features';
