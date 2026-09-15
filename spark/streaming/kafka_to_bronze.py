from pyspark.sql import SparkSession
# Creates the Spark application

from pyspark.sql.functions import from_json, col
# from_json converts JSON text into columns


from pyspark.sql.types import StructType, StructField, StringType
# Used to define the structure of our JSON data


# Start Spark
spark = SparkSession.builder \
    .appName("HumanActivityKafkaToBronze") \
    .getOrCreate()
# Creates a Spark session for our streaming application


spark.sparkContext.setLogLevel("WARN")
# Shows only important warnings/errors in the terminal


# Define the structure of our Kafka JSON data
schema = StructType([
    StructField("event_id", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("event_type", StringType(), True),
    StructField("page", StringType(), True),
    StructField("device", StringType(), True),
    StructField("country", StringType(), True),
    StructField("timestamp", StringType(), True),
    StructField("session_id", StringType(), True)
])
# This matches the 8 fields in your human activity events


# Read streaming data from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "human-activity") \
    .option("startingOffsets", "earliest") \
    .load()
# Connects Spark to Kafka
# localhost:9092 = Kafka server
# human-activity = Kafka topic
# earliest = read existing events first


# Convert Kafka value from bytes to JSON
activity_df = kafka_df.select(
    from_json(
        col("value").cast("string"),
        schema
    ).alias("data")
).select("data.*")
# Kafka stores the event in the "value" column
# Convert it to text
# Convert JSON text into proper columns


# Write the data to Bronze
query = activity_df.writeStream \
    .format("parquet") \
    .outputMode("append") \
    .option("path", "data/bronze/human_activity") \
    .option(
        "checkpointLocation",
        "data/checkpoints/human_activity"
    ) \
    .start()
# Saves the streaming data as Parquet
# append = add new events without deleting old events
# path = Bronze storage location
# checkpoint = remembers which Kafka events Spark processed


# Keep the streaming job running
query.awaitTermination()
# Spark continuously waits for new Kafka events