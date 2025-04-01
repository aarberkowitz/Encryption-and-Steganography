from pathlib import *
from PIL import Image

def save_result_to_file(original_path, content, suffix):
    output_path = original_path.with_name(original_path.stem + suffix)
    output_path.write_text(content, encoding="utf-8")
    print(f'File saved to: {output_path}')
    return output_path

def steganography_process(image_path, message=None, output_suffix="_decrypted.txt"):
    image_path = Path(image_path)

    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    if message is not None:
        # ENCODE MODE
        message_bytes = message.encode('utf-8')
        message_bits = ''.join(f"{byte:08b}" for byte in message_bytes)
        message_len = len(message_bits)
        full_bits = f"{message_len:032b}" + message_bits

        if len(full_bits) > width * height * 3:
            raise ValueError("The image is too small for the message.")

        bit_index = 0
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                channels = [r, g, b]
                for k in range(3):
                    if bit_index < len(full_bits):
                        channel_bin = format(channels[k], '08b')
                        channel_bin = channel_bin[:-1] + full_bits[bit_index]
                        channels[k] = int(channel_bin, 2)
                        bit_index += 1
                pixels[x, y] = tuple(channels)

        img.save(image_path)
        print(f"Message was embedded into image: {image_path}")

    else:
        # DECODE MODE
        bits = ""
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                bits += str(r & 1)
                bits += str(g & 1)
                bits += str(b & 1)

        length_bits = bits[:32]
        message_length = int(length_bits, 2)

        max_capacity = width * height * 3
        if message_length > (max_capacity - 32):
            raise ValueError("Invalid message length or corrupted image.")

        message_bits = bits[32:32 + message_length]
        message_bytes = bytearray(int(message_bits[i:i + 8], 2) for i in range(0, len(message_bits), 8))
        message = message_bytes.decode('utf-8')

        return save_result_to_file(image_path, message, output_suffix)


def embed_message_in_image(image_path, text_path):
    message = Path(text_path).read_text(encoding="utf-8")
    steganography_process(image_path, message=message)


def extract_message_from_image(image_path):
    return steganography_process(image_path)