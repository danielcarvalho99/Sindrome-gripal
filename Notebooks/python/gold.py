# Databricks notebook source
# MAGIC %run "./utils"

# COMMAND ----------

# Read data from silver layer
silver_reader = DeltaReader(location='/mnt/datalake/silver/')
silver_reader.set_file_names()
silver_reader.set_file_list()

# COMMAND ----------

# Necessary aggregations for the gold layer
for i,_ in enumerate(silver_reader.file_list):
  silver_reader.file_list[i].createOrReplaceTempView("casos")
  silver_reader.file_list[i] = spark.sql("""
    SELECT 
      municipioNotificacao,
      EXTRACT (YEAR FROM datanotificacao) AS anoNotificacao,
      EXTRACT (MONTH FROM datanotificacao) AS mesNotificacao,
      SUM(CASE WHEN (dataPrimeiraDose IS NULL AND dataSegundaDose IS NULL) THEN 1 ELSE 0 END) AS naoVacinados,
      SUM(CASE WHEN dataPrimeiraDose IS NOT NULL THEN 1 ELSE 0 END) AS vacinadosPrimeiraDose,
      SUM(CASE WHEN dataSegundaDose IS NOT NULL THEN 1 ELSE 0 END) AS vacinadosSegundaDose,
      SUM(CASE WHEN idade BETWEEN 0 AND 18 THEN 1 ELSE 0 END) AS casosNaFaixa_0_18,
      SUM(CASE WHEN idade BETWEEN 19 AND 35 THEN 1 ELSE 0 END) AS casosNaFaixa_19_35,
      SUM(CASE WHEN idade BETWEEN 36 AND 50 THEN 1 ELSE 0 END) AS casosNaFaixa_36_50,
      SUM(CASE WHEN idade BETWEEN 51 AND 65 THEN 1 ELSE 0 END) AS casosNaFaixa_51_65,
      SUM(CASE WHEN idade IS NULL THEN 1 ELSE 0 END) AS casosIdadeNaoInformada
    FROM
      casos
    WHERE
      datanotificacao IS NOT NULL
    GROUP BY 
      municipioNotificacao, EXTRACT (YEAR FROM datanotificacao), EXTRACT (MONTH FROM datanotificacao)
    ORDER BY 
      anoNotificacao, mesNotificacao, municipioNotificacao
  """)

# COMMAND ----------

# Write data in gold layer
gold_writer = Writer(location='/mnt/datalake/gold/', file_names=silver_reader.file_names, file_list=silver_reader.file_list)
gold_writer.write_files()