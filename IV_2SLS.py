import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from linearmodels import IV2SLS
from statsmodels.api import add_constant

url = "https://github.com/MartinFrancoIrabedra/Linear-regressions-using-instrumental-variables-2SLS-case-/blob/main/Data/ajr.dta"
data = pd.read_stata(url, index_col=0)
data.to_csv(url)
print(data)

#### OLS regression of loggdp on risk.
#### risk indicating the protection of property rights.
#### Log of GDP per capita is called loggdp.

x1 = data.risk
x1 = sm.add_constant(x1) 

y = data.loggdp


model_1 = sm.OLS(y,x1)
results_1 = model_1.fit().get_robustcov_results(cov_type = "HC1")
print(results_1.summary())




#### First stage for logmort0 to determine risk.
#### logmort0 being the log of European settler mortality.

x2 = data.logmort0
x2 = sm.add_constant(x2)

y2 = data.risk


#### OLS regression on the first stage using logmort0 as an independent variable
#### and risk as a dependent variable.

model_2 = sm.OLS(y2,x2)
results_2 = model_2.fit().get_robustcov_results(cov_type = "HC1")
print(results_2.summary())


#### Check the regression for loggdp using logmort0 as an independent variable 
#### and loggdp as a dependent variable.

x3 = data.logmort0
x3 = sm.add_constant(x3) 

y3 = data.loggdp


model_3 = sm.OLS(y3,x3)
results_3 = model_3.fit().get_robustcov_results(cov_type = "HC1")
print(results_3.summary())


#### Second stage of the 2SLS using logmort0 as an instrument.
data = add_constant(data)

IV = IV2SLS(dependent = data["loggdp"], exog = data["const"], endog = data["risk"], instruments = data["logmort0"]).fit()
print(IV)



##### OLS regression as before but adding malaria as a regressor.

##### The reason of this is that a critic of these regressions is worried that
##### the current level of GDP is correlated with the disease environment in a country,
##### which in turn will be correlated with European settler mortality in the 1800s.

##### First stage using logmort0 as an independent variable 
##### and risk as a dependent variable including malaria as a regressor.

x4 = pd.concat([data.logmort0,data.malaria],axis = 1)
x4 = sm.add_constant(x4) 

y4 = data.risk

model_4 = sm.OLS(y4,x4)
results_4 = model_4.fit().get_robustcov_results(cov_type = "HC1")
print(results_4.summary())


x5 = pd.concat([data.risk,data.malaria], axis = 1)
x5 = sm.add_constant(x5)

y5 = data.loggdp

model_5 = sm.OLS(y5,x5)
results_5 = model_5.fit().get_robustcov_results(cov_type = "HC1")
print(results_5.summary())

#### Second stage of the 2SLS

IV_2 = IV2SLS(dependent = data["loggdp"], exog = data[["const","malaria"]], endog = data["risk"],instruments = data["logmort0"]).fit()
print(IV_2)

























































































