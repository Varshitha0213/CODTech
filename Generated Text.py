# 🧠 Step 1: Install Transformers and import libraries
!pip install -q transformers

from transformers import pipeline, set_seed
import random

# 🛠️ Step 2: Load the text generation pipeline with GPT-2
generator = pipeline('text-generation', model='gpt2')
set_seed(random.randint(1, 1000))  # Set random seed for varied outputs

# 📝 Step 3: User Input Prompt
prompt = input("💬 Enter a prompt to generate text: ")

# ✨ Step 4: Generate text
results = generator(prompt, max_length=100, num_return_sequences=1)

# 📄 Step 5: Display the result
print("\n🧾 Generated Text:\n")
print(results[0]['generated_text'])
