from pathlib import Path, PurePath
from datetime import datetime
import mimetypes

mimetypes.init()

image = [ext for ext, type in mimetypes.types_map.items() if "image" in type]
video = [ext for ext, type in mimetypes.types_map.items() if "video" in type]
audio = [ext for ext, type in mimetypes.types_map.items() if "audio" in type]
font = [ext for ext, type in mimetypes.types_map.items() if "font" in type]
text = [ext for ext, type in mimetypes.types_map.items() if "text" in type]
document = ['.ppt', '.pptx', '.ods', '.xls', '.xlsx', '.pdf', '.odt', '.doc', '.docx', '.pps', '.odp', '.xlsm']
software = ['.exe', '.apk', '.bat', '.bin', '.jar', '.msi', '.app']
archives = ['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip']

folders = {'Images': image, 'Video': video, 'Audio': audio, 'Documents': document, 'Software': software,
           'Archives': archives, "Text": text, "Fonts": font, 'Miscellaneous': ['.*']}

curr_dir = Path(__file__).resolve().parent

file_exists = []

total_moved = 0
for folder_name, file_ext in folders.items():
    target_path = curr_dir.joinpath(folder_name)
    for ext in file_ext:
        for file in Path(curr_dir).glob("*" + ext):
            if Path.is_file(file) and file != PurePath(__file__):
                is_moved = False
                if not Path(folder_name).is_dir():
                    Path(Path.joinpath(curr_dir, folder_name)).mkdir(parents=True, exist_ok=True)
                try:
                    file.rename(target_path.joinpath(file.name))
                    is_moved = True
                except FileExistsError:
                    target_file = target_path.joinpath(file.name)
                    print(f"There is already a file with the name {file.name} in {target_path}.")
                    print(f"Last modified:\n"
                          f"{datetime.fromtimestamp(target_file.stat().st_ctime).strftime('%Y-%b-%d %H:%M:%S')}: {target_file}\n"
                          f"{datetime.fromtimestamp(file.stat().st_ctime).strftime('%Y-%b-%d %H:%M:%S')}: {file}\n")
                    while True:
                        answer = input("Do you want to overwrite the file? (Yes/No): ").lower()
                        if answer in ["yes", "y"]:
                            file.replace(target_path.joinpath(file.name))
                            is_moved = True
                            break
                        elif answer in ["no", "n"]:
                            break
                        else:
                            print("Invalid input. Please enter 'Yes' or 'No'.")
                if is_moved:
                    print(f'{file} ------------------> {target_path}')
                    total_moved += 1

print(f'\nTotal files moved: {total_moved}')
input("Press ENTER Key To Exit")
