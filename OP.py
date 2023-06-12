import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='LinearFunctionsPlotter!', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title("This website will help you plot linear equations :chart_with_upwards_trend:")
st.write('---')
col1,col2 = st.columns(2)
with col1:
    st.write('##')
    spaces = "\n" * 10
    text = spaces + " y ="
    st.write(text)

with col2:
    equation = st.text_input("Your linear equation (e.g., 2*x + 3):", key="equation_input")


x = np.linspace(-10, 10, 100)
try:
    y = eval(equation)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xticks(np.arange(-10, 11))
    ax.set_yticks(np.arange(-10, 11))
    ax.set_title('Linear Graph: {}'.format(equation))
    st.pyplot(fig)
    ax.grid(True)
except:
    st.error("I think you typed the equation wrong. Check the example carefully! :sob:")

if equation:
    equation



with st.container():
    st.write('---')
    st.header('Get in touch with me! :wave:')
    st.write('##')
    st.write('QUICK INTRO :  My name is Hari, Im 14 years old and i live in Germany. I make python projects for fun')
    st.write('If you want to message me, collaborate or have any ideas for anything')
    st.write('feel free to fill out the form below and i will get back to you shortly.')

    contact_form = """<form action="https://formsubmit.co/harikiran.turla@gmail.com" method="POST">
    <input type = "hidden" name= "_captcha" value ="false">
     <input type="text" name="name"placeholder = "Your name" required>
     <input type="email" name="email"Placeholder= "Your Email" required>
     <textarea name ="message" Placeholder="your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

st.write("write your message for me in that box, maybe its for an improvement.")
