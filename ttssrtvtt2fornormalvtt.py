from vtt_to_srt.vtt_to_srt import ConvertDirectories, ConvertFile

recursive = False
convert_file = ConvertDirectories(".", recursive, "utf-8")
convert_file.convert()

convert_file = ConvertFile("vtts/前传.vtt", "utf-8")
convert_file.convert()
