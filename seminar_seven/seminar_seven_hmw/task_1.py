import os

dir = '/home/gaia/PycharmProjects/Getting Deep Into Python/seminar_seven/pictures'
print(os.listdir(dir))

def grp_rnm_fls(dir, files_qty_to_raname=2, #сколько файлов переименовать
                digits_qty_in_name_sequence=2, # колиечество цифр в порядковом номере
                input_file_ext= 'txt',  #расширение исходного файла
                output_file_ext= 'odt', # расширение файла на выходе
                range_of_input_name=[2,8] # диапазон сохраняемых букв начального имени
                ):

    if not os.path.isdir(dir):
        print('Directory is not found')

    files = [f for f in os.listdir(dir) if f.endswith(input_file_ext)]

    if not files:
        print('Files are not found')
        return

    format_seq_dig = f"{{:0{digits_qty_in_name_sequence}d}}"

    for index, file_name in enumerate(files, start=1):
        input_file_name = os.path.splitext(file_name)[0]

        if range_of_input_name: # извлекаем часть имени файла из диапазона
            start, end = range_of_input_name # указанный диапазон
            file_name_part = input_file_name[start-1: end] # извлекаемая часть имени для переименования
        else:
            file_name_part = input_file_name

        new_file_name = f'{file_name_part} {files_qty_to_raname} {format_seq_dig.format(index)}.{output_file_ext}'

        old_file_path = os.path.join(dir, input_file_name)
        new_file_path = os.path.join(dir, new_file_name)

        os.rename(old_file_path, new_file_path)
        print(f'{input_file_name} renamed to {new_file_name}')



if __name__ == "__main__":
    grp_rnm_fls('/home/gaia/PycharmProjects/Getting Deep Into Python/seminar_seven/pictures', files_qty_to_raname=2,
                digits_qty_in_name_sequence=1, input_file_ext='svg', output_file_ext='json', range_of_input_name=[2,6])
