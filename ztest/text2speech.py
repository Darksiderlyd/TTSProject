from paddlespeech.cli.tts.infer import TTSExecutor

TEXT = str('今天天气十分不错。')

tts = TTSExecutor()
tts(text=TEXT, output="output.wav")
