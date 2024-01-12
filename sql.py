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
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

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
    response = read_sql_query(response1, 'student.db')
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)


