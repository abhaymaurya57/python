import whisper

model = whisper.load_model("base", device="cpu")
result = model.transcribe("library/audio.mp3", fp16=False)
print(result["text"])
