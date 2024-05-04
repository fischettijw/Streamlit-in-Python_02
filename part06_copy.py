import streamlit as st
import pandas as pd

st.title("Hi, I am Streamlit Web App")
st.subheader("I am your Subheader")
st.header("I am Header")
st.text("Hi, I am the text function")
st.markdown("**Hello** World")
st.markdown("[Google](https://www.google.com/)")
st.markdown("# Hello World")
st.caption("Hi, I am the caption")
st.markdown("---")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.markdown("# [Katex](https://katex.org/docs/supported.html)")
json_dict = {"a": "1,2,3", "b": "4,5,6"}
st.json(json_dict)
my_code = """
print("Hello World")
def funct():
    return 0
    """
st.code(my_code, language="python")

st.write("## H2")
st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4ms⁻¹")

my_table = pd.DataFrame({"Column 1": [1, 2, 3, 4, 5],
                         "Column 2": [11, 12, 13, 14, 15]})
st.table(my_table)
st.dataframe(my_table)

st.image("a_sample.jpg", caption="This is a CAT as is")
st.image("a_sample.jpg", caption="This is a CAT with width = 320", width=320)
st.audio("a_sample.mp3")
st.video("a_sample.mp4")
