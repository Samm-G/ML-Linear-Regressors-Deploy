# Imports
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge, Lasso, LassoCV, RidgeCV, LarsCV, ElasticNet, ElasticNetCV, LinearRegression
import pickle

# PARAMS..
st_scaler_filepath = 'MLModels/lr_model_scaler.scl'
lr_model_filepath = 'MLModels/lr_model.pkl'
lassocv_model_filepath = 'MLModels/lassocv_model.pkl'
ridgecv_model_filepath = 'MLModels/ridgecv_model.pkl'
elasticnetcv_model_filepath = 'MLModels/elasticnetcv_model.pkl'

## All Models..
predictors = {
        'Linear Regression' : lr_model_filepath,
        'LassoCV Regression' : lassocv_model_filepath,
        'RidgeCV Regression' : ridgecv_model_filepath,
        'ElasticNetCV Regression' : elasticnetcv_model_filepath,
    }


def predict_models(input_data):
    print(input_data)
    # Scale the Data..
    st_scaler = pickle.load(open(st_scaler_filepath, 'rb'))
    st_input_data = st_scaler.transform(input_data)

    # Predict and Return
    predictions = {}
    for pred in predictors:
        predictions[pred] = predict_regression(predictors[pred],st_input_data)
    return predictions

def predict_regression(model_filepath, input_data):
    # Linear Regression..
    model = pickle.load(open(model_filepath, 'rb'))
    return model.predict(input_data)

# Testing..
# predict_models([[324.000000,107.0,4,4,4.5,8.87,1]])