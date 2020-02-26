The original data is from Kaggle:

https://www.kaggle.com/brllrb/uber-and-lyft-dataset-boston-ma

DESCRIPTION: 

Firstly, "T13_average.scala" is used for grouping each trip based on cab's product name, source and destination, then calculating the average prices. After using Excel to calculate the surge parameter using price for each trip divided by average price for the corresponding group, "T13_refine.ipynb" is used for transforming timestamp into real time and calculate the corresponding weekday and rounding the surge multiplier to an integer according to its definition.

For prediction, "creating_unique_combinations.ipynb" is used for generating a series of combinations of different variables in order for the test use in prediction. Then "T13_analysis.ipynb" is used for building the classification model and fitting the random forests model in Python scikit-learn with refined dataset. It also makes prediction based on our self-constructed attributes set from "creating_unique_combinations.ipynb" as an experiment.

In visualization part, using "results.csv", "Preprocessing.py" stores the codes we write to put the results into 3 different clusters. It makes the predicted result more separated, whose output can be used for visualization. "T13visual.html" is the source code of the visualization realized in d3.js.

At last, we use "results.csv" and "T13_PC_GUI.py" to implement GUI in PC platform and "T13_mobile_GUI.xd" to implement GUI in mobile platform.

INSTALLATION

There is no need to install the implementations. We only need to prepare Python, the community version of Databricks, Jupyter Notebook and Firefox browser.

EXECUTION

Load the original data into databricks, then import the source codes into Jupyter Notebook and Databricks.com, then execute the code to get corresponding dataset, then upload data or import source code onto Databricks.com or Jupyter Notebook for the next step. At last, use the data "results.csv" to prepare for visualization launched in Firefox or implement GUI via python.
