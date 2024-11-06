import streamlit as st
from Feature_01 import return_even 

from Feature_02 import return_odd

original_list = [i for i in range(10)]

even_list = return_even(original_list)

odd_list = return_odd(original_list)

st.write("Hooray it fking works")

st.write("This will be the place where the app is coded in")

st.write(even_list)

st.write(odd_list)

st.write("why isn't it updating??")

