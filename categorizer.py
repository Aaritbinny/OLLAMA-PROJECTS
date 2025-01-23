import ollama
import os
model = "llama3.2"

input_file = "./data/grocery_list.txt"
output_file = "./data/categorized_grocery_list.txt"

if not os.path.exists(input_file):
    print(f"input file '{input_file}' not found.")
    exit(1)

with open(input_file, "r") as f:
    items = f.read().strip()

prompt = f"""
You are a smart assistant who categorizes and sort grocery items.

Here is the list of grocery items:
{items}

Please:
1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, sauces etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.

"""

#send the prompt and get the response

try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print("========Categorised list========\n ")
    print(generated_text)

    #writing to output file
    with open(output_file, "w") as f:
        f.write(generated_text.strip())

    print(f"categorised list has been saved to '{output_file}.")
except Exception as e:
    print("an error occured:",str(e))