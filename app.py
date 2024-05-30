from dotenv import load_dotenv
load_dotenv() #load all the environment variable

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# configure our API key 
genai.configure(api_key=os.getenv("GOOGLE_APT_KEY"))

# Function to load Google Gemini Model and provide sql query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

# Function to retrieve query from the sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
       print(row)
    return rows 

# define the proper prompt

prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name Employee and has the following columns - Employeeid,Name, Department, Salary, City
    \n\nFor example, \nExample 1 - How many entries of records are present?
    The SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all the Employee in Data Science Department?
    The SQL command will be something like this SELECT * FROM Employee
    where Department="Data Science";
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

# Streamlit App
st.set_page_config(page_title="To Retrive Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"Employee.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)


