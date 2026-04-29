import processor
import json


def main():
	# fpath = "/Users/jihoonlee/Downloads/test.png"
	# processor.image_ascii_to_json(fpath, "test.json")
	# processor.video_ascii_to_json(fpath, "output.json")
	with open("test.json") as f:
		ascii = json.load(f)
		print(ascii)


if __name__ == "__main__":
	main()
