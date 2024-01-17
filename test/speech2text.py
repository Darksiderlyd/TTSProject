from paddlespeech.cli.asr.infer import ASRExecutor

asr = ASRExecutor()

result = asr(audio_file = "simple.wav")

print(result)
