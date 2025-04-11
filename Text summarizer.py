!pip install -q transformers
!pip install -q torch
!pip install -q nltk
import nltk
from transformers import pipeline
nltk.download('punkt')
summarizer = pipeline("summarization")
def summarize_text(input_text, min_length=50, max_length=150):
    if len(input_text.split()) < 50:
        return "Text too short to summarize effectively. Please enter at least 50 words."
    summary = summarizer(input_text, min_length=min_length, max_length=max_length, do_sample=False)
    return summary[0]['summary_text']
long_text = """
The evolution of technology has significantly impacted how we consume and process information.
With the rapid growth of digital content, it has become increasingly challenging for individuals
to stay updated with the most relevant information. Text summarization addresses this issue by
automatically generating concise summaries of larger texts, allowing users to grasp the core message
quickly. Modern summarization techniques, particularly those powered by machine learning and deep learning,
have proven to be highly effective. Pretrained models like BART and T5 from HuggingFace enable users to
perform abstractive summarization, where the model paraphrases and rewrites the main points using natural
language. These tools are now widely used in applications like news aggregation, academic research,
and legal document analysis.
"""
print("🔹 Original Text:\n")
print(long_text)
summary_output = summarize_text(long_text)
print("\n🔸 Summarized Text:\n")
print(summary_output)
