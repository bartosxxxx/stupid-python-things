#!/usr/bin/env python3
import os
import requests
import uuid
import time
import sys

def loading_animation(text="Loading cat images"):
    for _ in range(3):
        for dot_count in range(4):
            dots = '.' * dot_count
            sys.stdout.write(f"\r{text}{dots}   ")
            sys.stdout.flush()
            time.sleep(0.4)
    print("\r" + " " * (len(text) + 5), end="\r")

def get_pictures_folder():
    home = os.path.expanduser("~")
    possible_dirs = ["Pictures", "Obrazy", "Zdjęcia", "Fotos"]  # Add any localized names
    for d in possible_dirs:
        full_path = os.path.join(home, d)
        if os.path.isdir(full_path):
            return full_path
    return home  # fallback to home if nothing found

def generate_cat_image():
    try:
        pictures = get_pictures_folder()
        url = "https://cataas.com/cat"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            filename = f"cat_{uuid.uuid4()}.jpg"
            filepath = os.path.join(pictures, filename)
            with open(filepath, "wb") as f:
                f.write(response.content)
            print(f"🐱 A random cat is waiting for you in: {filepath}")
        else:
            print("😿 No cat image for you, try again!")
    except Exception as e:
        print(f"😿 No cat image for you, try again! Error: {e}")

if __name__ == "__main__":
    loading_animation()
    generate_cat_image()
