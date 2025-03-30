import json
import base64
import gzip

def safe_base64_decode(data):
    if isinstance(data, str):
        return data
    try:
        data = data.decode("utf-8")
    except UnicodeDecodeError as e:
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
def decode_data(json_file):
    """
    Decodes a file encoded using gzip compression, Base64, and split into JSON chunks.
    Args:
        json_file: Path to the JSON file containing the chunks.
    Returns:
        The decompressed string, or None if an error occurs.
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        if "chunks" not in data or not isinstance(data["chunks"], list):
            raise ValueError("Invalid JSON structure. Expected a dictionary with 'chunks' key containing a list.")

        # Concatenate all chunks:
        concatenated_data = "".join(data["chunks"])

        # Base64 Decode:
        decoded_data = safe_base64_decode(concatenated_data.encode('utf-8'))

        if decoded_data is None:
            raise ValueError("Base64 decoding failed.")

        # Gzip Decompress:
        decompressed_data = gzip.decompress(decoded_data).decode("utf-8")  # Decompress and decode as UTF-8

        return decompressed_data

    except FileNotFoundError:
        print(f"Error: File not found: {json_file}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    except gzip.BadGzipfile as e:
        print(f"Gzip decompression failed: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example Usage:
if __name__ == "__main__":
    decoded_text = decode_data("chunks.json")
    if decoded_text:
        print("Decoded Text:")
        print(decoded_text)
        with open("decoded_output.txt", "w", encoding="utf-8") as outfile:
          outfile.write(decoded_text)
    else:
        print("Decoding failed.")
