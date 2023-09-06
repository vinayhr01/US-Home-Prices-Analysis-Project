# US Home Prices Analysis

## Supply and demand factors impacting US home prices over the last 20 years

* Considered time period for all supply and demand factors are from 1st January 2003 to 1st April 2023 have quarter of an year incremented values
* All data are from taken from [Economic Research Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org).
* Considered [S&amp;P/Case-Shiller U.S. National Home Price Index](https://fred.stlouisfed.org/series/CSUSHPISA#) as proxy for home prices.
* Considered 30+ factors (refer [Factors.csv](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/Factors.csv) file for all factors) which could have direct or indirect impact on home prices by searching the data source, [Economic Research Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org) using housing related keywords.

### Procedure followed to filter 30+ factors to more relevant and less factors

* All factors were initially separate CSV files when downloaded from the source mentioned above, but have been merged and converted into a single CSV file (refer [merged_data.csv](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/merged_data.csv) for CSV file) and since factors have code names, the description of these factors were also considered to form a CSV file (refer [Factors.csv](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/Factors.csv) for CSV file).
* If any factors have less data than time period mentioned above, the missing values are handled by using mean simple imputation method and according to requirements.
* For instance, [Interest Rates, Discount Rate for United States (INTDSRUSM193N)](https://fred.stlouisfed.org/series/INTDSRUSM193N) had 7 values missing and had been filled using mean simple imputation method (refer [MLmodel.py](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/49f7cff5ac010564062e9ea573aca33b851b92b0/MLmodel.py#L19-L31))
* Then found the correlation of all factors with respect to [S&amp;P/Case-Shiller U.S. National Home Price Index](https://fred.stlouisfed.org/series/CSUSHPISA#).
* Based on high correlation values and meaning of the factors, first filtering of a few factors were done and then variance inflation method was applied to further remove factors (refer [multicollinearity.py](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/multicollinearity.py)) thus helping in reducing multicollinearity problem which could arise due to highly correlated predictor and target (refer [delsimfactors.txt](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/delsimfactors.txt) file for factors removal) and then studying the visualizations, few more factors were removed.

### ML Model building

* Initially all values are converted to their appropriate numeric values in the dataset after filtering certain factors based on the above mentioned criteria (refer [final_merged_data.csv](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/final_merged_data.csv) for CSV file) and similarly factors manipulated are updated in another CSV file (refer [final_Factors.csv](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/final_Factors.csv)).
* Then preprocessing of data must be done, such removing outliers from dataset, normalizing the values, because of different types of measured values in the dataset.
* Z-Scores with a certain threshold condition are used to remove outliers, if there are any outliers. Z-Scores determine how far a data point is from the mean of that data in terms of standard deviation, given by Z = (X - mean) / std. deviation, positive Z-score means data point is above the mean and similarly holds true for other conditions.
* Normalization is done using MinMaxScaler which reduces all values to a range of 0 to 1. Then another column caller **QUARTER** is added to the dataset to have quarter divisions for visualization (refer [normalized_data.csv](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/normalized_data.csv))
* Every graph visualization depicts a view of a factor mapped along with home price index to show its variation as shown in below images.
* Then data is split into training and testing data with 80% to 20% ratio.
* 5 different ML algorithms and best algorithm producing the least **Mean Squared Error** are chosen to build the model.
* The parameters to be set for these algorithms are chosen with the help of **hyper-parameter tuning** (refer [hyppara_tune.py](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/hyppara_tune.py)).
* In order to check if data is overfitting or underfitting, baseline predicitons are where mean and median of testing dataset are compared with testing predictions scores of the model, the model here shows a significant differences between them, ensuring that data is not underfitting or overfitting.

## Key Supply-Demand factors that impacted US home prices over the last 20 years

## Supply Factors:

##### 1) AUTHNOTTSA, New Privately-Owned Housing Units Authorized but Not Started: Total Units:

###### Visualization:

![AUTHNOTTSA.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/AUTHNOTTSA.png "AUTHNOTTSA.png")

**Explanation:**

* Initially authorized housing units were more and hence prices were lower. But later a recession during 2008-09 hit the market, hence both prices and housing units both declined.
* Once the recession period ended gradually market started to go up hand-in-hand, i.e, prices and authorized housing units inclined drastically.

##### 2) EVACANTUSQ176N, Housing Inventory Estimate: Vacant Housing Units in the United States:

###### Visualization:

![EVACANTUSQ176N.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/EVACANTUSQ176N.png "EVACANTUSQ176N.png")

**Explanation:**

* Similar to above phenomena, initially both vacant housing units and prices started to increase.
* But then on, it started with an indirect relationship from recession period. That is, due to recession period, the vacant housing units started to increase as people could not afford the prices and hence housing prices took a hit and was reduced.
* But the market gradually went up, and recently there is a change in the trend where there are less housing units and demand is more and hence prices have exponentially shook up.

##### 3) MNMFS, Median Number of Months on Sales Market for Newly Completed Homes:

###### Visualization:

![MNMFS.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/MNMFS.png "MNMFS.png")

**Explanation:**

* This factor shows how many months typically a housing unit could be present in the market before going on sale.
* During recession 2008-09 period houses were more in market as people could not purchase due to lack of funds and hence to keep business going at a certain pace, prices were reduced which can be clearly seen.
* Then housing units starting selling fast and hence costs went exponentially up.

##### 4) MSACSR, Monthly Supply of New Houses in the United States:

###### Visualization:

![MSACSR.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/MSACSR.png "MSACSR.png")

**Explanation:**

* This shows monthly supply of houses to the market. It can be clearly seen during recession period 2008-09 similar plot can be seen as that of above factor.
* But later even when the houses supply was moderate the prices were exponentially growing.

##### 5) NHSDPTS, New Houses Sold by Stage of Construction, Total:

###### Visualization:

![NHSDPTS.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/NHSDPTS.png "NHSDPTS.png")

**Explanation:**

* Initially there are a lot of homes which are partially, completely or not constructed at all. The prices gradually for all these homes started increasing gradually.
* Due to recession, houses probably stopped being constructed at same pace as that of initial case, but then again it gradually picked up.
* Recently prices have been exponential because of limited supply, but more demand.

##### 6) PERMIT, New Privately-Owned Housing Units Authorized in Permit-Issuing Places: Total Units:

###### Visualization:

![PERMIT.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/PERMIT.png "PERMIT.png")

**Explanation:**

* This also holds similar explanation to other factors mentioned above and almost similar to 1st factor mentioned in this list.

## Demand Factors:

##### 1) ASPUS, Average Sales Price of Houses Sold for the United States:

###### Visualization:

![ASPUS.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/ASPUS.png "ASPUS.png")

**Explanation:**

* Since Average prices of houses are directly related to home price index, they almost go hand-in-hand for all quarters of the year.

##### 2) INTDSRUSM193N, Interest Rates, Discount Rate for United States:

###### Visualization:

![INTDSRUSM193N.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/INTDSRUSM193N.png "INTDSRUSM193N.png")

**Explanation:**

* This factor is having indirect relationship with home price index. This basically indicates that, if interest rates are low, then more people tend to buy homes irrespective of tenure of the home loan.
* This fact can be significantly observed in above image.
* This loan need not be a mortgage loan, because people can submit any other valuables like gold, car, etc. as collateral for loan purpose and hence it is necessary to consider this factor.

##### 3) LREM25TTUSM156S, Employment Rate: Aged 25-54: All Persons for the United States:

###### Visualization:

![LREM25TTUSM156S.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/LREM25TTUSM156S.png "LREM25TTUSM156S.png")

**Explanation:**

* Until an exponential growth in home price index is observed in above image, both Employment Rate and home price index go with each other in trends, which shows in case of recession time period as well.
* But during exponential growth home price index values are more than employment rate values even though they might be growing at the same pace.
* Hence, it can thought as people getting employed to specifically achieve building homes in their career.

##### 4) MORTGAGE30US, 30-Year Fixed Rate Mortgage Average in the United States:

###### Visualization:

![MORTGAGE30US.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/MORTGAGE30US.png "MORTGAGE30US.png")

**Explanation:**

* Mortgage is where the loan is taken on something and is pledged as collateral. Typically home loans happen to be mortgage loans and its rate plays a significant role.
* Initially mortgage rates are pretty high when compared to home prices and this might be due to less demand in housing, but mortgage rates almost had little fluctuations later, resulting in people investing in homes maybe due to its stability, thereby increasing home prices.
* There can be a decline seen in mortgage and this is when home prices started growing exponentially. But then a gradual fluctuation can be seen in both mortgage and home prices as well.

##### 5) TTLCONS, Total Construction Spending: Total Construction in the United States:

###### Visualization:

![TTLCONS.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/TTLCONS.png "TTLCONS.png")

**Explanation:**

* Total construction spending includes construction of all types of infrastructure like schools, hospitals, etc. which are necessary concerns before deciding upon location of home for any person.
* Therefore home prices and this factor go hand-in-hand because demand for homes automatically increases when there are such facilities around a home location which can be clearly seen in above image.

##### 6) UMCSENT, University of Michigan: Consumer Sentiment:

###### Visualization:

![UMCSENT.png](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/images/UMCSENT.png "UMCSENT.png")

**Explanation:**

* This measures the level of confidence and sentiment among U.S. consumers regarding the state of the economy, in this case it is about home prices growth over the years and its future. Typically involves showing if they have the confidence to invest and if it is possible for them.
* The plot image shows intially that as home prices went up, consumers had confidence that it might go up more. Similarly, when it started dropping due to recession during 2008-09, confidence started reducing,  and fear of investing started.
* Then similar to that of initial phase happened. But when prices started growing exponentially, confidence drastically decreased probably due to the difficulty in investing because of sky-rocketting prices.
