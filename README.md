# Does protection of property rights lead to growth? Linear Regressions using Instrumental Variables (2SLS case)

Property rights are in the Universal Declaration of Human Rights and respecting it might lead to an increment not only in the conception of ethics but also in economical factors. I tested the hypothesis of whether the protection of property rights leads to economical growth using a linear regression. The problem that sometimes appears with linear regression is endogenity, which is when an independent variable is correlated with the error term. The IV estimator can potentially solve endogeneity problems in much the same way as a randomized experiment but you need to find a valid instrument.

Growth should be correlated with the level of contemporary per capita income. In the study of AJR, it is suggested that using the mortality of European colonial settlers as an instrument for property rights protection. This is because European imperial powers set up different institutions in various countries depending on whether they decided to settle there or whether they decided simply to exploit the natural resources of the colony.

We need two assumptions for a valid IV:
1) There must be correlation between z and x conditional on all other variables in a system.
2) The variable can be excluded from the main equation of interest. Two important parts to this assumption:
The only relationship between z and y is through the first stage relationship and the instrument is as good as randomly assigned (Conditional on covariates).

The process for the 2SLS is : 
In the first stage, a new variable is created using the instrument variable.
The second stage then uses the model estimated values from stage one instead of the actual values of the problematic predictors to calculate the OLS model.

First stage  : X = A0 + A1*Z + A2*W + v

Second stage : Y = B0 + B1*X + B2*W + e

being v,e the error terms, Z the instrument, X the treatment and X in the second stage being the predicted values of X, Y the outcome and W the controls.
If the instrument is exogenous (which is assumed), the estimated value will not be correlated with the error term.

