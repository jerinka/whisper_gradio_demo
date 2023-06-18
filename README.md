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
python audio_transcription_app.py -s (-s for sharing, avoid for local alone)
python record_stt.py (for record and speech to text)
python live_transformer_stt.py (for live speech to text)
```

## Transformer based

```bash
python3 -m venv env
source env/bin/activate
pip install transformers
pip install gradio
python record_stt.py (for record and speech to text)
python live_transformer_stt.py (for live speech to text)
```

## Deep Speech

```bash
cd deep_speech_demo

wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.2/deepspeech-0.8.2-models.pbmm
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.2/deepspeech-0.8.2-models.scorer
apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
pip install deepspeech==0.8.2

python deep_demo.py (TODO: not working now, need to fix)
```