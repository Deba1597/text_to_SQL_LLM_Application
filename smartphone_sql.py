from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai 

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# FUNCTION to load google gemini model

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

#function to retrive query from data base
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# define prompts
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name  smartphone and has the following columns - 
    'brand_name', 'model', 'price', 'rating', 'has_5g', 'has_nfc',
    'has_ir_blaster', 'processor_brand', 'num_cores', 'processor_speed',
    'battery_capacity', 'fast_charging_available', 'fast_charging',
    'ram_capacity', 'internal_memory', 'screen_size', 'refresh_rate',
    'num_rear_cameras', 'num_front_cameras', 'os', 'primary_camera_rear',
    'primary_camera_front', 'extended_memory_available', 'extended_upto',
    'resolution_width', 'resolution_height' \n\nFor example,\n
    Example 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM smartphone ;
    \nExample 2 - Tell me all the smartphone from database?, 
    the SQL command will be something like this SELECT * FROM smartphone; 
    also the sql code should not have ``` in beginning or end and sql word in output
    and also remember that all feature/column name are in lower case only.

    """



]


st.set_page_config(page_title='i can retrive ant SQL query')

st.header("Gemini app to retrive SQL Database")

question = st.text_input('Input: ', key='input')

submit = st.button("Ask any question")
# is submit is clicked
if submit:
    response1 = get_gemini_response(question, prompt)
    print(response1)
    response = read_sql_query(response1, 'smartphone.db')
    st.subheader("The response is")
    for row in response:
        #print(row)
        st.header(row)


