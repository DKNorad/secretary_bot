import fnmatch
from os import path, listdir, getcwd
from pathlib import Path
from shutil import move

image = ['*.bmp', '*.jpg', '*.jpeg', '*.gif', '*.png', '*.ico', '*.psd']
video = ['*.mov', '*.wmv', '*.avi', '*.avchd', '*.flv', '*.f4v', '*.swf', '*.mkv', '*.webm', '*.mpg', '*.mpv', '*.mpe', '*.mpeg-2', '*.mpeg', '*.m4p', '*.m4v', '*.mp4', '*.ogg']
audio = ['*.mp3', '*.aif', '*.cda', '*.mid', '*.midi', '*.mpa', '*.wav', '*.wma', '*.wpl']
document = ['*.txt', '*.ppt', '*.pptx', '*.ods', '*.xls', '*.xlsx', '*.pdf', '*.odt', '*.html', '*.htm', '*.doc', '*.docx', '*.pps', '*.odp', '*.xlsm']
software = ['*.exe', '*.apk', '*.bat', '*.bin', '*.jar', '*.msi']
archives = ['*.7z', '*.arj', '*.deb', '*.pkg', '*.rar', '*.rpm', '*.tar.gz', '*.z', '*.zip']
total_moved = 0


def move_file(src: str, dst: str, pattern: list = '*.*'):
    global total_moved
    for ext in pattern:
        for f in fnmatch.filter(listdir(src), ext):
            if path.isfile(f) and f != 'SecretaryBot.exe':
                if not path.isdir(dst):
                    Path(dst).mkdir(parents=True, exist_ok=True)
                move(path.join(src, f), path.join(dst, f))
                print(f'{f} ------------------> {dst}')
                total_moved += 1


curr_dir = getcwd()
move_file(curr_dir, curr_dir + '\\Images', image)
move_file(curr_dir, curr_dir + '\\Video', video)
move_file(curr_dir, curr_dir + '\\Audio', audio)
move_file(curr_dir, curr_dir + '\\Documents', document)
move_file(curr_dir, curr_dir + '\\Software', software)
move_file(curr_dir, curr_dir + '\\Archives', archives)
move_file(curr_dir, curr_dir + '\\Miscellaneous')

print(f'\nTotal files moved: {total_moved}')
input("Press ENTER Key To Exit")
