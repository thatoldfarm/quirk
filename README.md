# quirk
Encoder and decoder for files encoded as QR codes in animated '.gif' and '.mp4' formats.

This project consists of a set of Python scripts designed to encode textual data into QR codes, compile these codes into visual formats (video and GIF), and then decode them back to the original text. It showcases a method for data encoding, transmission, and decoding using QR codes.

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
