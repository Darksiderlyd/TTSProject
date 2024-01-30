import webbrowser

import gradio as gr

from config import config

import asyncio
import string
import time
import edge_tts
import os

from submaker import SubMaker
from ttssrtvtt import batch_convert_vtt_to_srt


def getSoundFileName(file_name) -> string:
    return f"sounds/{file_name}.wav"


def getSrtFileName(file_name) -> string:
    return f"vtts/{file_name}.vtt"


async def convert(text, file_name, rate="+20%", volume="+20%") -> None:
    start_time = time.time()

    communicate = edge_tts.Communicate(text, "zh-CN-YunxiNeural", rate=rate, volume=volume)
    print(f"{file_name}: 开始生成{file_name}.wav")
    await communicate.save(getSoundFileName(file_name))
    print(f"{file_name}: 用时 {int(time.time() - start_time)}秒")

    print(f"{file_name}: 开始读取语音文件生成{file_name}字幕")
    start_time_vtt = time.time()
    subMaker = SubMaker()
    with open(getSoundFileName(file_name), "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                subMaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])

    with open(getSrtFileName(file_name), "w", encoding="utf-8") as file:
        lines = subMaker.generate_subs().split('\n')
        for line in lines:
            file.write(line)

    print(
        f"{file_name}: 全部处理完成，字幕生成用时 {int(time.time() - start_time_vtt)}秒  总用时 {int(time.time() - start_time)}秒")


async def amain(inputDir, outputDir, rateValue=20, volumeValue=20):
    # 创建输出文件夹
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    if not os.path.exists("vtts"):
        os.makedirs("vtts")

    rate = f'+{rateValue}%'
    volume = f'+{volumeValue}%'

    tasks = []
    # 遍历输入文件夹
    for root, dirs, files in os.walk(inputDir):
        for file in files:
            # 将文件中的文本读出来
            with open(os.path.join(root, file), "r", encoding='utf-8') as text_file:
                text = text_file.read()
                # 获取文件名
                file_name, ext = os.path.splitext(file)
                # 加入任务列表
                tasks.append(convert(text, file_name, rate, volume))
    # 等待所有任务完成
    await asyncio.gather(*tasks)

    batch_convert_vtt_to_srt('vtts', 'srts')

    return ["生成结束", "srts"]


def greet(name, intensity):
    return "Hello " * intensity + name + "!"


def openFile(dirfile):
    os.startfile(dirfile)


if __name__ == "__main__":
    with gr.Blocks() as app:
        with gr.Row():
            with gr.Column():
                input_dir = gr.Textbox(label="文本输入文件夹")
                output_dir = gr.Textbox(label="语音输出文件夹")

                with gr.Row():
                    slider_rate = gr.Slider(label="说话速度", minimum=0, maximum=100, step=1)
                    slider_volume = gr.Slider(label="音量", minimum=0, maximum=100, step=1)

                srt_dir = gr.Textbox(label="语音输出文件夹(可选)", value='srts')

                info = gr.Textbox(label="结果")

                submit = gr.Button(value="执行", variant="primary")
                open_wav_dir = gr.Button(value="打开输出文件夹", variant="primary")
                open_srt_dir = gr.Button(value="打开字幕文件地址", variant="primary")

        submit.click(
            amain,
            inputs=[input_dir, output_dir, slider_rate, slider_volume],
            outputs=[info, srt_dir]
        )

        open_wav_dir.click(
            openFile,
            inputs=[output_dir],
        )

        open_srt_dir.click(
            openFile,
            inputs=[srt_dir],
        )

    webbrowser.open(f"http://127.0.0.1:{config.webui_config.port}")
    app.launch(share=config.webui_config.share, server_port=config.webui_config.port)
