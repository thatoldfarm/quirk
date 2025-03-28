# quirk
Encoder and decoder for files encoded as QR codes in animated '.gif' and '.mp4' formats.

This project consists of a set of Python scripts designed to encode textual data into QR codes, compile these codes into visual formats (video and GIF), and then decode them back to the original text. It showcases a method for data encoding, transmission, and decoding using QR codes.

In a nutshell the encoders take any kind of file type as an input.

It turns the file *itself* into text and then encodes that text *into* the QR codes.

The QR codes are then used to generate an animated gif file and/or a mp4 file.

The gif and/or mp4 file can then be decoded back into the 'original' *file* itself including the file extension.

Both the animated gifs and the mp4 video files can then be broadcast and decoded.

This enables it to be able to read from one device to another *with only the camera* and be able to recreate the *file* itself on the receiving device once the frames are decoded.

Main quirk Repository:

https://github.com/thatoldfarm/quirk

Source text for test.txt

https://github.com/thatoldfarm/quirk/blob/main/test.txt

Source text for test.pdf

https://github.com/thatoldfarm/quirk/blob/main/quirk-pdf/test.pdf

Alpha release with source code:

https://github.com/thatoldfarm/quirk/releases/tag/0.001

#### Dependencies:
- Python 3
- OpenCV (`cv2`)
- numpy
- qrcode
- gzip
- base64
- os
- json
- pyzbar


#### EXTRA Dependencies for troubleshooting:
- libgtk2.0-dev
- pkg-config
- opencv-contrib-python


#### Order of execution:

quirk_vid_encode.py
quirk_vid_decode.py

quirk_gif_encode.py
quirk_gif_decode.py





#### License

MIT License
Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
