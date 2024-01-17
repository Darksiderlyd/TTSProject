import asyncio
import string
import time
import edge_tts
import os

from ttssrtvtt import batch_convert_vtt_to_srt


def getSoundFileName(file_name) -> string:
    return f"sounds/{file_name}.wav"


def getSrtFileName(file_name) -> string:
    return f"vtts/{file_name}.vtt"


async def convert(text, file_name) -> None:
    start_time = time.time()
    communicate = edge_tts.Communicate(text, "zh-CN-YunxiNeural")
    print(f"{file_name}: 开始生成{file_name}.wav")
    await communicate.save(getSoundFileName(file_name))
    print(f"{file_name}: 用时 {int(time.time() - start_time)}秒")

    print(f"{file_name}: 开始读取语音文件生成{file_name}字幕")
    start_time_vtt = time.time()
    subMaker = edge_tts.SubMaker()
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
    print(f"{file_name}: 全部处理完成，字幕生成用时 {int(time.time() - start_time_vtt)}秒  总用时 {int(time.time() - start_time)}秒")

async def amain():
    # 创建输出文件夹
    if not os.path.exists("sounds"):
        os.makedirs("sounds")

    if not os.path.exists("vtts"):
        os.makedirs("vtts")

    tasks = []
    # 遍历输入文件夹
    for root, dirs, files in os.walk("texts"):
        for file in files:
            # 将文件中的文本读出来
            with open(os.path.join(root, file), "r", encoding='utf-8') as text_file:
                text = text_file.read()
                # 获取文件名
                file_name, ext = os.path.splitext(file)
                # 加入任务列表
                tasks.append(convert(text, file_name))
    # 等待所有任务完成
    await asyncio.gather(*tasks)

    batch_convert_vtt_to_srt('vtts', 'srts')


if __name__ == "__main__":
    amain()
