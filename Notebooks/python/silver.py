# Databricks notebook source
# MAGIC %run "./utils"

# COMMAND ----------

# Read data from the bronze layer
bronze_reader = DeltaReader(location='/mnt/datalake/bronze/')
bronze_reader.set_file_names()
bronze_reader.set_file_list()

# COMMAND ----------

# Perform the necessary transformations for silver layer
from pyspark.sql.functions import col, lower
from pyspark.sql.functions import *


for i,_ in enumerate(bronze_reader.file_list):
    # Replacing '/' with ' '
    bronze_reader.file_list[i] = (
        bronze_reader.file_list[i]
            .withColumn("codigoLaboratorioPrimeiraDose", regexp_replace(bronze_reader.file_list[i]["codigoLaboratorioPrimeiraDose"], "/", " / "))
            .withColumn("codigoLaboratorioSegundaDose", regexp_replace(bronze_reader.file_list[i]["codigoLaboratorioSegundaDose"], "/", " / "))
            .withColumn("dataNotificacao", to_date(bronze_reader.file_list[i]["dataNotificacao"], "yyyy-MM-dd"))
            .withColumn("dataInicioSintomas", to_date(bronze_reader.file_list[i]["dataInicioSintomas"], "yyyy-MM-dd"))
            .withColumn("dataEncerramento", to_date(bronze_reader.file_list[i]["dataEncerramento"], "yyyy-MM-dd"))
            .withColumn("dataPrimeiraDose", to_date(bronze_reader.file_list[i]["dataPrimeiraDose"], "yyyy-MM-dd"))
            .withColumn("dataSegundaDose", to_date(bronze_reader.file_list[i]["dataSegundaDose"], "yyyy-MM-dd"))
            .withColumn("idade", bronze_reader.file_list[i]["idade"].cast("int"))
        )

    # Using initcap
    bronze_reader.file_list[i] = (
        bronze_reader.file_list[i]
            .withColumn("outrosSintomas",initcap(col("outrosSintomas")))
            .withColumn("outrasCondicoes",initcap(col("outrasCondicoes")))
            .withColumn("codigoLaboratorioPrimeiraDose",initcap(col("codigoLaboratorioPrimeiraDose")))
            .withColumn("codigoLaboratorioSegundaDose",initcap(col("codigoLaboratorioSegundaDose")))         
        )


# COMMAND ----------

# Write data in silver layer
silver_writer = Writer(location='/mnt/datalake/silver/', file_names=bronze_reader.file_names, file_list=bronze_reader.file_list)
silver_writer.write_files()