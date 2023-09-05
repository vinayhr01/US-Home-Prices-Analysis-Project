# US Home Prices Analysis

## Supply and demand factors impacting US home prices over the last 20 years

* Considered time period for all supply and demand factors are from 1st January 2003 to 1st April 2023 have quarter of an year incremented values
* All data are from taken from [Economic Research Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org).
* Considered [S&amp;P/Case-Shiller U.S. National Home Price Index](https://fred.stlouisfed.org/series/CSUSHPISA#) as proxy for home prices.
* Considered 30+ factors (refer [Factors.csv](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/Factors.csv) file for all factors) which could have direct or indirect impact on home prices by searching the data source, [Economic Research Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org) using housing related keywords.

### Procedure followed to filter these 30+ factors to more relevant and less factors

* All factors were initially separate CSV files when downloaded from the source mentioned above, but have been merged and converted into a single CSV file (refer [merged_data.csv](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/merged_data.csv) for CSV file) and since factors have code names, the description of these factors were also considered to form a CSV file (refer [Factors.csv](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/Factors.csv) for CSV file).
* If any factors have less data than time period mentioned above, the missing values are handled by using mean simple imputation method and according to requirements.
* For instance, [Interest Rates, Discount Rate for United States (INTDSRUSM193N)](https://fred.stlouisfed.org/series/INTDSRUSM193N) had 7 values missing and had been filled using mean simple imputation method (refer [MLmodel.py](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/49f7cff5ac010564062e9ea573aca33b851b92b0/MLmodel.py#L19-L31))
* Then found the correlation of all factors with respect to [S&amp;P/Case-Shiller U.S. National Home Price Index](https://fred.stlouisfed.org/series/CSUSHPISA#).
* Based on high correlation values and meaning of the factors, first filtering of a few factors were done and then variance inflation method was applied to further remove factors (refer [multicollinearity.py](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/multicollinearity.py)) thus helping in reducing multicollinearity problem which could arise due to highly correlated predictor and target (refer [delsimfactors.txt](https://github.com/vinayhr01/US-Home-Prices-Analysis-Project/blob/main/delsimfactors.txt) file for factors removal).

### ML Model building

![combined_ASPUS_AUTHNOTTSA_0](images\combined_ASPUS_AUTHNOTTSA_0.png "combined_ASPUS_AUTHNOTTSA_0")![combined_COMPUTSA_EOFFMARUSQ176N_1](images/combined_COMPUTSA_EOFFMARUSQ176N_1.png "combined_COMPUTSA_EOFFMARUSQ176N_1")![1693919852821](image/README/1693919852821.png)![combined_INTDSRUSM193N_LFWA25TTUSM647S_3](images/combined_INTDSRUSM193N_LFWA25TTUSM647S_3.png "combined_INTDSRUSM193N_LFWA25TTUSM647S_3")![combined_LREM25TTUSM156S_LRUN64TTUSM156S_4](images/combined_LREM25TTUSM156S_LRUN64TTUSM156S_4.png "combined_LREM25TTUSM156S_LRUN64TTUSM156S_4")![combined_MNMFS_MORTGAGE30US_5](images/combined_MNMFS_MORTGAGE30US_5.png "combined_MNMFS_MORTGAGE30US_5")![combined_MSACSR_NHSDPTS_6](images/combined_MSACSR_NHSDPTS_6.png "combined_MSACSR_NHSDPTS_6")![combined_PERMIT_RHVRUSQ156N_7](images/combined_PERMIT_RHVRUSQ156N_7.png "combined_PERMIT_RHVRUSQ156N_7")![1693920352495](image/README/1693920352495.png)
