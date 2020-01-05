""" 
Bite 233. Make a zipfile of the latest log files
"""
from datetime import datetime
from pathlib import Path, PosixPath, WindowsPath
from zipfile import ZipFile
import os

TMP = Path('./tmp')
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: PosixPath = LOG_DIR,
                     zip_file: str = ZIP_FILE,
                     n: int = 3) -> None:
    """zip_last_n_files

    create a zip file of files from logs dir based on their creation time
    
    Args:
        directory (PosixPath): path to logs folder.
        zip_file (str): where zip file should be saved
        n (int): amount of files to zip
    """

    zip_format = "{name}_{date}.log"
    date_format = "%Y-%m-%d"

    with ZipFile(zip_file, 'w') as zfile:
        for _, _, files in os.walk(directory):

            sorted_files = sorted(
                files,
                key=lambda x: os.stat(directory / x).st_ctime,
                reverse=True)[:n]

            for f in sorted_files:
                # date format
                dt = datetime.fromtimestamp(os.stat(
                    directory / f).st_ctime).strftime(date_format)

                new_name = zip_format.format(name=f.strip('.log'), date=dt)

                zfile.write(directory / f, new_name)


if __name__ == "__main__":
    zip_file = TMP / ZIP_FILE
    zip_last_n_files(LOG_DIR, zip_file, 3)
    for zip_logs in ZipFile(zip_file).namelist():
        print(zip_logs)