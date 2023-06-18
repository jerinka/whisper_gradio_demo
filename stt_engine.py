
import whisper

class whisper_stt:
    def __init__(self) -> None:
        self.model = whisper.load_model("base")

    def stt(self,audio):
        result = self.model.transcribe(audio)
        return result["text"]
        