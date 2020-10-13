from pathlib import Path
from sys import argv
from shutil import move

directories = {
    # Archives
    "iso": "Archives", "tar": "Archives", "gz": "Archives", "7z": "Archives", "rar": "Archives", "zip": "Archives",
    
    # Code
    "c": "Code", "cpp": "Code", "css": "Code", "js": "Code", "html": "Code", "java": "Code", "py": "Code", "sh": "Code",
    
    # Documents
    "pdf": "Documents", "doc": "Documents", "docx": "Documents", "txt": "Documents", "ppt": "Documents", "ods": "Documents", "csv": "Documents", "rtf": "Documents",

    # Images
    "bmp": "Images", "gif": "Images", "jpeg": "Images", "jpg": "Images", "png": "Images", "svg": "Images", "tiff": "Images",
    
    # Music
    "aac": "Music", "flac": "Music", "m4a": "Music", "mp3": "Music", "ogg": "Music", "wav": "Music",
    
    # Videos
    ".avi": "Videos", "flv": "Videos", "mp4": "Videos", "mkv": "Videos", "mov": "Videos", "webm": "Videos",
}

def get_dir(filename):
    ext = filename.suffix[1:]
    return directories.get(ext, "Misc")

# If ran with an incorrect number of arguments
if len(argv) != 2:
    print(f"{'-' * 45}\nERROR!!! please specify a directory to organize\nExample: python organize.py \"Path/To/Directory\"\n{'-' * 45}")
    exit(1)

# Directory Path
PATH = Path(argv[1])

for filename in PATH.iterdir():
    
    path_to_file = filename.absolute()

    if path_to_file.is_file():
        destination = PATH / get_dir(filename)

        if not destination.exists():
            destination.mkdir()

        move(str(path_to_file), str(destination))
