#### SERX94: Experimentation
#### TODO (title)
#### Scotty Solomon
#### 20-Nov-23


## Explainable Records
### Record 1
#### Fund: AABFX
**Raw Data:** 12.97978779 12.98448375 12.98968285 12.99471423 12.99991333 13.00494471
 13.01014381 13.01534291 13.02037429 13.02557339 13.03060477 13.03580387
 13.04100297 13.04569893 13.05089802 13.05592941 13.06112851 13.06615989
 13.07135899 13.07655808 13.08158947 13.08678857 13.09181995 13.09701905
 13.10221814 13.1069141  13.1121132  13.11714458 13.12234368 13.12737507
 13.13257416 13.13777326 13.14280464

Prediction Explanation:** In terms of the domain this output makes sense because experts usually expect for funds to appreciate in price. This predict prices for each month does increase more than the last, but it's not a very big increase. This matches the idea that investment in mutual funds are usually more for long term retirement rather than short term gains.

### Record 2
#### Fund: RYWDX
**Raw Data:** 52.71512646 52.24463563 51.72373506 51.21963774 50.69873717 50.19463984
 49.67373928 49.15283871 48.64874139 48.12784082 47.62374349 47.10284293
 46.58194236 46.11145152 45.59055096 45.08645363 44.56555307 44.06145574
 43.54055518 43.01965461 42.51555728 41.99465672 41.49055939 40.96965883
 40.44875826 39.97826742 39.45736686 38.95326953 38.43236896 37.92827164
 37.40737107 36.88647051 36.38237318

Prediction Explanation:** In terms of the domain the output makes sense because we're seeing a gradual decline in price from month to month. The amount of the drop itself isn't a large amount of money, which makes sense, since most funds won't lose an immense of value over night. Instead, a gradual but continual decline in price makes sense in terms of the domain. 

## Interesting Features
### Feature A
**Feature:** Price Variability

**Justification:** Price variation effects the models since the rate at which a fund increase or decreases effects the overall price of the fund. The models are affected by the variability, since as a fund varies, the output of the model would also need to vary accordingly.

### Feature B
**Feature:** Average Return

**Justification:** The average return of a fund affects the model because the average return of a mutual fund signals what the projected growth might be overtime. 

## Experiments 
### Varying Price
**Prediction Trend Seen:** So one interesting thing is that funds that vary less in price are able to be predicted better and have a lower mse score. However, they have a negative R^2 score, which suggest that these models likely struggle with over fitting. 

### Varying Average Return
**Prediction Trend Seen:** Funds with more consistent returns are able to be predicted better. Although prices from month to month will usually go up or down, the models tend to only go up. Thus, funds that have consistent positive returns are predicted more accurately.

### Varying A and B together
**Prediction Trend Seen:** When price and return are varied together, they usually do not vary much at all. A fund has a steady yearly return, meaning that the month-to-month price of a fund typically goes up.


### Varying A and B inversely
**Prediction Trend Seen:** When price and return are varied inversely, the model struggles to predict the new price accurately. Unless the fund is very consistently loosing money, the models will generally predict a rapid increase in price from month to month (rapid relative to typical price increases. This is usually an increase of $1 to $2.50). This lead to a fund being predicted to be priced vary high at the end of the prediction when in reality the model did not account for the fund losing money, so the predicted value is overestimated.