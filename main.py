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

st.title("Grocery List Categorizer")

input_text = st.text_input("Enter your grocery list (comma-separated):")

if st.button("Categorize List") and input_text:
    categorized_list = categorize_grocery_list(input_text)
    st.subheader("Categorized Grocery List:")
    st.write(categorized_list)
