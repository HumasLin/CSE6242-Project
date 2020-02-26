// This part of code aims at calculating the average price for different groups in our dataset

// Databricks notebook source

// Import necessary libraries needed
import org.apache.spark.sql.functions.desc
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import spark.implicits._

// The applied options are for CSV files. For other file types, these will be ignored
// Suppose the name of dataset is "team13_original_data.csv", read data by the following commands
// COMMAND ----------

var df = spark.read.format("com.databricks.spark.csv") 
              .option("header", "true") // Use first line of all files as header
              .option("nullValue", "null")
              .load("/FileStore/tables/team13_original_data.csv")
display(df)

// Group the data by product name, source and destination and caculate the average price for each group
// COMMAND ----------

var average = df.groupBy("name", "source", "destination").agg(avg("price")).toDF("name1", "source1", "destination1", "avg(price)")
average.describe()

// Add the average column to the original dataset
// COMMAND ----------

var df3 = df.join(average, df("name") === average("name1") && df("source") === average("source1") && df("destination") === average("destination1"))
display(df3)
