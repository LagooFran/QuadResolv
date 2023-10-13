import streamlit as st
import quadSolver as q
import time
import mpld3
import streamlit.components.v1 as components

#Set wide mode as default
st.set_page_config(layout="wide")

#Add custom styles using style.css file
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

#Hide streamlit default header and footer
st_style = """
        <style>
        #MainMenu {visibility: visible;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(st_style, unsafe_allow_html=True)


#Code used later to show the user what the app has been up to
code = """ #Code used to solve the formula (using cmath lib)
                
def solveQuad(a,b,c): #The data you enter into the side panel

discriminant = (b**2) - (4*a*c)
x1 = (-b-cmath.sqrt(discriminant))/(2 * a)  
x2 = (-b + cmath.sqrt(discriminant))/(2 * a)

return x1, x2 #What you get on screen
"""

#Sidebar setup
with st.sidebar:   
    st.title('QuadResolv')
    st.latex('ax^2 + bx + c')
    a = st.text_input('a')
    b = st.text_input('b')
    c = st.text_input('c')
    quadForm = r"x = \frac {-b \pm \sqrt {b^2 - 4ac}}{2a}"
    st.latex(quadForm)
    solveButton = st.button('Solve')



#Main web panel
if solveButton == False:
    defaultText = st.empty()
    with defaultText.container():
        st.title('Parameters to solve the quadratic formula have not been added yet')
        st.subheader('Add parameters by completing the form in the side pannel.')
if solveButton == True:
    defaultText = st.empty()
    try:
        with st.spinner('Asking Bhaskara...'):
            time.sleep(4)
            answer, graph, = st.columns(2)
            with answer:
                x1, x2 = q.solveQuad(int(a),int(b),int(c))
                st.title('Results of the formula:')
                st.subheader('Places where the line touches the x axis.')
                st.title(f'X1: {x1}')
                st.title(f'X2: {x2}')
                st.code(code, 'python')
            with graph:
                st.title('Graph')
                st.subheader('Generated using matplotlib')
                fig = q.createGraph(int(a),int(b),int(c))
                st.pyplot(fig)
    except:
        st.title('Invalid parameters detected, please try again')