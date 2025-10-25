import socket
from PIL import ImageGrab, Image, ImageDraw
import time
from io import BytesIO
import ctypes

host = '192.168.1.167'  # server IP address
port = 12347

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX_DATAGRAM_BYTES = 65000

def encode_udp_jpeg(image, max_bytes=MAX_DATAGRAM_BYTES):
    quality = 60
    scale = 1.0
    attempts = 0
    while True:
        frame = image
        if scale < 0.999:
            w, h = image.size
            new_w = max(1, int(w * scale))
            new_h = max(1, int(h * scale))
            frame = image.resize((new_w, new_h), Image.LANCZOS)

        buf = BytesIO()
        frame.save(buf, format='JPEG', quality=quality, optimize=True)
        data = buf.getvalue()
        if len(data) <= max_bytes:
            return data

        attempts += 1
        if attempts > 10:
            # Failsafe: aggressive downscale and low quality
            w, h = image.size
            frame = image.resize((max(1, w // 3), max(1, h // 3)), Image.LANCZOS)
            buf = BytesIO()
            frame.save(buf, format='JPEG', quality=30, optimize=True)
            return buf.getvalue()

        if quality > 30:
            quality -= 5
        else:
            scale *= 0.8

#Added mouse pointer
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def get_cursor_position():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

try:
    while True:
        screenshot = ImageGrab.grab().convert('RGB')
        try:
            x, y = get_cursor_position()
            draw = ImageDraw.Draw(screenshot)
            r_outer = 8
            r_inner = 5
            # White outer ring for visibility
            draw.ellipse((x - r_outer, y - r_outer, x + r_outer, y + r_outer), outline='white', width=3)
            # Red inner dot
            draw.ellipse((x - r_inner, y - r_inner, x + r_inner, y + r_inner), fill='red')
        except Exception:
            pass
        payload = encode_udp_jpeg(screenshot)
        client_socket.sendto(payload, (host, port))
        time.sleep(1/60)  # 60 FPS
finally:
    client_socket.close()