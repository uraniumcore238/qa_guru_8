import os
import zipfile

def add_files_to_the_zip():
    zip_name = zipfile.ZipFile('my_test_zip.zip', 'w')
    for root, dirs, files in os.walk(r'./resources'):
        for file in files:
            zip_name.write(os.path.join(root, file))

    zip_name.close()


add_files_to_the_zip()
