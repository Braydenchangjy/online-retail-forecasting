import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Importing dataframe 
df = pd.read_csv("data/raw_data.csv")

# Renaming variables
year_float = df.Year
online_retail_rate = df.Percentage

# Changing "year" variable to datetime data type
year = year_float.round(0).astype(int)
days_into_year = round(((year_float - year) * 365), 0) # Assuming 365 days a year
time = pd.to_datetime(year.astype(str) + "-01-01", utc=False) + pd.to_timedelta(days_into_year - 1, unit="D")

# Splitting dataset into training (90%) and testing (10%) dataset, as well as pre-pandemic (<31 Jan 2020) and pandemic (>31 Jan 2020) dataset
time_train = time[:143]
time_test = time[143:159]
time_pandemic = time[159:]
online_retail_rate_train = online_retail_rate[:143]
online_retail_rate_test = online_retail_rate[143:159]
online_retail_rate_pandemic = online_retail_rate[159:]

# Creating dataframes
train_processed_df = pd.DataFrame({"Time": time_train, "Online Retail Rate": online_retail_rate_train})
test_processed_df = pd.DataFrame({"Time": time_test, "Online Retail Rate": online_retail_rate_test})
pandemic_processed_df = pd.DataFrame({"Time": time_pandemic, "Online Retail Rate": online_retail_rate_pandemic})

# Exporting dataframes as csv files
train_processed_df.to_csv("data/train_processed.csv")
test_processed_df.to_csv("data/test_processed.csv")
pandemic_processed_df.to_csv("data/pandemic_processed.csv")
