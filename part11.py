import datetime
import pandas as pd
import streamlit as st


# st.title("Hi, I am Streamlit Web App")
# st.subheader("I am your Subheader")
# st.header("I am Header")
# st.text("Hi, I am the text function")
# st.markdown("**Hello** World")
# st.markdown("[Google](https://www.google.com/)")
# st.markdown("# Hello World")
# st.caption("Hi, I am the caption")
# st.markdown("---")
# st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
# st.markdown("# [Katex](https://katex.org/docs/supported.html)")
# json_dict = {"a": "1,2,3", "b": "4,5,6"}
# st.json(json_dict)
# my_code = """
# print("Hello World")
# def funct():
#     return 0
#     """
# # st.code(my_code, language="python")

# st.write("## H2")
# st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4ms⁻¹")

# my_table = pd.DataFrame({"Column 1": [1, 2, 3, 4, 5],
#                          "Column 2": [11, 12, 13, 14, 15]})
# st.table(my_table)
# st.dataframe(my_table)

# st.image("a_sample.jpg", caption="This is a CAT as is")
# st.image("a_sample.jpg", caption="This is a CAT with width = 320", width=320)
# st.audio("a_sample.mp3")
# st.video("a_sample.mp4")

# # refer to video 7 to learn to remove HAMBURGER Menu & footer   ~  time 04:20


# def change():
#     st.text(st.session_state.checker)


# state = st.checkbox("Checkbox", value=True, on_change=change,
#                     key="checker")
# if state:
#     st.write(state, "checked")
# else:
#     st.write(state, "un-checked")

# radio_btn = st.radio("In what country do you live?",
#                      options=("US", "UK", "Canada"))

# st.write(radio_btn)


# def btn_click():
#     st.write("Buton Clicked")


# btn = st.button("Click", on_click=btn_click)

# select = st.selectbox("What is your favorite card?", 
#                       options=('Audi', 'BMW', 'Ford'))
# st.write(select)

# multi_select = st.multiselect("What are your favorite sports?",
#                               options=("Baseball", "Football",
#                                        "Basketball", "Hockey"))

# st.write(multi_select)

# st.title("Uploading Files")
# st.markdown("--------------------------------")
# img = st.file_uploader("Please upload an Image",
#                        type=("png", "jpg", "webp", "gif"),
#                        accept_multiple_files=True)
# if img is not None:
#     st.image(img)
# vid = st.file_uploader("Please upload a Video", type="mp4")
# if vid is not None:
#     st.video(vid)

# Start video #10
num = st.slider("This is a slider", min_value=50, max_value=150, value=70)
st.write(num)

txt = st.text_input("Enter your Name", max_chars=50)
st.write(txt)

para = st.text_area("Small Essay")
st.write(para)

date = st.date_input("Enter your birthdate",
                     min_value=datetime.date(1940, 2, 13))
st.write(date)

tim = st.time_input("Enter a time")
st.write(tim)

#   https://www.youtube.com/watch?v=dPYlqTGA6wc&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=11
