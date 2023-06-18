# from transformers import pipeline
# p = pipeline("automatic-speech-recognition")

import gradio as gr

import whisper
model = whisper.load_model("base")

def transcribe(audio):
    # text = p(audio)["text"]
    result = model.transcribe(audio)
    return result["text"]

gr.Interface(
    fn=transcribe, 
    inputs=gr.Audio(source="microphone", type="filepath"), 
    outputs="text").launch()
