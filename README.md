# Investigating the Impact of FOMC Meetings on Stock Market Performance

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


The goal of this project is to investigate the impact of Federal Open Market Committee (FOMC) meetings on stock market performance. The FOMC is the monetary policymaking body of the Federal Reserve System, responsible for supervising the country's open market operations and shaping monetary policy. The project used text analysis to uncover key themes, discussions, and focal points in FOMC meetings and gauge the overall sentiment among committee members during meetings. Additionally, a diverse range of economic indicators was integrated to contextualize FOMC decisions within the broader economic landscape, identifying potential interconnections between monetary policy and overall economic performance.

### Data Collection and Feature Engineering:
Data for the project was collected from three different sources. The S&P 500 index price data was gathered from Yahoo Finance, providing comprehensive stock market performance information. Three new features were engineered from this data, including target variable labels (price change) from the adjusted close price, percentage change in Adjust closing price (lagged), and the 15-day rolling average of the percentage change in Adjust closing price (lagged).

The second source of data was FRED (Federal Reserve Economic Data), providing access to a wide range of essential economic indicators. The project used the FRED API to scrape indicators such as Real GDP, Consumer Price Index (CPI), Retail Sales, Federal Fund Rate, Treasury yield, Treasury yield spread, and US dollar strength. Additional engineered features included Year-over-Year (YoY) GDP growth and YoY Inflation Rate.

The last source of data was FOMC meeting minutes, which underwent thorough cleaning steps, including removal of punctuations, stopwords, and non-noun, verb, or adjective words. Lemmatization of the remaining tokens was also performed.

### Topic Modeling and Meeting Sentiments:
Topic modeling, specifically Latent Dirichlet Allocation (LDA), was employed to reveal key topics and themes discussed during FOMC meetings. This statistical modeling approach helped identify clusters or groups of similar words within the text data, providing insights into the context of discussions and focusing on significant US economic concerns.

Meeting sentiments were generated using two methods. The first method used the Loughran and McDonald Word Dictionary, a specialized word list designed for analyzing financial documents. This approach allowed for effective sentiment analysis of FOMC statements, considering their often-vague and technical language.

The second method employed zero-shot text classification, utilizing a pre-trained transformer model developed by Facebook (BART-large-mnli) which allows classifying previously unseen classes in this project, providing a more comprehensive sentiment analysis. Using this approach a sentiment analysis model was develped to classify FOMC minutes into positive and negative categories.

### Model Evaluation:
Five classification models (Recurrent Neural Net, Logistic Regression, Random Forest, Support Vector Machine, and Gradient Boosting) were evaluated using cross-validated randomized search. The performance of these models was measured using accuracy and AUC scores. The Gradient Boosting Classifier achieved the highest accuracy (57%) and AUC score (61%).

### Conclusion:
The project successfully investigated the impact of FOMC meetings on stock market performance and fluctuations using advanced text analysis techniques. The analysis of key themes and discussions in FOMC meetings, combined with meeting sentiments and economic indicators, provided valuable insights into policymakers' expectations and monetary policy's influence on the economy. The findings contribute to a deeper understanding of the relationship between FOMC decisions and overall economic performance, offering potential implications for investors and policymakers alike.

