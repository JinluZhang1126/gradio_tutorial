import gradio as gr
from transformers import pipeline

pipe = pipeline(task="image-classification")
gr.Interface.from_pipeline(pipe).launch()