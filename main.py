import os
import io
import time
import zipfile
import re
import time

def unzip_directory(directory):
    # This function unzips and then delete all zip files
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if re.search(r'\.txt$',filename):
                print("Textfile be found")
                break
            if re.search(r'.zip$',filename):
                zip_lastfile = filename
                to_path = os.path.join(root, filename.split('.zip')[0])
                zipped_file = os.path.join(root,filename)
                if not os.path.exists(to_path):
                    os.makedirs(to_path)
                with zipfile.ZipFile(zipped_file, 'r') as zfile:
                    zfile.extractall(root)
                os.removedirs(to_path)
                time.sleep(1)
                os.remove(zfile.filename)
                    # deletes zip file


def exists_zip(directory):
    # This function returns T/F whether any .zip file exist
    is_zip=False
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if re.search(r'\.zip$',filename):
                is_zip = True
    return is_zip


def unzip_directory_recursively(directory, max_iter=2022):
    print("Does the directory path exits?", os.path.exists(directory))
    iterate = 0

    while exists_zip(directory) or iterate < max_iter:
        unzip_directory(directory)
        iterate += 1

    pre ="Did not " if iterate < max_iter else "Done"
    print(pre, "time out based on max_iter limit of", max_iter)


location ='C:/Users/Adrian Höppener/Downloads/Projekt/'
unzip_directory_recursively(location)
print('done')