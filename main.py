import sys
import time

import cv2
import numpy


ASCII_RAMP = " .:-=+*#%@"
ASCII_RAMP = " ░▒▓█"
ASCII_RAMP_LEN = len(ASCII_RAMP) - 1
LOOKUP = numpy.array(list(ASCII_RAMP))
CLAHE = cv2.createCLAHE(clipLimit=6.0, tileGridSize=(8, 8))


def frame_to_ascii(frame, width: int = 50, height: int = 25) -> str:
	frame = cv2.resize(frame, (width, height))
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame = CLAHE.apply(frame)
	indices = (frame / 255 * ASCII_RAMP_LEN).astype(int)
	return "\n".join("".join(row) for row in LOOKUP[indices])


def img_to_ascii(fpath: str, width: int = 50, height: int = 25) -> str:
	img = cv2.imread(fpath)
	return frame_to_ascii(img, width, height)


def video_to_ascii(fpath: str, width: int = 50, height: int = 25) -> None:
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
		sys.stdout.write(frame_to_ascii(frame, width, height))
		sys.stdout.flush()
		elapsed = time.time() - start
		time.sleep(max(0, delay - elapsed))
	cap.release()


def main():
	# video_to_ascii("wargraymon.mov", 120, 30)
	test = img_to_ascii("agumon.webp", 120, 30)
	print(test)



if __name__ == "__main__":
	main()
