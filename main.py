import processor


def main():
	fpath = "/Users/jihoonlee/Downloads/wargreymon.mp4"
	processor.video_ascii_to_json(fpath, "output.json")
	processor.render_json_video("output.json")


if __name__ == "__main__":
	main()
