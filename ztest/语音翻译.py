from paddlespeech.cli.st.infer import STExecutor

st = STExecutor()
# 使用预编译的 kaldi 相关工具，只支持在 Ubuntu 系统中体验
result = st(audio_file="en.wav")
