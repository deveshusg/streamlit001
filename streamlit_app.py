import streamlit as st
import pandas as pd
st.title('Streamlit Intro')
st.header('Header')
st.subheader('Subheader')
st.text('Text')
st.write('Streamlit is s python framework for web applicstions.')
st.markdown('**Hello** *World*')
st.markdown('> Blockquote')
st.markdown('>> Blockquote')
st.markdown('---')
st.markdown('[Google](https://www.google.com)')
#st.markdown('![alt text](image.jpg)')
st.caption('caption')
st.latex(r'\begin{pmatrix}a&b\\c&d\end{pmatrix}')
code=("""
        import numpy as np
        array=np.array(1,2,3,4,5,6,7,8,9,10).reshape(5,2)
        new_array=array*2
      """)
st.code(code,language="python")
st.metric(label="Wind Speed",value="120ms-1",delta="1.4ms-1")
table=pd.DataFrame({"Column 1":[1,2,3,4,5],"Column 2":[6,7,8,9,10]})
st.table(label="Example Table",table)
