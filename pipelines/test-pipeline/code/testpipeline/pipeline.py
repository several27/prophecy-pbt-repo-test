from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from testpipeline.config.ConfigStore import *
from testpipeline.udfs.UDFs import *
from prophecy.utils import *
from testpipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers_source = customers_source(spark)
    df_Reformat_1 = Reformat_1(spark, df_customers_source)
    customers_output(spark, df_Reformat_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "2867/pipelines/test-pipeline")
    MetricsCollector.start(spark = spark, pipelineId = "2867/pipelines/test-pipeline")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
