import streamlit as st
import app as app_main
import sklearn

# Page title
st.header('Predict Your Chances for Admission')

# Sidebar
gre_score = st.text_input('GRE Score')
toefl_score = st.text_input('TOEFL Score')
sop_score = st.text_input('SOP Score')
lor_score = st.text_input('LOR Score')
cgpa = st.text_input('CGPA')
university_rating = st.text_input('University Rating')
is_research = st.checkbox('Is Research')

# Format the Data.
# gre_score = float(gre_score if gre_score != '' else 0)
# toefl_score = float(toefl_score if toefl_score != '' else 0)
# sop_score = float(sop_score if sop_score != '' else 0)
# lor_score = float(lor_score if lor_score != '' else 0)
# cgpa = float(cgpa if cgpa != '' else 0)
# university_rating = float(university_rating if university_rating != '' else 0)
# is_research = int(is_research if is_research != '' else 0)

if st.button('Predict'):
    st.markdown(
        """
        ---
        """
    )
    pred_arr = [gre_score,toefl_score,university_rating,sop_score,lor_score,cgpa,is_research]

    has_empty = False

    for i in pred_arr:
        if i=='':
            has_empty = True
            st.error('Enter all the Fields')
            break
    if has_empty == False:
        # Make all Floats..
        floats_pred_arr = list(map(lambda a : float(a),pred_arr))
        predictions = app_main.predict_models(floats_pred_arr)
        
        for pred in predictions:
            print(predictions)
            if pred in app_main.prev_perc_values:
                pass
            else:
                app_main.prev_perc_values[pred] = 0

        
        # st.header(str(''+str(round(prediction[0],6) * 100)+'%'))
        # st.text(predictions)
        
        for pred in predictions:
            perc_value = predictions[pred]

            perc_value = round(float(perc_value),6)
            app_main.prev_perc_values[pred] = round(float(app_main.prev_perc_values[pred]),6)

            st.metric("Your Chance of Admission is",
                str(float(perc_value)* 100)+'%',
                str((perc_value - app_main.prev_perc_values[pred]) * 100)+'%')
            app_main.prev_perc_values[pred] = perc_value
else:
    st.info('Click the Predict Button to show results.')