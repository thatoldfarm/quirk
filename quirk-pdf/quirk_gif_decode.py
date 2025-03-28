import cv2
import numpy as np
from pyzbar.pyzbar import decode
import base64
import gzip
from PIL import Image
import qrcode
import os
import json

def safe_base64_decode(data):
    if isinstance(data, str):
        return data
    try:
        data = data.decode("utf-8")  # Decode the bytes to a string
    except UnicodeDecodeError:
      #  return data  # If data is not valid UTF-8, it's probably already decoded

      raise ValueError(f"UnicodeDecodeError: {data!r}")

    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    try:
        return base64.urlsafe_b64decode(data)
    except Exception as e:
        print(f"Exception during decoding: {e}")
        #return None
        raise ValueError(f"Base64DecodeError: {e}") #Change it to an unhandled error
    #If your data is still failing to base64 decode, you can also print data
    #print(data)


# Open the animated GIF file
gif_file = 'animated.gif'

# Initialize an empty list to hold the data chunks
data_chunks = []
prev_chunk = None

# Open the GIF file
gif = Image.open(gif_file)
try:
    while True:
        # Get the current frame
        current_frame = gif.tell()

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(cv2.cvtColor(np.array(gif), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)

        # Decode QR codes from the frame
        decoded_objects = decode(gray_frame)

        # Process the decoded data
        for obj in decoded_objects:
            try:
                decoded_data = safe_base64_decode(obj.data)
                if decoded_data is not None and decoded_data != prev_chunk:
                    data_chunks.append(decoded_data)
                    prev_chunk = decoded_data
                    print(f"Successfully decoded frame {current_frame}: {len(decoded_data)} bytes") #Log a successful chunk!
            except ValueError as e:
                print(f"Error decoding frame {current_frame}: {e}")

        # Move to the next frame
        gif.seek(current_frame + 1)
except EOFError:
    pass

# Concatenating and decompressing data
concatenated_data = b''.join(data_chunks)
try:
    # Decompress the full data
    decompressed_data = gzip.decompress(concatenated_data)
    with open("test_gif_decoded.pdf", "wb") as out_file:
        out_file.write(decompressed_data)
    print("Data decompressed and written to 'test_gif_decoded.pdf'.")
except Exception as e:
    print(f"Exception occurred during decompression: {e}")

print("Finished.")
