import processor


def main():
	fpath = "/Users/jihoonlee/Movies/wargreymon.mov"
	processor.video_ascii_to_json(fpath, "../assets/digimon/output.json")


if __name__ == "__main__":
	main()
