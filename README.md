# Linear-regressions-using-instrumental-variables-2SLS-case-

The IV estimator can potentially solve endogeneity problems in much the same way as a randomized experiment but you need to find a valid instrument.
We need two assumptions for a valid IV:
1) There must be correlation between z and x conditional on all other variables in a system.
2) The variable can be excluded from the main equation of interest. Two important parts to this assumption:
The only relationship between z and y is through the first stage relationship and the instrument is as good as randomly assigned (Conditional on covariates).

The process for the 2SLS is : 
In the first stage, a new variable is created using the instrument variable.
The second stage then uses the model estimated values from stage one instead of the actual values of the problematic predictors to calculate the OLS model.

First stage  : X = a0 + a1*Z + a2*W + v
Second stage : Y = B0 + B1*X + B2*W + e

being v,e the error terms, Z the instrument, X the treatment and X in the second stage being the predicted values of X, Y the outcome and W the controls.

If the instrument is exogenous (which is assumed), the estimated value will not be correlated with the error term.
