from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("c_custkey"), 
        concat(col("c_name"), col("c_name")).alias("c_name"), 
        col("c_address"), 
        col("c_nationkey"), 
        col("c_phone"), 
        col("c_acctbal"), 
        col("c_mktsegment"), 
        col("c_comment")
    )
