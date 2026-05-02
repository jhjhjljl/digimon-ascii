import processor


def main():
	fpath = "/Users/jihoonlee/Pictures/vlcsnap-2026-05-01-00h15m47s927.png"
	# fpath = "/Users/jihoonlee/Downloads/test.jpg"
	ascii = processor.image_to_ascii(fpath)
	print(ascii)
	# fpath = "/Users/jihoonlee/Movies/DaVinci Resolve/warp digivolve wargreymon.mov"
	processor.video_ascii_to_json(fpath, "../assets/digimon/output.json")
	# processor.render_json_video("../assets/digimon/output.json")

	# fpath = "/Users/jihoonlee/Downloads/test.png"
	# processor.image_ascii_to_json(fpath, "test.json")
	# processor.video_ascii_to_json(fpath, "output.json")


if __name__ == "__main__":
	main()
