from collections import namedtuple
import os
import logging

logger = logging.getLogger('Namedtuple logging')
logger.setLevel(logging.INFO)

formatter = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
logger_file = logging.FileHandler('file_info.log')
logger.addHandler(logger_file)
logger_file.setFormatter(logging.Formatter(formatter))

Dir_content = namedtuple('Content',
                         ['is_file',
                          'is_directory',
                          'name',
                          'extension',
                          'parent_dir'])


def file_info(dir_path):

    if not os.path.isdir(dir_path) and not os.path.isfile(dir_path):
        raise ValueError(f'Path is neither a directory nor a file')
    elif os.path.isdir(dir_path):
        file_info = Dir_content(is_file=os.path.isfile(dir_path),
                                is_directory=os.path.isdir(dir_path),
                                name=os.path.dirname(dir_path),
                                parent_dir=os.path.basename(dir_path),
                                extension=None)
    elif os.path.isfile(dir_path):
        file_name, file_extension = os.path.splitext(dir_path)
        file_info = Dir_content(is_file=os.path.isfile(dir_path),
                                is_directory=os.path.isdir(dir_path),
                                name=os.path.basename(dir_path).split('.')[0],
                                parent_dir=os.path.relpath(dir_path),
                                extension=file_extension)
    logger.info(f"File info is successfully "
                f"placed to named tuple: \n{file_info}")


if __name__ == '__main__':
    file_info('/home/gaia/PycharmProjects/'
              'Getting Deep Into Python/loops/loop.py')
    file_info('/home/gaia/.cache/JetBrains/PyCharmCE2024.2/'
              'python_stubs/1020079574/_abc.py')
