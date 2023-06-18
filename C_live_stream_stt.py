import gradio as gr
import time
from stt_engine import whisper_stt

stt_obj = whisper_stt()

def transcribe(audio, state=""):
    time.sleep(2)
    text = stt_obj.stt(audio)
    state += text + " "
    return state, state

gr.Interface(
    fn=transcribe, 
    inputs=[
        gr.Audio(source="microphone", type="filepath", streaming=True), 
        "state"
    ],
    outputs=[
        "textbox",
        "state"
    ],
    live=True).launch()
