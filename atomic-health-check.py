import streamlit as st

st.set_page_config(page_title='Atomic Health Check', page_icon='healthcare.png', layout="wide", initial_sidebar_state="auto", menu_items=None)
left, center, right = st.columns(3, gap='medium')

# Introduction message for users
with left:
    st.title("**Welcome to Atomic Health Check**")
    st.markdown('''We provide a *quick* and *simple* health diagnosis based on your current bodily conditions.''')
    st.markdown('''Just fill up the form as best as you can and click the ***Diagnose*** button to view the results.''')
    st.markdown(''':male-doctor: Thank you! :female-doctor:''')

# Form to be filled up by users
with center:
    with st.form('symptoms'):
        temperature = st.number_input('What is your body temperature (Celsius)?', min_value=11.00, max_value=47.00, value=37.00)
        nasal_breathing = st.selectbox(
            'Please describe your nasal breathing.',
            ['Light', 'Heavy']
        )
        st.write('Kindly check the boxes if you have any of the symptoms.')
        col1, col2 = st.columns(2)
        with col1:
            headache = st.checkbox('Headache')
            cough = st.checkbox('Cough')
        with col2:
            sore_throat = st.checkbox('Sore Throat')
            antibiotics_allergy = st.checkbox('Antibiotics Allergy')

        diagnose = st.form_submit_button('Diagnose')

# Diagnosis results based on form input
with right:
    if diagnose:
        fever = 'None'
        nasal_discharge = False
        sinus_membranes_swelling = False
        cold = False
        treat = None
        give_medication = None
        give_tylenol = False
        give_antibiotics = False

        st.subheader('Results :clipboard:')

        if temperature < 37:
            st.write('You have no fever')
        elif temperature <= 38:
            st.write('You have a low fever')
            fever = 'Low'
        else:
            st.write('You have a high fever')
            fever = 'High'

        if nasal_breathing == 'Light':
            st.write('You have nasal discharge')
            nasal_discharge = True
        elif nasal_breathing == 'Heavy':
            st.write('You have sinus membranes swelling')
            sinus_membranes_swelling = True

        if fever == 'Low' and headache and nasal_discharge and cough:
            st.write('You have a cold')
            cold = True

        if cold:
            if not sore_throat:
                treat = False
            else:
                treat = True

        if not treat:
            give_medication = False
        else:
            give_medication = True

        if give_medication:
            if antibiotics_allergy:
                st.markdown('**Take Tylenol for your treatment** :pill:')
                give_tylenol = True
            else:
                st.markdown('**Take Antibiotics for your treatment** :pill:')
                give_antibiotics = True