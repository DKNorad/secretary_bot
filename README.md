# Secretary Bot
A simple script that sorts all the files in a folder into separate folders based on filename extension

Changelog:\
2023-Sep-14: Completely reworked the script as it was not working properly under Linux.
Improved the code and used pathlib for all the work with the files.

TODO:
- ~~Add a way to check for duplicate file names.~~
  - Also added a prompt to confirm to overwrite the file.
- ~~Avoid the hardcoded extensions.~~
  - Using the mimetypes library for that.
  - Will still be using hard coded extensions for some files. A lot of the extensions are under "application" in the iana media types, but I want to separate them.
