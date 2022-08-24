from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def customers_output(spark: SparkSession, in0: DataFrame):
    in0.write.format("parquet").mode("overwrite").save("dbfs:/FileStore/Users/Maciej/test_output/customers/")
