import ollama
import os

model = "llama3.2"

# List of input image file paths
input_files = [
    "./data/bear.jpeg",
    "./data/lion.jpeg",
    "./data/maccao.jpeg",
    "./data/racoon.jpeg",
    "./data/tiger.jpeg"
]

# Check if all files exist
missing_files = [file for file in input_files if not os.path.exists(file)]
if missing_files:
    print(f"The following input files were not found: {missing_files}")
    exit(1)

# Prepare the prompt
prompt = """
You are a smart assistant who categorizes and sorts animals.

Here are pictures of some animals. Please:
1. Categorize these pictures into their animal names by identifying the pictures.
2. Categorize the animals under carnivore and herbivore.
3. If any animal exists in both categories, add their names in both.
"""

# Attempt to process the images and generate a response
try:
    # Assuming `ollama.generate` accepts image file paths
    response = ollama.generate(model=model, prompt=prompt, images=input_files)
    generated_response = response.get("response", "")
    
    print("========ANIMAL CATEGORIES=======")
    print(generated_response)

except Exception as e:
    print("An error occurred:", str(e))
