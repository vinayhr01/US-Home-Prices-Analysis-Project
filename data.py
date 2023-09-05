'''
GDP.csv ---> GDP ---> Seasonally adjusted
LREM64TTUSM156S.csv ---> Employment Rate: Aged 15-64: All Persons for the United States ---> Seasonally adjusted
UMCSENT.csv ---> University of Michigan: Consumer Sentiment ---> Not Seasonally adjusted
MORTGAGE30US.csv ---> 30-Year Fixed Rate Mortgage Average in the United States ---> Not Seasonally adjusted
TTLCONS.csv ---> Total Construction Spending: Total Construction in the United States ---> Seasonally adjusted
ASPUS.csv ---> Average Sales Price of Houses Sold for the United States	---> Not Seasonally adjusted
HOUST.csv ---> New Privately-Owned Housing Units Started: Total Units ---> Seasonally adjusted
MSACSR.csv ---> Monthly Supply of New Houses in the United States ---> Seasonally Adjusted
PERMIT.csv ---> New Privately-Owned Housing Units Authorized in Permit-Issuing Places: Total Units ---> Seasonally adjusted
HSN1F.csv ---> New One Family Houses Sold: United States ---> Seasonally adjusted
MSPNHSUS.csv ---> Median Sales Price for New Houses Sold in the United States ---> Not Seasonally Adjusted
UNDCONTSA.csv ---> New Privately-Owned Housing Units Under Construction: Total Units ---> Seasonally adjusted
LFWA64TTUSM647S.csv ---> Working Age Population: Aged 15-64: All Persons for the United States ---> Seasonally Adjusted
COMPUTSA.csv ---> New Privately-Owned Housing Units Completed: Total Units ---> Seasonally adjusted
LREM25TTUSM156S.csv ---> Employment Rate: Aged 25-54: All Persons for the United States ---> Seasonally adjusted
NHSUSSPT.csv ---> New Houses Sold by Sales Price in the United States, Total ---> Not Seasonally adjusted
LRUN64TTUSM156S.csv ---> Unemployment Rate: Aged 15-64: All Persons for the United States ---> Seasonally Adjusted
LFWA25TTUSM647S.csv ---> Working Age Population: Aged 25-54: All Persons for the United States ---> Seasonally Adjusted
NHFSEPCS.csv ---> New Houses for Sale by Stage of Construction, Completed ---> Seasonally Adjusted
AUTHNOTTSA.csv ---> New Privately-Owned Housing Units Authorized but Not Started: Total Units ---> Seasonally adjusted
NHFSEPUCS.csv ---> New Houses for Sale by Stage of Construction, Under Construction ---> Seasonally adjusted
NHSDPTS.csv ---> New Houses Sold by Stage of Construction, Total ---> Seasonally adjusted
MNMFS.csv ---> Median Number of Months on Sales Market for Newly Completed Homes ---> Not Seasonally Adjusted
TLRESCONS.csv ---> Total Construction Spending: Residential in the United States ---> Seasonally Adjusted
RRVRUSQ156N.csv ---> Rental Vacancy Rate in the United States ---> Not Seasonally adjusted
EVACANTUSQ176N.csv ---> Housing Inventory Estimate: Vacant Housing Units in the United States ---> Not Seasonally adjusted
RHVRUSQ156N.csv ---> Homeowner Vacancy Rate in the United States ---> Not Seasonally Adjusted
ERENTUSQ176N.csv ---> Housing Inventory Estimate: Vacant Housing Units for Rent in the United States ---> Not Seasonally adjusted
ESALEUSQ176N.csv ---> Housing Inventory Estimate: Vacant Housing Units for Sale in the United States ---> Not Seasonally Adjusted
EOFFMARUSQ176N.csv ---> Housing Inventory Estimate: Vacant Housing Units Held Off the Market in the United States ---> Not Seasonally Adjusted
INTDSRUSM193N.csv ---> Interest Rates, Discount Rate for United States ---> Not Seasonally adjusted
MSPUS.csv ---> Median Sales Price of Houses Sold for the United States ---> Not Seasonally adjusted
ASPNHSUS.csv ---> Average Sales Price for New Houses Sold in the United States ---> Not Seasonally Adjusted
'''


