import streamlit as st
with st.sidebar:
    st.radio('Select operation:', ["Operators","List","Tuples","Dictionary"])
st.title("Basic Python Operators: ")
st.write("Arithmetic Operators: \n This are used for performing mathematical operations such as Addition, Multiplication, Division etc.")
st.subheader('Program for simple Arithmetic operation:')
st.write("-----------------------------------------------------------------------")

#=====================================================
st.write("**Sum Operator:**")
st.write("Question No.1 ➡ Write a program for sum of below given values:")
value1 = 45
value2 = 50
Sum = value1+value2
st.code(">>> value1 = 45 \n>>> value2 = 50 \n>>> Sum = value1 + value2 \n >>> print(Sum)  or \n >>> print(value1 + value2)")
if st.button('Output of Q1'):
    st.code(Sum)
#======================================================
st.write("Question No.2 ➡ Write a program for substraction of below given values:")
value1 = 100
value2 = 50
Substraction = value1-value2
st.code(">>> value1 = 100 \n>>> value2 = 50 \n>>> Substraction = value1 - value2 \n >>> print(Subtraction)  or \n >>> print(value1 - value2)")
if st.button('Output of Q2'):
    st.code(Substraction)
#======================================================
st.write("Question No.3 ➡ Write a program for Multiplication of below given values:")
value1 = 45
value2 = 5
Mul = value1*value2
st.code(">>> value1 = 45 \n>>> value2 = 5 \n>>> Multiplication = value1 * value2 \n >>> print(Multiplication)  or \n >>> print(value1 * value2)")
if st.button('Output of Q3'):
    st.code(Mul)
#======================================================
st.write("Question No.4 ➡ Write a program for Division of below given values:")
value1 = 45
value2 = 5
Div = value1/value2
st.code(">>> value1 = 45 \n>>> value2 = 5 \n>>> Division = value1 / value2 \n >>> print(Division)  or \n >>> print(value1 / value2)")
if st.button('Output of Q4'):
    st.code(Div)
#=======================================================
st.write("Question No.5 ➡ Write a program for floor Division of below given values:")
value1 = 100
value2 = 10
F_Div = value1//value2
st.code(">>> value1 = 100 \n>>> value2 = 10 \n>>> Floor_Division = value1 // value2 \n >>> print(Floor_Division)  or \n >>> print(value1 // value2)")
if st.button('Output of Q5'):
    st.code(F_Div)
#=======================================================
st.write("Question No.6 ➡ Write a program for Exponentiation of below given values:")
value1 = 5
value2 = 3
Expo = value1**value2
st.code(">>> value1 = 5 \n>>> value2 = 3 \n>>> Exponentiation = value1 ** value2 \n >>> print(Exponentiation)  or \n >>> print(value1 ** value2)")
if st.button('Output of Q6'):
    st.code(Expo)
#========================================================
st.write("Question No.7 ➡ Write a program for Modulus of below given values:")
value1 = 100
value2 = 5
mod = value1/value2
st.code(">>> value1 = 100 \n>>> value2 = 5 \n>>> Modulus = value1 ** value2 \n >>> print(Modulus)  or \n >>> print(value1 % value2)")
if st.button('Output of Q7'):
    st.code(mod)
st.write("------------------------------------------------------------------------")
