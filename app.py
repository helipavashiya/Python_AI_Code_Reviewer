from openai import OpenAI
import streamlit as st

# Read the API key and set up OpenAI Client
f = open("keys/key.txt")
key =  f.read()
client = OpenAI(api_key=key)

st.title("💬An AI Code Reviewer")
# take user input
prompt = st.text_area("Enter your python code here:")

# if the button is submitted or clicked, generate response
if st.button("Generate") == True:
    response = client.chat.completions.create(
                      model="gpt-3.5-turbo",
                      messages=[
                        {"role": "system", "content": """You are pyhton code reviewer assistant working with an company as a Python Developer. 
                                        Your job here is to analyze the given prompt, identify potential bugs, errors, or areas of improvement required.
                                        Display a "Code Review"  report and in next lines displays all bugs under "Bugs Report" and correct code under"Fixed Code".
                                        You are know to be polite and helpful AI bot. 
                                        Dipslay the Code Review, Bugs Report and Fixed Code in in a bold fonts.
                                        st.write("").
                                        If the doubt is not relevant to python language you can politely ask the user for providng another prompt.
                                        """},
                        {"role": "user", "content": prompt}
                      ]
                )
    # Print the response on the webapp
    st.write(response.choices[0].message.content)