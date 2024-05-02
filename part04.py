import streamlit as st

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
