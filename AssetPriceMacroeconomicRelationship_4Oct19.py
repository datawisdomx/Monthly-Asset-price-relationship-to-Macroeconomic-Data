#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:13:56 2019

@author: nitinsinghal
"""

#Import libraries
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Import the macro and asset data for each country
# Macro data - US, UK, EU, India.
usmacrodata = pd.read_csv('Data/usmacrodata_sep19.csv')
eumacrodata = pd.read_csv('Data/eurmacrodata_sep19.csv')
ukmacrodata = pd.read_csv('Data/gbpmacrodata_sep19.csv')
# Asset data
nasdaqdata = pd.read_csv('Data/Nasdaq.csv')
sp500data = pd.read_csv('Data/SP500.csv')
daxdata = pd.read_csv('Data/DAX.csv')
oilwtidata = pd.read_csv('Data/OilWTI.csv')
golddata = pd.read_csv('Data/Gold.csv')
Russell2000data = pd.read_csv('Data/Russell2000.csv')
CACdata = pd.read_csv('Data/CAC40.csv')
FTSEdata = pd.read_csv('Data/FTSE.csv')
WilshireUSRealEstatedata = pd.read_csv('Data/WilshireUSRealEstatePriceIndex.csv')
UST10YrPricedata = pd.read_csv('Data/UST10YrPrice.csv')
Treasury10Yrdata = pd.read_csv('Data/UST10YrRates.csv')
UST2s10sdata = pd.read_csv('Data/UST2s10s.csv')

nasdaqdata['Date'] = pd.to_datetime(nasdaqdata['Date'])
nasdaqdata['Date'] = nasdaqdata['Date'].dt.strftime('%Y-%m-%d')
nasdaqdata = nasdaqdata.sort_values(by=['Date']).reset_index(drop=True)

sp500data['Date'] = pd.to_datetime(sp500data['Date'])
sp500data['Date'] = sp500data['Date'].dt.strftime('%Y-%m-%d')
sp500data = sp500data.sort_values(by=['Date']).reset_index(drop=True)

FTSEdata['Date'] = pd.to_datetime(FTSEdata['Date'])
FTSEdata['Date'] = FTSEdata['Date'].dt.strftime('%Y-%m-%d')
FTSEdata = FTSEdata.sort_values(by=['Date']).reset_index(drop=True)

daxdata['Date'] = pd.to_datetime(daxdata['Date'])
daxdata['Date'] = daxdata['Date'].dt.strftime('%Y-%m-%d')
daxdata = daxdata.sort_values(by=['Date']).reset_index(drop=True)

CACdata['Date'] = pd.to_datetime(CACdata['Date'])
CACdata['Date'] = CACdata['Date'].dt.strftime('%Y-%m-%d')
CACdata = CACdata.sort_values(by=['Date']).reset_index(drop=True)

Russell2000data['Date'] = pd.to_datetime(Russell2000data['Date'])
Russell2000data['Date'] = Russell2000data['Date'].dt.strftime('%Y-%m-%d')
Russell2000data = Russell2000data.sort_values(by=['Date']).reset_index(drop=True)

oilwtidata['Date'] = pd.to_datetime(oilwtidata['DATE'])
oilwtidata['Date'] = oilwtidata['Date'].dt.strftime('%Y-%m-%d')
oilwtidata.drop(['DATE'], inplace=True, axis=1)
oilwtidata = oilwtidata.sort_values(by=['Date']).reset_index(drop=True)

golddata['Date'] = pd.to_datetime(golddata['DATE'])
golddata['Date'] = golddata['Date'].dt.strftime('%Y-%m-%d')
golddata.drop(['DATE'], inplace=True, axis=1)
golddata = golddata.sort_values(by=['Date']).reset_index(drop=True)

UST10YrPricedata['Date'] = pd.to_datetime(UST10YrPricedata['Date'])
UST10YrPricedata['Date'] = UST10YrPricedata['Date'].dt.strftime('%Y-%m-%d')
UST10YrPricedata = UST10YrPricedata.sort_values(by=['Date']).reset_index(drop=True)

Treasury10Yrdata['Date'] = pd.to_datetime(Treasury10Yrdata['Date'])
Treasury10Yrdata['Date'] = Treasury10Yrdata['Date'].dt.strftime('%Y-%m-%d')
Treasury10Yrdata = Treasury10Yrdata.sort_values(by=['Date']).reset_index(drop=True)

UST2s10sdata['Date'] = pd.to_datetime(UST2s10sdata['DATE'])
UST2s10sdata['Date'] = UST2s10sdata['Date'].dt.strftime('%Y-%m-%d')
UST2s10sdata.drop(['DATE'], inplace=True, axis=1)
UST2s10sdata = UST2s10sdata.sort_values(by=['Date']).reset_index(drop=True)

# Take macro data from 1999 
usmacrodata = usmacrodata[['date','us_gdp_yoy', 'us_industrial_production','us_inflation_rate', 'us_core_pceinflation_rate',
                           'us_interest_rate','us_retail_sales_yoy', 
                           'us_consumer_confidence', 'us_business_confidence', 'us_unemployment_rate', 'us_manufacturing_production']] 
# 'us_manufacturing_pmi', 'us_non_manufacturing_pmi', 
usmacrodata['date'] = pd.to_datetime(usmacrodata['date'])
usmacrodata = usmacrodata[(usmacrodata['date'] > '31/12/1998')]
usmacrodata['date'] = usmacrodata['date'].dt.strftime('%Y-%m-%d')

eumacrodata = eumacrodata[['date','eu_gdp_yoy', 'eu_industrial_production','eu_inflation_rate', 'eu_core_inflation_rate',
                           'eu_interest_rate','eu_manufacturing_production','eu_retail_sales_yoy',
                           'eu_consumer_confidence','eu_business_confidence','eu_unemployment_rate']]
# 'eu_manufacturing_pmi','eu_services_pmi',
eumacrodata['date'] = pd.to_datetime(eumacrodata['date'])
eumacrodata = eumacrodata[(eumacrodata['date'] > '31/12/1998')]
eumacrodata['date'] = eumacrodata['date'].dt.strftime('%Y-%m-%d')

ukmacrodata = ukmacrodata[['date','uk_gdp_yoy', 'uk_industrial_production','uk_inflation_rate', 'uk_core_inflation_rate',
                           'uk_interest_rate','uk_manufacturing_production','uk_retail_sales_yoy',
                           'uk_consumer_confidence','uk_business_confidence','uk_unemployment_rate']]
# 'uk_manufacturing_pmi', 'uk_services_pmi',
ukmacrodata['date'] = pd.to_datetime(ukmacrodata['date'])
ukmacrodata = ukmacrodata[(ukmacrodata['date'] > '31/12/1998')]
ukmacrodata['date'] = ukmacrodata['date'].dt.strftime('%Y-%m-%d')

# Calculate R, R2, Cov matrix for usmacro Monthly data
usmacrocorrdata = usmacrodata.drop(['date'], axis=1).reset_index(drop=True)
usmacroMthlyRmatrix = usmacrocorrdata.corr(method='pearson')
usmacroMthlyR2matrix = usmacroMthlyRmatrix.pow(2)
usmacroMthlyCovmatrix = usmacrocorrdata.cov()
sns.heatmap(usmacroMthlyRmatrix, annot=True, fmt=".2f")

# Calculate R, R2, Cov matrix for eumacro Monthly data
eumacrocorrdata = eumacrodata.drop(['date'], axis=1).reset_index(drop=True)
eumacroMthlyRmatrix = eumacrocorrdata.corr(method='pearson')
eumacroMthlyR2matrix = eumacroMthlyRmatrix.pow(2)
eumacroMthlyCovmatrix = eumacrocorrdata.cov()
sns.heatmap(eumacroMthlyRmatrix, annot=True, fmt=".2f")

# Calculate R, R2, Cov matrix for ukmacro Monthly data
ukmacrocorrdata = ukmacrodata.drop(['date'], axis=1).reset_index(drop=True)
ukmacroMthlyRmatrix = ukmacrocorrdata.corr(method='pearson')
ukmacroMthlyR2matrix = ukmacroMthlyRmatrix.pow(2)
ukmacroMthlyCovmatrix = ukmacrocorrdata.cov()
sns.heatmap(ukmacroMthlyRmatrix, annot=True, fmt=".2f")

# merge us, eu, uk macro data files
macro99data = pd.merge(usmacrodata, eumacrodata, how='left', on='date')
macro99data = pd.merge(macro99data, ukmacrodata, how='left', on='date')

#Use only Close price
nasdaqclose = nasdaqdata.drop(['Open','High','Low','Adj Close', 'Volume'],axis=1)
nasdaqclose = nasdaqclose.rename({'Close':'nasdaq'}, axis='columns')
nasdaqclose['nasdaq'] = nasdaqclose['nasdaq'].str.replace(',', '').astype(float)
sp500close = sp500data.drop(['Open','High','Low','Adj Close', 'Volume'],axis=1)
sp500close = sp500close.rename({'Close':'sp500'}, axis='columns')
sp500close['sp500'] = sp500close['sp500'].str.replace(',', '').astype(float)
daxclose = daxdata.drop(['Open','High','Low','Adj Close', 'Volume'],axis=1)
daxclose = daxclose.rename({'Close':'dax'}, axis='columns')
CACclose = CACdata.drop(['Open','High','Low','Adj Close', 'Volume'],axis=1)
CACclose = CACclose.rename({'Close':'CAC'}, axis='columns')
FTSEclose = FTSEdata.drop(['Open','High','Low','Adj Close'],axis=1)
FTSEclose = FTSEclose.rename({'Close':'FTSE'}, axis='columns')
FTSEclose['FTSE'] = FTSEclose['FTSE'].str.replace(',', '').astype(float)
Russell2000close = Russell2000data.drop(['Open','High','Low','Adj Close', 'Volume'],axis=1)
Russell2000close = Russell2000close.rename({'Close':'Russell2000'}, axis='columns')
Treasury10Yrclose = Treasury10Yrdata.drop(['Open','High','Low','Adj Close', 'Volume'],axis=1)
Treasury10Yrclose = Treasury10Yrclose.rename({'Close':'Treasury10Yr'}, axis='columns')
UST10YrPriceClose = UST10YrPricedata.drop(['Open','High','Low','Vol.'],axis=1)
UST10YrPriceClose = UST10YrPriceClose.rename({'Price':'UST10YrPrice'}, axis='columns')

#Rename Close price column to index name
WilshireUSRealEstateclose = WilshireUSRealEstatedata.rename({'WILLRESIPR':'WilshireUSRealEst', 'DATE':'Date'}, axis='columns')
WilshireUSRealEstateclose['WilshireUSRealEst'] = pd.to_numeric(WilshireUSRealEstateclose['WilshireUSRealEst'], errors='coerce')
oilwticlose = oilwtidata.rename({'DCOILWTICO':'oilwti', 'DATE':'Date'}, axis='columns')
oilwticlose['oilwti'] = pd.to_numeric(oilwticlose['oilwti'], errors='coerce')
goldclose = golddata.rename({'GOLDAMGBD228NLBM':'gold', 'DATE':'Date'}, axis='columns')
goldclose['gold'] = pd.to_numeric(goldclose['gold'], errors='coerce')
UST2s10sclose = UST2s10sdata.rename({'T10Y2Y':'T2s10s', 'DATE':'Date'}, axis='columns')
UST2s10sclose['T2s10s'] = pd.to_numeric(UST2s10sclose['T2s10s'], errors='coerce')

#Merge asset, stock, oil, gold, treasur index data
Mergedstockindexdata = pd.merge(sp500close, nasdaqclose, how='left', on='Date')
Mergedstockindexdata = pd.merge(Mergedstockindexdata, daxclose, how='left', on='Date')
Mergedstockindexdata = pd.merge(Mergedstockindexdata, CACclose, how='left', on='Date')
Mergedstockindexdata = pd.merge(Mergedstockindexdata, Russell2000close, how='left', on='Date')
Mergedstockindexdata = pd.merge(Mergedstockindexdata, FTSEclose, how='left', on='Date')
Mergedstockindexdata = Mergedstockindexdata[(Mergedstockindexdata['Date'] < '2019-09-24')]

MergedAssetdata = pd.merge(Mergedstockindexdata, WilshireUSRealEstateclose, how='left', on='Date')
MergedAssetdata = pd.merge(MergedAssetdata, goldclose, how='left', on='Date')
MergedAssetdata = pd.merge(MergedAssetdata, oilwticlose, how='left', on='Date')
MergedAssetdata = pd.merge(MergedAssetdata, Treasury10Yrclose, how='left', on='Date')
MergedAssetdata = pd.merge(MergedAssetdata, UST10YrPriceClose, how='left', on='Date')
MergedAssetdata = pd.merge(MergedAssetdata, UST2s10sclose, how='left', on='Date')
MergedAssetdata = MergedAssetdata.fillna(0)

#Get all merged data from 1999, as most indices have data from then 
MergedAsset99data = MergedAssetdata[(MergedAssetdata['Date'] > '1998-12-31')]
MergedAsset99data.drop_duplicates(subset='Date', keep='first', inplace=True)

MergedAsset99Pricedata = MergedAsset99data.drop(['Treasury10Yr', 'T2s10s'], axis=1).reset_index(drop=True)

#Plot all asset data with subplot to plot against their own scale on x-axis, same y-axis date
MergedAsset99Pricedata.plot(x='Date', subplots=True, figsize=(8,20))

# Merge each asset price with us macro data
macro99 = macro99data
macro99['Date'] = pd.to_datetime(macro99['date'],format='%Y-%d-%m')
macro99 = macro99.drop(['date'], axis=1)
macro99 = macro99[(macro99['Date'] < '2019-10-01')]
macro99 = macro99.fillna(0)

indexdata = MergedAsset99Pricedata
indexdata.set_index(pd.DatetimeIndex(indexdata['Date']), inplace=True)
indexdata.drop(['Date'],inplace=True, axis=1)
assetmthlypricedata = indexdata.resample('M').mean()
assetmthlypricedata['Date'] = assetmthlypricedata.index
assetmthlypricedata['Date'] = pd.to_datetime(assetmthlypricedata['Date'].dt.strftime('%Y-%m'), format='%Y-%m')
assetmthlypricedata.reset_index(drop=True, inplace=True)
assetmthlypricedata = assetmthlypricedata[(assetmthlypricedata['Date'] < '2019-09-01')]

# Check correlation for different 10 year buckets for monthly average price of assets
mergedassetmacrodata = pd.merge(macro99, assetmthlypricedata, how='left', on='Date')
mergedassetmacrodata.plot(x='Date')
mergedassetmacrodata9908 = mergedassetmacrodata[(mergedassetmacrodata['Date'] <= '2008-12-01')]
mergedassetmacrodata0919 = mergedassetmacrodata[(mergedassetmacrodata['Date'] > '2008-12-01')]

# Calculate correlation of mthly avg price with main macro data
mergedassetmacrodataR = mergedassetmacrodata.corr(method='pearson')
mergedassetmacrodata9908R = mergedassetmacrodata9908.corr(method='pearson')
mergedassetmacrodata0919R = mergedassetmacrodata0919.corr(method='pearson')
mergedassetmacrodataR2 = mergedassetmacrodataR.pow(2)
mergedassetmacrodataCov = mergedassetmacrodata.cov()
mergedassetmacrodata9908R2 = mergedassetmacrodata9908R.pow(2)
mergedassetmacrodata0919R2 = mergedassetmacrodata0919R.pow(2)
plt.figure(figsize=(20,10))
sns.heatmap(mergedassetmacrodataR, annot=True, fmt=".2f")
sns.heatmap(mergedassetmacrodata9908R, annot=True, fmt=".2f")
sns.heatmap(mergedassetmacrodata0919R, annot=True, fmt=".2f")

# Plot main asset monthly prices vs main macro
mergedassetmacrodatamain = mergedassetmacrodata.drop(['us_gdp_yoy', 'us_industrial_production', 'us_retail_sales_yoy',
                            'us_business_confidence', 'us_manufacturing_production', 'us_inflation_rate', 
                            'eu_gdp_yoy', 'eu_industrial_production', 'eu_retail_sales_yoy', 
                            'eu_business_confidence', 'eu_manufacturing_production', 'eu_inflation_rate', 
                            'uk_gdp_yoy', 'uk_industrial_production', 'uk_retail_sales_yoy', 
                            'uk_business_confidence', 'uk_manufacturing_production', 'uk_inflation_rate', ], axis=1)
mergedassetmacrodatamainR = mergedassetmacrodatamain.corr(method='pearson')
mergedassetmacrodatamainR2 = mergedassetmacrodatamainR.pow(2)
plt.figure(figsize=(20,10))
sns.heatmap(mergedassetmacrodatamainR, annot=True, fmt=".2f")
plt.figure(figsize=(20,10))
sns.heatmap(mergedassetmacrodatamainR2, annot=True, fmt=".2f")

mergedassetmacrodata9908main = mergedassetmacrodata9908.drop(['us_gdp_yoy', 'us_industrial_production', 'us_retail_sales_yoy',
                            'us_business_confidence', 'us_manufacturing_production', 'us_inflation_rate', 
                            'eu_gdp_yoy', 'eu_industrial_production', 'eu_retail_sales_yoy', 
                            'eu_business_confidence', 'eu_manufacturing_production', 'eu_inflation_rate', 
                            'uk_gdp_yoy', 'uk_industrial_production', 'uk_retail_sales_yoy', 
                            'uk_business_confidence', 'uk_manufacturing_production', 'uk_inflation_rate', ], axis=1)
mergedassetmacrodata9908mainR = mergedassetmacrodata9908main.corr(method='pearson')
mergedassetmacrodata9908mainR2 = mergedassetmacrodata9908mainR.pow(2)
sns.heatmap(mergedassetmacrodata9908main.corr(method='pearson'), annot=True, fmt=".2f")

mergedassetmacrodata0919main = mergedassetmacrodata0919.drop(['us_gdp_yoy', 'us_industrial_production', 'us_retail_sales_yoy',
                            'us_business_confidence', 'us_manufacturing_production', 'us_inflation_rate', 
                            'eu_gdp_yoy', 'eu_industrial_production', 'eu_retail_sales_yoy', 
                            'eu_business_confidence', 'eu_manufacturing_production', 'eu_inflation_rate', 
                            'uk_gdp_yoy', 'uk_industrial_production', 'uk_retail_sales_yoy', 
                            'uk_business_confidence', 'uk_manufacturing_production', 'uk_inflation_rate', ], axis=1)
mergedassetmacrodata0919mainR = mergedassetmacrodata0919main.corr(method='pearson')
mergedassetmacrodata0919mainR2 = mergedassetmacrodata0919mainR.pow(2)
sns.heatmap(mergedassetmacrodata0919main.corr(method='pearson'), annot=True, fmt=".2f")

#### Comparing 2018 and 2019 Macro data visually using charts  #####
macro19 = macro99[(macro99['Date'] < '2019-10-01') & (macro99['Date'] > '2018-12-01')]
macro18 = macro99[(macro99['Date'] < '2019-01-01') & (macro99['Date'] > '2017-12-01')]
macro19 = macro19[['Date', 'us_interest_rate', 'uk_interest_rate', 'eu_interest_rate', 
                   'us_inflation_rate', 'uk_inflation_rate', 'eu_inflation_rate']]
macro18 = macro18[['Date', 'us_interest_rate', 'uk_interest_rate', 'eu_interest_rate', 
                   'us_inflation_rate', 'uk_inflation_rate', 'eu_inflation_rate']]
macro18.reset_index(drop=True, inplace=True)
macro19.reset_index(drop=True, inplace=True)
macro18.plot(x='Date', kind='line', figsize=(8,6))
macro19.plot(x='Date', kind='line', figsize=(8,6))
         
ir1819 = pd.concat([macro18[['us_interest_rate', 'uk_interest_rate', 'eu_interest_rate']], 
                    macro19[['us_interest_rate', 'uk_interest_rate', 'eu_interest_rate']]], axis=1)
ir1819.plot()
infl1819 = pd.concat([macro18[['us_inflation_rate', 'uk_inflation_rate', 'eu_inflation_rate']], 
                    macro19[['us_inflation_rate', 'uk_inflation_rate', 'eu_inflation_rate']]], axis=1)
infl1819.plot()





