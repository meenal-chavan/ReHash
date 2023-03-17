from transformers import T5Tokenizer, T5ForConditionalGeneration
import regex as re

#Some simple post processing to make the output look nice. might need to add some more processing here
def postprocess(text):
  text = re.sub('-LRB-', '(', text)
  text = re.sub('-RRB-', ')', text)
  return text

def style_transfer(text):
    model = T5ForConditionalGeneration.from_pretrained('./models/simp')
    tokenizer = T5Tokenizer.from_pretrained('./models/simp')

    # define prefix for T5
    prefix = 'simplify: '

    # tokenize text
    tokenized_text = tokenizer([prefix + text], padding=False, truncation=True, return_tensors='pt')['input_ids']
    
    # get model output
    output = model.generate(tokenized_text,
                             do_sample=True,
                             max_length=150,
                             top_k=50,
                             top_p=0.95,
                             no_repeat_ngram_size=3,
                             temperature=0.7)
    
    # return decoded and postprocessed output
    return postprocess(tokenizer.decode(output[0], skip_special_tokens=True))