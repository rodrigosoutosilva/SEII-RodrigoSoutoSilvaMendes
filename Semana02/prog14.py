import os

os.chdir('C:/Users/rodri/Google Drive/UFU/4- Sistemas Digitais/Semana02/osex')


for f in os.listdir():

    if f == '.txt':
        continue

    file_name, file_ext = os.path.splitext(f)

    f_title, f_course, f_number = file_name.split('-')


    f_title = f_title.strip()
    f_course = f_course.strip()

    f_number = f_number.strip()[1:].zfill(2)

    print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    new_name = '{}-{}{}'.format(f_number, f_title, file_ext)

    os.rename(f, new_name)