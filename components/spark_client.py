from databricks.connect import DatabricksSession

import config

spark = DatabricksSession.builder.remote(
    host=config.DATABRICKS_HOST,
    token=config.DATABRICKS_TOKEN,
    cluster_id=config.DATABRICKS_CLUSTER_ID
).getOrCreate()
