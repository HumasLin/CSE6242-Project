# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ## Overview
# MAGIC 
# MAGIC This notebook will show you how to create and query a table or DataFrame that you uploaded to DBFS. [DBFS](https://docs.databricks.com/user-guide/dbfs-databricks-file-system.html) is a Databricks File System that allows you to store data for querying inside of Databricks. This notebook assumes that you have a file already inside of DBFS that you would like to read from.
# MAGIC 
# MAGIC This notebook is written in **Python** so the default cell type is Python. However, you can use different languages by using the `%LANGUAGE` syntax. Python, Scala, SQL, and R are all supported.

# COMMAND ----------

# File location and type
file_location = "/FileStore/tables/666.csv"
file_type = "csv"

# CSV options
infer_schema = "false"
first_row_is_header = "true"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

display(df)

# COMMAND ----------

# Create a view or table

temp_table_name = "666_csv"

df.createOrReplaceTempView(temp_table_name)

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC /* Query the created temp table in a SQL cell */
# MAGIC drop table if exists new;
# MAGIC 
# MAGIC create table new
# MAGIC select icon, weekday, hour, avg(predict) as pre from `666_csv`
# MAGIC group by icon, weekday, hour

# COMMAND ----------

# MAGIC %sql
# MAGIC /* Query the created temp table in a SQL cell */
# MAGIC drop table if exists draw;
# MAGIC 
# MAGIC create table draw
# MAGIC select icon, weekday, hour, 1 as pre from new
# MAGIC where pre < 1.35
# MAGIC union all
# MAGIC select  icon, weekday, hour, 2 as pre from new
# MAGIC where pre >= 1.35 and pre <= 1.47
# MAGIC union all
# MAGIC select  icon, weekday, hour, 3 as pre from new
# MAGIC where pre > 1.47

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select count(*), pre from draw
# MAGIC group by pre

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from draw
