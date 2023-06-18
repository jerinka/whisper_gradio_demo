# from transformers import pipeline
# p = pipeline("automatic-speech-recognition")

import argparse
import gradio as gr

from stt_engine import whisper_stt

stt_obj = whisper_stt()

def transcribe(audio):
    # text = p(audio)["text"]
    text = stt_obj.stt(audio)
    return text

def main(share=False):
    
    gr.Interface(
        fn=transcribe, 
        inputs=gr.Audio(source="microphone", type="filepath"), 
        outputs="text").launch(share=share)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--share', action='store_true')
    args = parser.parse_args()
    share = args.share
    main(share)
