import gradio as gr
import time
import whisper

model = whisper.load_model("base")

def transcribe(audio, state=""):
    time.sleep(2)
    result = model.transcribe(audio)
    text = result["text"]
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
