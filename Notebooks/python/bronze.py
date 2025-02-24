# Databricks notebook source
# Mounting the ADLS if necessary
access_key = dbutils.secrets.get(scope="databricks-secrets", key="access-key")
storage_account = "danieldatalake"
container = "sindrome-gripal"
source_path = f"wasbs://{container}@{storage_account}.blob.core.windows.net/"

if not dbutils.fs.ls('/mnt/'):
    dbutils.fs.mount(source = source_path,
              mount_point = '/mnt/datalake',
              extra_configs = {f"fs.azure.account.key.{storage_account}.blob.core.windows.net": f"{access_key}"})
    print('Directory mounted!')
else:
    print('Directory already mounted!')
    

# COMMAND ----------

# MAGIC %run "./utils"
# MAGIC

# COMMAND ----------

# Read data from raw folder
raw_reader = CsvReader(location='/mnt/datalake/raw/')
raw_reader.set_file_names()
raw_reader.set_file_list()


# COMMAND ----------

# Write data in bronze layer
bronze_writer = Writer(location='/mnt/datalake/bronze/', file_names=raw_reader.file_names, file_list=raw_reader.file_list)
bronze_writer.write_files()