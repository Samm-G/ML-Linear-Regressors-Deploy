# Imports
import yaml
import flask_app
import os
import pickle

# Local Imports
import prediction

# Params..
app = ''
frontend_app_server = ''

# Global Params..
prev_perc_values = {}

def get_app_params():
    """Loads the app_params.yml and sets the Appserver for Frontend. Options are Flask and Streamlit.
    """
    with open('app_params.yaml','r') as file:
        app_params = yaml.safe_load(file)

    file.close()
    return app_params

def predict_models(input_data):
    return prediction.predict_models([input_data])

if __name__ == "__main__":
    # # initializing a flask app
    #app.run(host='127.0.0.1', port=8001, debug=True)
    #app.run(debug=True) # running the app
    
    params = get_app_params()
    
    if params['app_server_type'] == 'Flask':
        flask_app.start_app()
    if params['app_server_type'] == 'StreamLit':
        os.system('streamlit run streamlit_app.py')
    pass

