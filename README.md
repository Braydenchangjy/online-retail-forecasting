# The Fate of Online Retail Post-pandemic
**An analysis of the effect of the COVID-19 interruption on the online retail rates in the UK**

The COVID-19 pandemic brought a surge in online retail rates (expressed as a percentage of total retail rates) globally due to lockdown restrictions forcing many consumers to go online. The question to be answered post-pandemic is whether this surge in online retail will be retained by consumers or whether they are opting to return to traditional retail methods. The project will focus on online retail data in the UK, aiming to create a counterfactual model of what online retail rates would have been like without the COVID-19 interruption for comparison with the actual online retail rates during the COVID-19 pandemic. 

Exploratory Data Analysis to determine the optimal model parameters is first conducted. Online retail rate data is decomposed using STL (Seasonal and Trend Decomposition using LOESS) as well as analysed for non-stationariness, autocorrelation and partial autocorrelation. The results are used to fit a SARIMA (Seasonal AutoRegressive Integrated Moving Average) counterfactual model without the effect of the COVID-19 pandemic. The SARIMA counterfactual model will then be compared to historical data as well as evaluated for its accuracy.

The analysis serves to give business insights into whether the pandemic has permanently affected the future of online retail or whether the surge in online retail will only be temporary, assisting businesses, policy makers, and stakeholders in their decisions.

# Details

**Dataset:** https://www.ons.gov.uk/businessindustryandtrade/retailindustry/timeseries/j4mc/drsi

**Jupyter Notebooks and Python Scripts:** The main analysis is conducted in "analysis.ipynb", a separate python script "data_preparation.py" is used to create the processed datasets ("data/train_processed.csv", "data/test_processed.csv", "data/pandemic_processed.csv") from the above original dataset.

*All graphs used in the poster have the poster aesthetics, all graphs not used have default parameters.*
