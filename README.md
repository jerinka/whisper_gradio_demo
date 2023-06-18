# Whisper Gradio Demo

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DqmqokgSWt87hQ8QY33TccO_IRfQkBZb?usp=sharing)

## Clone the repository

```bash
git clone https://github.com/your-username/audio-transcription-app.git
cd audio-transcription-app
```

## Whisper based

```bash
python3 -m venv env
source env/bin/activate
pip install git+https://github.com/openai/whisper.git 
pip install gradio

python audio_file_stt.py -s (-s for sharing, avoid for local alone)
python record_stream_stt.py (record and submit)
python live_stream_stt.py (TODO: not good, need to improve)
```