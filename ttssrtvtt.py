import os
import re
import sys

def vtt_to_srt(vtt_path, srt_path):
    try:
        with open(vtt_path, 'r', encoding='utf-8') as vtt_file:
            vtt_content = vtt_file.read()
    except FileNotFoundError:
        print(f"Error: File '{vtt_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file '{vtt_path}': {e}")
        return None

    # 使用正则表达式匹配WebVTT格式的时间戳和文本
    pattern = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{3})\s-->\s(\d{2}:\d{2}:\d{2}\.\d{3})\n(.+?)\n\n', re.DOTALL)

    # 匹配所有时间戳和文本
    matches = re.findall(pattern, vtt_content)

    # 将匹配的内容转换为SRT格式
    srt_content = '\n'.join([f"{idx}\n{start.replace('.', ',')} --> {end.replace('.', ',')}\n{text}\n" for idx, (start, end, text) in enumerate(matches, start=1)])

    # 去除多余的空行
    srt_content = re.sub(r'\n{3,}', r'\n\n', srt_content)

    try:
        with open(srt_path, 'w', encoding='utf-8') as srt_file:
            srt_file.write(srt_content)
    except Exception as e:
        print(f"An error occurred while writing the SRT file '{srt_path}': {e}")
        return None

    return srt_path

def batch_convert_vtt_to_srt(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    vtt_files = [f for f in os.listdir(input_dir) if f.endswith('.vtt')]

    for vtt_file in vtt_files:
        vtt_path = os.path.join(input_dir, vtt_file)
        srt_file = vtt_file.replace('.vtt', '.srt')
        srt_path = os.path.join(output_dir, srt_file)

        converted_file = vtt_to_srt(vtt_path, srt_path)
        if converted_file:
            print(f"Conversion successful: {converted_file}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py input_directory output_directory")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    batch_convert_vtt_to_srt(input_dir, output_dir)

if __name__ == "__main__":
    main()
