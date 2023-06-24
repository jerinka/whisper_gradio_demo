# Whisper Gradio Demo

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DqmqokgSWt87hQ8QY33TccO_IRfQkBZb?usp=sharing)

## Install

```bash
git clone https://github.com/jerinka/whisper_gradio_demo
cd whisper_gradio_demo

python3 -m venv env
source env/bin/activate
pip install git+https://github.com/openai/whisper.git 
pip install gradio
```

## Whisper Demo

```bash
python A_audio_file_stt.py -s (-s for sharing, avoid for local alone)
python B_record_stream_stt.py (record and submit)
python C_live_stream_stt.py (TODO: not good, need to improve)
```

This is part of Udemy Course: Deep Learning with Tensorflow and Pytorch\
You may use this [link](https://www.udemy.com/course/gitlab-cicd-essentials-for-industry-comprehensive-tutorial/?referralCode=78BD52230019795171CF) to enroll.
