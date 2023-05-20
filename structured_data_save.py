import os
import pandas as pd
from bs4 import BeautifulSoup


def extract_tags_from_files(txt_files):
    tags = set()
    for txt_file in txt_files:
        with open(txt_file, "r", encoding="utf-8") as f:
            html = f.read()
            soup = BeautifulSoup(html, "html.parser")
            for tag in soup.find_all():
                tags.add(tag.name)
    return tags


def save_tags_to_excel(tags, filename):
    df = pd.DataFrame({"Tag": list(tags)})
    df.to_excel(filename, index=False)
    print(f"Tags have been saved to {filename}")


def scan_txt(path):
    txt_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))

    return txt_files
