import json
import sys
import time

import cv2
import numpy


ASCII_RAMP = " ░▒▓█"
ASCII_RAMP_LEN = len(ASCII_RAMP) - 1
LOOKUP = numpy.array(list(ASCII_RAMP))


def _frame_to_ascii(
	frame: numpy.ndarray,
	width: int,
	height: int
):
	frame = cv2.resize(frame, (width, height))
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	indices = (frame / 255 * ASCII_RAMP_LEN).astype(int)
	return "\n".join(("".join(row) for row in LOOKUP[indices]))


def image_to_ascii(
	fpath: str,
	width: int = 60,
	height: int = 30
):
	frame = cv2.imread(fpath)
	return _frame_to_ascii(frame, width, height)


def video_to_ascii(
	fpath: str,
	width: int = 60,
	height: int = 30
):
	cap = cv2.VideoCapture(fpath)
	fps = cap.get(cv2.CAP_PROP_FPS)
	delay = 1 / fps
	sys.stdout.write("\033[2J")
	while True:
		ret, frame = cap.read()
		if not ret:
			break
		start = time.time()
		sys.stdout.write("\033[H")
		sys.stdout.write(_frame_to_ascii(frame, width, height))
		sys.stdout.flush()
		elapsed = time.time() - start
		time.sleep(max(0, delay - elapsed))
	cap.release()


def video_to_json(
	fpath: str,
	output: str,
	width: int = 60,
	height: int = 30
):
	import json
	cap = cv2.VideoCapture(fpath)
	with open(output, "w") as f:
		f.write("[")
		first = True
		while True:
			ret, frame = cap.read()
			if not ret:
				break
			if not first:
				f.write(",")
			json.dump(_frame_to_ascii(frame, width, height), f)
			first = False
		f.write("]")
	cap.release()


def main():
	video_to_json("video.mp4", "test.json")


if __name__ == "__main__":
	main()
