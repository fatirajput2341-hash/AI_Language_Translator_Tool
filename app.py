import streamlit as st
from deep_translator import GoogleTranslator

# 1. Page Configuration Setup
st.set_page_config(page_title="AI Translation Tool", page_icon="🌐", layout="centered")

# Header Section
st.title("🌐 AI Language Translation Tool")
st.markdown("CodeAlpha Artificial Intelligence Internship Task 1")
st.write("---")

# 2. Languages Selection Dropdowns
languages_dict = {
    "English": "en",
    "Urdu": "ur",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Arabic": "ar"
}

left_col, right_col = st.columns(2)
with left_col:
    source_lang = st.selectbox("From Language:", list(languages_dict.keys()), index=0)
with right_col:
    target_lang = st.selectbox("To Language:", list(languages_dict.keys()), index=1)

st.write("")

# 3. Text Input Field
input_text = st.text_area("Enter Text to Translate:", height=150, placeholder="Type your text here...")

# 4. Translation Logic & Output screen display
if st.button("Translate Text", type="primary"):
    if not input_text.strip():
        st.warning("Please enter some text before processing the translation.")
    else:
        try:
            with st.spinner("Processing translation via Google Translate API..."):
                src_code = languages_dict[source_lang]
                dest_code = languages_dict[target_lang]
                
                # Fetching translation response
                translated_result = GoogleTranslator(source=src_code, target=dest_code).translate(input_text)
                
                st.write("---")
                st.success("✨ Translation Completed Successfully!")
                st.text_area("Translated Output:", value=translated_result, height=150)
                
        except Exception as e:
            st.error(f"Could not connect to translation services. Error: {e}")

st.write("---")
st.caption("Developed by Fatima | Student ID: CA/DF1/190219 | CodeAlpha Internship Assignment")