'''
CSUSHPISA.csv ---> S&P/Case-Shiller U.S. National Home Price Index ---> Seasonally adjusted
'''

data_tuples = [
    ('GDP.csv', 'GDP'),
    ('LREM64TTUSM156S.csv', 'Employment Rate: Aged 15-64: All Persons for the United States'),
    ('UMCSENT.csv', 'University of Michigan: Consumer Sentiment'),
    ('MORTGAGE30US.csv', '30-Year Fixed Rate Mortgage Average in the United States'),
    ('TTLCONS.csv', 'Total Construction Spending: Total Construction in the United States'),
    ('ASPUS.csv', 'Average Sales Price of Houses Sold for the United States'),
    ('HOUST.csv', 'New Privately-Owned Housing Units Started: Total Units'),
    ('MSACSR.csv', 'Monthly Supply of New Houses in the United States'),
    ('PERMIT.csv', 'New Privately-Owned Housing Units Authorized in Permit-Issuing Places: Total Units'),
    ('HSN1F.csv', 'New One Family Houses Sold: United States'),
    ('MSPNHSUS.csv', 'Median Sales Price for New Houses Sold in the United States'),
    ('UNDCONTSA.csv', 'New Privately-Owned Housing Units Under Construction: Total Units'),
    ('LFWA64TTUSM647S.csv', 'Working Age Population: Aged 15-64: All Persons for the United States'),
    ('COMPUTSA.csv', 'New Privately-Owned Housing Units Completed: Total Units'),
    ('LREM25TTUSM156S.csv', 'Employment Rate: Aged 25-54: All Persons for the United States'),
    ('NHSUSSPT.csv', 'New Houses Sold by Sales Price in the United States, Total'),
    ('LRUN64TTUSM156S.csv', 'Unemployment Rate: Aged 15-64: All Persons for the United States'),
    ('LFWA25TTUSM647S.csv', 'Working Age Population: Aged 25-54: All Persons for the United States'),
    ('NHFSEPCS.csv', 'New Houses for Sale by Stage of Construction, Completed'),
    ('AUTHNOTTSA.csv', 'New Privately-Owned Housing Units Authorized but Not Started: Total Units'),
    ('NHFSEPUCS.csv', 'New Houses for Sale by Stage of Construction, Under Construction'),
    ('NHSDPTS.csv', 'New Houses Sold by Stage of Construction, Total'),
    ('MNMFS.csv', 'Median Number of Months on Sales Market for Newly Completed Homes'),
    ('TLRESCONS.csv', 'Total Construction Spending: Residential in the United States'),
    ('RRVRUSQ156N.csv', 'Rental Vacancy Rate in the United States'),
    ('EVACANTUSQ176N.csv', 'Housing Inventory Estimate: Vacant Housing Units in the United States'),
    ('RHVRUSQ156N.csv', 'Homeowner Vacancy Rate in the United States'),
    ('ERENTUSQ176N.csv', 'Housing Inventory Estimate: Vacant Housing Units for Rent in the United States'),
    ('ESALEUSQ176N.csv', 'Housing Inventory Estimate: Vacant Housing Units for Sale in the United States'),
    ('EOFFMARUSQ176N.csv', 'Housing Inventory Estimate: Vacant Housing Units Held Off the Market in the United States'),
    ('INTDSRUSM193N.csv', 'Interest Rates, Discount Rate for United States'),
    ('MSPUS.csv', 'Median Sales Price of Houses Sold for the United States'),
    ('ASPNHSUS.csv', 'Average Sales Price for New Houses Sold in the United States'),
    ('CSUSHPISA.csv', 'S&P/Case-Shiller U.S. National Home Price Index')
]
