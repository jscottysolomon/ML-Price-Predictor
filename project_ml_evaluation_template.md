#### SERX94: Machine Learning Evaluation
#### Analyzing Actively Manged Mutual Funds
#### Scotty Solomon
#### 20-Nov-2023

## Basic Information

For the original model, each fund has it's own model. The thought process was that each model would be based off of the historical performance of that specific fund.

## Evaluation Metrics

### Mean Squared Error(MSE)

**Choice Justification:** This compares the difference between expected and actual for training data. This was chosen since, ideally, models would have lower scores. 

**Interpretation:** TODO


### Mean Absolute Error
**Choice Justification:** So this statistic works in tandem with the MSE to gage the average absolute difference between the true output and expected output. This was chosen to see, on average, how close the predictions actually were to the actual value. This could be used to gage the average dollar amount that each model could be off by in each prediction.

**Interpretation:** TODO

## Alternative Models
### Polynomial
**Construction:** This version of the model essentially uses polynomial linear regression rather than the standard builtin regression.

**Evaluation:** This version of the model did bad. I was essentially just thinking "well what if i tried this" but it was evidently a bad idea and as it turns out it resulted in poor models. The mse highs and lows are about double what they are from the original models and the mae is usually twice as large.

### Lagged
**Construction:** So this version of the model uses "lagged" values of the fund as output. So the the input is not just the current date but the opening amount of the previous month. Construction was largely the same, except that an additional variable was used.

**Evaluation:** This one did actually preform better than the original; however, I'm not sure that the way it was tested was reasonable. It was given the test dates as well as the real test lagged input, so of course it would be more accurate because it already has a baseline of exactly how well it just preformed. However, I think that this model might be promising. It would have to essentially be used to generate data points one at a time, where the y output would go into the x input as a lagged input, though this remains untested.

### Collective
**Construction**: This model is very different from the other models and was largely created from the ground up. The idea of this model is that rather than creating one model for each fund, it's creating one model across every fund. It takes in the date and the ytd appreciation for the month and outputs the expected appreciation for the next month.

**Evaluation**: This model seems to be less inclined to overfit, which is a struggle that some of the alternative models run into. However, the year to date appreciation might not be the best input. 


## Best Model
I think that the lagged model might be the best model. The way the model is set up, it could be further expanded into a bigger model that's similar to the collective model in that it could be used across several different funds.