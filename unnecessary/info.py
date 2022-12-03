import wikipedia
from summarizer import TransformerSummarizer
from row_matching import df_new

content = wikipedia.page(df_new['prognosis'])

GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
gpt_summary = ''.join(GPT2_model(content.content, num_sentences=4))
print(gpt_summary)
