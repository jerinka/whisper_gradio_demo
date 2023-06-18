import time
import whisper

class whisper_stt:
    def __init__(self) -> None:
        self.model = whisper.load_model("base")

    def stt(self,audio):
        result = self.model.transcribe(audio)
        return result["text"]
        

if __name__=="__main__":
    stt_obj = whisper_stt()
    for i in range(3):
        start = time.time()
        txt = stt_obj.stt('sample.wav') # audio 18sec
        print('txt:',txt, "\ntime:",time.time()-start) # 0.8sec