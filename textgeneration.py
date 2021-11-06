# -*- coding: utf-8 -*-


from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')

set_seed(50)
text = generator("I am hungry for success")

print(text)

import gradio as gr
def func(text):
  generated  = generator(text)
  return generated

description = "This is a text genration application, It builds genrate text from sentences put in. Built by Edem Gold🚀"

app = gr.Interface(fn=func, inputs="textbox", outputs="textbox", title="Text Generator")
app.launch()

