import streamlit as st
st.set_page_config(page_title='ReHash', page_icon='🖖')

from paraphrase import paraphrase
from list_conversion import list_conversion
from style_transfer import style_transfer

st.image('rehash.png', width=200)
st.markdown('An AI-powered rewriting tool')

st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
res=''
# selectbox
option = st.selectbox('Select an option', ['','Paraphrase', 'Simplify', 'List → Paragraph'])
st.markdown("""<p style='font-size: 14px; color: #008080; margin: 0 0 8px'>Enter text here</p>""", unsafe_allow_html=True)
text = st.text_area(label='Enter text here:color[violet]', height=200, key=42, label_visibility='collapsed')

if st.button('Go'):
    if option=='Simplify':
        with st.spinner('Simplifying...'):
            res = style_transfer(text)
    elif option=='List → Paragraph':
        with st.spinner('Converting...'):
            res = list_conversion(text)    
    elif option=='Paraphrase':
        with st.spinner('Paraphrasing...'):
            res = paraphrase(text)
    else:
        st.write('Select an option!')
        res = 'When you select an option, the output will appear here.'

# output text box

st.markdown('---')
st.markdown('<style>div.row-widget.stMarkdown > div{color: white}</style> <small>Magic Area</small>', unsafe_allow_html=True)
output = st.code(str(res), language=None)


clear = st.button('Clear', key=1)
if clear:
    res= ''




# CSS ONLY

css = """
<style>
    .stSelectbox [data-testid='stMarkdownContainer'] {
        color: #008080;
    }

    .stTextArea [data-baseweb=base-input] {
        color: #008080;
    }
    .stTextArea [data-baseweb=base-input] [disabled=""] {
        color: #008080;
    }
    .element-container>stTextArea>div>label>div>p{
        color: #008080;
    }
    small{
        color: #008080;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
}

a:hover,  a:active {
color: red;
background-color: transparent;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='color:#008080; text-decoration:none' href="https://www.linkedin.com/in/meenal-chavan/" target="_blank">Meenal Chavan</a> and <a style='color:#008080; text-decoration:none' href="https://www.linkedin.com/in/abigail-kufeldt-17a934126/ target="_blank">Abigail Kufeldt</a></p>
</div>
"""

st.markdown(footer,unsafe_allow_html=True)

# st.markdown('Made with ❤️ by [Meenal](https://www.linkedin.com/in/meenal-chavan/) & [Abigail](https://www.linkedin.com/in/abigail-kufeldt-17a934126/)')
# st.markdown('Source code: [GitHub]()')