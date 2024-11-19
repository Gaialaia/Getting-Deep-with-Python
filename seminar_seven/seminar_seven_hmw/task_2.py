import os
import zipfile


def make_zip(dir_path_to_archive, dest_dir):
    with zipfile.ZipFile('seminar_seven.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
        for address, dirs, files in os.walk(dir_path_to_archive):
            for file in files:
                file_path = os.path.join(address,file)
                zf.write(file_path,os.path.relpath(file_path, dir_path_to_archive))

os.system('seminar_seven.zip')
# print(os.getcwd())
print(os.path.relpath('/home/gaia/PycharmProjects/Getting Deep Into Python/seminar_seven'))

if __name__ == "__main__":
    make_zip('/home/gaia/PycharmProjects/Getting Deep Into Python/seminar_seven',
             '/home/gaia/PycharmProjects/Getting Deep Into Python/flower')


os.system('seminar_seven.zip')