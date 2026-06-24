from pyspark.sql import SparkSession


def get_spark():

    return (
        SparkSession.builder
        .appName("GrammarRigor")
        .master("local[*]")
        .getOrCreate()
    )


def create_rdd(spark, sentences, partitions=8):

    return spark.sparkContext.parallelize(sentences, partitions)