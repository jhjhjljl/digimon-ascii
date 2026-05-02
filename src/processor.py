import json
import time
import sys

import cv2
import numpy
import ijson


ASCII_RAMP = " .:-=+*#%@"
ASCII_RAMP_LEN = len(ASCII_RAMP) - 1
LOOKUP = numpy.array(list(ASCII_RAMP))
BASE_WIDTH = 960
BASE_HEIGHT = 720
FRAME_WIDTH = 200
FRAME_HEIGHT = int(FRAME_WIDTH * (BASE_HEIGHT/ BASE_WIDTH))
FPS = 23.976


def frame_to_ascii(
	frame: numpy.ndarray,
	width: int,
	height: int
) -> str:
	frame = cv2.resize(frame, (width, height))
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	indices = (frame / 255 * ASCII_RAMP_LEN).astype(int)
	return "\n".join(("".join(row) for row in LOOKUP[indices]))


def image_to_ascii(
	fpath: str,
	width: int = FRAME_WIDTH,
	height: int = FRAME_HEIGHT
) -> str:
	frame = cv2.imread(fpath)
	return frame_to_ascii(frame, width, height)


def image_ascii_to_json(
	fpath: str,
	output: str,
	width: int = FRAME_WIDTH,
	height: int = FRAME_HEIGHT
) -> None:
	ascii = image_to_ascii(fpath, width, height)
	with open(output, "w") as f:
		json.dump(ascii, f)


def video_ascii_to_json(
	fpath: str,
	output: str,
	width: int = FRAME_WIDTH,
	height: int = FRAME_HEIGHT
) -> None:
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
			json.dump(frame_to_ascii(frame, width, height), f)
			first = False
		f.write("]")
	cap.release()


def render_json_video(
	fpath: str,
	fps: float = FPS
) -> None:
	delay = 1 / fps
	sys.stdout.write("\033[2J")
	with open(fpath) as f:
		for frame in ijson.items(f, "item"):
			start = time.time()
			sys.stdout.write("\033[H")
			sys.stdout.write(frame)
			sys.stdout.flush()
			elapsed = time.time() - start
			time.sleep(max(0, delay - elapsed))
