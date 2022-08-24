from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def customers_source(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/databricks-datasets/tpch/delta-001/customer/")
