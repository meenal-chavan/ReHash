from transformers import T5Tokenizer, T5ForConditionalGeneration
import regex as re

# empty for now bc not sure how we want to postprocess the text
def postprocess(text):
  return text

def paraphrase(text):
    # define prefix for T5
    model = T5ForConditionalGeneration.from_pretrained('./models/paraphrase')
    tokenizer = T5Tokenizer.from_pretrained('./models/paraphrase')
    prefix = 'paraphrase: '

    # tokenize text
    tokenized_text = tokenizer([prefix + text], padding=False, truncation=True, return_tensors='pt')['input_ids']
    
    # get model output
    output = model.generate(tokenized_text,
                             do_sample=True,
                             max_length=250,
                             top_k=50,
                             top_p=0.95,
                             num_return_sequences=1,
                             no_repeat_ngram_size=3,
                             early_stopping=True,
                             temperature=0.7)
    
    # return decoded and postprocessed output
    return postprocess(tokenizer.decode(output[0], skip_special_tokens=True))

print(paraphrase('This is the first sentence we\'re using'))