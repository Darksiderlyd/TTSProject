#!/usr/bin/env python3

"""
Streaming TTS example with subtitles.

This example is similar to the example basic_audio_streaming.py, but it shows
WordBoundary events to create subtitles using SubMaker.
"""

import asyncio

import edge_tts

TEXT = '''这是一个普通人成长的故事。街头小混混丁原自小饱受冷眼，以偷盗为生。偶然机遇下，天陆上正魔两道追索的宝物《晓寒春山图》、无数人梦寐以求的绝学“翠微九歌”，竟然难以解释的与他产生了交集，从此他的生命轨迹发生了天翻地覆的改变。天意昭昭，不管是福是祸，一个桀骜少年的修仙传说就从这里开始展开……'''
VOICE = "zh-CN-YunxiNeural"
OUTPUT_FILE = "simple.mp3"
WEBVTT_FILE = "simple.vtt"


async def amain() -> None:
    """Main function"""
    communicate = edge_tts.Communicate(TEXT, VOICE)
    subMaker = edge_tts.SubMaker()
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                subMaker.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])

    content = subMaker.generate_subs()
    print("||" + content + "||")

    # 特殊处理
    with open(WEBVTT_FILE, "w", encoding="utf-8") as file:
        lines = content.split('\n')
        for line in lines:
            file.write(line)


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(amain())
    finally:
        loop.close()
