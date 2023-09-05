# Delete similar factors based on their meaning, correlation values and variance inflation values considered above 300

import pandas as pd

'''
The correlation values are with respect to S&P/Case-Shiller home price index provided to consider.

Similar factors can lead to multicollinearity hence dropping them is good.

1) Factor:
    ASPNHSUS (0.9569) - Average Sales Price for New Houses Sold in the United States
    ASPUS (0.9553) - Average Sales Price of Houses Sold for the United States
    Dropping: ASPNHSUS
    Reason: These two factors have almost the same correlation and are likely measuring very similar aspects of the housing market. Both are highly correlated with home prices, but we can retain ASPUS, which is also correlated at 0.9553, to avoid redundancy, as ASPUS gives aspect of average prices of all houses.

2) Factor:

    LFWA64TTUSM647S (0.5936) - Working Age Population: Aged 15-64: All Persons for the United States
    LFWA25TTUSM647S (0.7966) - Working Age Population: Aged 25-54: All Persons for the United States
    Dropping: LFWA64TTUSM647S
    Reason: These two factors are correlated, but LFWA25TTUSM647S is more closely related to the prime working-age population (25-54), which is a critical demographic for the housing market. Therefore, we can retain LFWA25TTUSM647S and neglect LFWA64TTUSM647S to avoid redundancy and also people from age 15-25 mostly are involved in education than house purchasing activities.

3) Factor:

    MSPNHSUS (0.9443) - Median Sales Price for New Houses Sold in the United States
    MSPUS (0.9435) - Median Sales Price of Houses Sold for the United States
    Dropping: Both
    Reason: These two factors have almost the same correlation and measure similar aspects of median sales prices for new and existing homes and average prices are considered.

4) Factor:

    HSN1F,0.127644271087494,New One Family Houses Sold: United States
    Dropping: Yes
    Reason: Because there could be 2-family houses or multi-family houses as well.

5) Factor:

    LFWA25TTUSM647S,0.7966487000487664,Working Age Population: Aged 25-54: All Persons for the United States
    LREM25TTUSM156S,0.4221924849974826,Employment Rate: Aged 25-54: All Persons for the United States
    LRUN64TTUSM156S,-0.532962542615867,Unemployment Rate: Aged 15-64: All Persons for the United States
    Dropping: No
    Reason: This indicates working age population and employment rate but also shows moderately quite a few of that age are unemployed and also Employment Rate for ages 25-64 is considered and people of age group 15-25 are mostly students.

6) Factor: 
    NHSUSSPT,0.1239415016908768,"New Houses Sold by Sales Price in the United States, Total"
    Dropping: Yes
    Reason: Price aspect considered.

7) Factor:
    NHFSEPCS,-0.2550396914571141,"New Houses for Sale by Stage of Construction, Completed"
    NHFSEPUCS,0.5499136840549724,"New Houses for Sale by Stage of Construction, Under Construction"
    Dropping: Yes, both
    Reason: Total aspect considered for this.

8) Factor:
    TLRESCONS,0.8952767341669163,Total Construction Spending: Residential in the United States
    TTLCONS,0.98175036826635,Total Construction Spending: Total Construction in the United States
    Dropping: TLRESCONS
    Reason: Total construction spending is more correlated than residential construction spending, most probably due to inclusion of other important buildings construction like schools, hospitals, etc. and not just residential construction and makes people to consider these factors before deciding on a house.

    CONSIDERED DELETING VIF (Variance Inflation) above 300

9) Factor:
    ERENTUSQ176N,-0.7869195412854356,Housing Inventory Estimate: Vacant Housing Units for Rent in the United States
    ESALEUSQ176N,-0.720321468253932,Housing Inventory Estimate: Vacant Housing Units for Sale in the United States
    Dropping: Yes, Both
    Reason: Variance inflation (means increase in the variance of the estimated coefficients in a regression model when the predictor variables in the model are correlated with each other)

'''

