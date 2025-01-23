import streamlit as st
import ollama

def categorize_grocery_list(input_text, model="llama3.2"):
    prompt = f"""
    You are a smart assistant who categorizes and sorts grocery items.
    Here is the list of grocery items: {input_text}

    Please:
    1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, Sauces, etc.
    2. Sort the items alphabetically within each category.
    3. Present the categorized list in a clear and organized manner, using bullet points or numbering.
    """
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response.get("response", "Error: No response received.")
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Title of the app
st.title("Grocery List Categorizer")

# Custom input field with increased size
input_text = st.text_area("Enter your grocery list (comma-separated):", height=200)

# Button to trigger categorization
if st.button("Categorize List") and input_text:
    categorized_list = categorize_grocery_list(input_text)
    
    # Display categorized list
    st.subheader("Categorized Grocery List:")
    st.write(categorized_list)

# Add some custom CSS to style the input field
st.markdown("""
    <style>
        .stTextInput>div>div>input {
            width: 100%;
            padding: 15px;
            font-size: 16px;
            border-radius: 10px;
            border: 1px solid #ddd;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 18px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)
