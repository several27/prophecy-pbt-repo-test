from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from testpipeline.graph.Reformat_1 import *
import testpipeline.config.ConfigStore as ConfigStore


class Reformat_1Test(BaseTestCase):

    def test_unit_test_0(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/testpipeline/graph/Reformat_1/in0/schema.json',
            'test/resources/data/testpipeline/graph/Reformat_1/in0/data/test_unit_test_0.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/testpipeline/graph/Reformat_1/out/schema.json',
            'test/resources/data/testpipeline/graph/Reformat_1/out/data/test_unit_test_0.json',
            'out'
        )
        dfOutComputed = Reformat_1(self.spark, dfIn0)
        assertDFEquals(dfOut.select("c_name"), dfOutComputed.select("c_name"), self.maxUnequalRowsToShow)

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        ConfigStore.Utils.initializeFromArgs(
            self.spark,
            Namespace(file = f"configs/resources/config/{fabricName}.json", config = None)
        )
