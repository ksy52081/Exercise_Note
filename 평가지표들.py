

### R2 MAE MAPE 평가 지표들  
### Method 1 :  MSE ###
"""MSE 공식 : sqrt [(1/측정한 데이터수) * 더하기((예측값-실측값)^2)]"""

from sklearn.metrics import mean_squared_error
print("MSE(train)")
y_predLR = LR.predict(train_X)
lin_mse = mean_squared_error(train_Y1, y_predLR)
lin_rmse = np.sqrt(lin_mse)
print (lin_rmse)

print("MSE(test)")
y_predLR = LR.predict(test_X)
lin_mse = mean_squared_error(test_Y1, y_predLR)
lin_rmse = np.sqrt(lin_mse)
print (lin_rmse)

### Method 2 : R-square ###
''' R2 공식 : 다 더하기(예측값의 편차^2) / 다 더하기(편차 ^2) 
예측값의 편차 : 예측값 - 실측값의 평균값
편차 : 실측값 - 실측값의 평균값
'''
from sklearn.metrics import r2_score
##y_predLR = LR.predict(test_X)

print("R2-score(train)")
y_predLR = LR.predict(train_X)
print(r2_score(train_Y1, y_predLR))

print("R2-score(test)")
y_predLR = LR.predict(test_X)
print(r2_score(test_Y1, y_predLR))

## Method 3 : MAE
''' MAE 공식 : (1/측정한 데이터수) * 더하기|(예측값-실측값)|'''
from sklearn.metrics import mean_absolute_error
y_true
y_pred
MAE = mean_absolute_error(y_true, y_pred)


### Method 4 : MAPE
'''MAPE 공식 : (100/측정한 데이터수) *더하기[|(실측값-예측값)/실측값|]'''
from sklearn.utils import check_arrays
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = check_arrays(y_true, y_pred)
    return np.mean(np.abs((y_true, y_pred)/y_true))*100
MAPE = mean_absolute_percentage_error(y_true, y_pred)

#### Method 5 : MASE Mean Absolute Scaled Error
