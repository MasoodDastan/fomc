# Analyzing the Impact of Federal Open Market Committee Meetings on Stock Market Performance

## Problem Statement:

The aim of this project is to investigate the impact of Federal Open Market Committee (FOMC) meetings on stock market performance and fluctuation. The FOMC's decisions have a substantial influence not only on the broader economy but also on the stock market. Therefore, the primary objective is to analyze how the content of the discussions during these meetings and the overall sentiment expressed among committee members contribute to the overall performance of the stock market.

By incorporating a variety of economic indicators, this project seeks to gain valuable insights into the interplay between FOMC meetings, financial market behavior, and economic indicators. The findings from this research can offer a deeper understanding of how the FOMC's actions and sentiments influence stock market movements and provide valuable implications for investors, policymakers, and financial analysts alike.

## Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**ffr**|float|FRED|The federal funds rate is the interest rate at which depository institutions trade federal funds (balances held at Federal Reserve Banks) with each other overnight. ([link](https://fred.stlouisfed.org/series/DFF))|
|**unemployment_rate**|float|FRED|The federal funds rate is the interest rate at which depository institutions trade federal funds (balances held at Federal Reserve Banks) with each other overnight. ([link](https://fred.stlouisfed.org/series/UNRATE))|
|**retail_sales**|float|FRED|The most recent month's value of the advance estimate based on data from a subsample of firms. ([link](https://fred.stlouisfed.org/series/MRTSSM44X72USS))|
|**10_year_treasury_yeild**|float|FRED|The most recent month's value of the advance estimate based on data from a subsample of firms. ([link](https://fred.stlouisfed.org/series/T10Y2Y))|
|**vix**|float|FRED|VIX measures market expectation of near term volatility conveyed by stock index option prices. ([link](https://fred.stlouisfed.org/series/VIXCLS))|
|**real_gdp**|float|FRED|The inflation adjusted value of the goods and services produced by labor and property located in the United States. ([link](https://fred.stlouisfed.org/series/GDPC1))|
|**cpi**|float|FRED|Price index of a basket of goods and services paid by urban consumers. ([link](https://fred.stlouisfed.org/series/CPIAUCSL))|
|**10year_3month_yield_spread**|float|FRED|The spread between 10-Year Treasury Constant Maturity and 3-Month Treasury Constant Maturity. ([link](https://fred.stlouisfed.org/series/T10Y3M))|
|**us_china_exchange_rate**|float|FRED|Chinese Yuan Renminbi to U.S. Dollar Spot Exchange Rate. ([link](https://fred.stlouisfed.org/series/DEXCHUS))|
|**us_japan_exchange_rate**|float|FRED|Japanese Yen to U.S. Dollar Spot Exchange Rate. ([link](https://fred.stlouisfed.org/series/DEXJPUS))|
|**FOMC minutes**|object|Federal Reserve|The minutes text data of the FOMC meetings ([link](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm))|
|**epu**|float| policyuncertainty | Economic Policy Uncertainty (EPU) Index is an economic indicator that measures the level of uncertainty in a country's economy arising from policy-related factors. ([link](https://www.policyuncertainty.com/))|


## Executive Summary:

In this project

