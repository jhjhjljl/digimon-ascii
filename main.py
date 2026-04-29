import processor


def main():
	processor.video_ascii_to_json("video.mp4", "output.json")
	processor.render_json_video("output.json")


if __name__ == "__main__":
	main()
