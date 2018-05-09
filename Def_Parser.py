import requests , bs4
import shutil
import xlrd


excel_data_file=xlrd.open_workbook('./schedule.xlsx')
worksheet = excel_data_file.sheet_by_index(0)


def download() :
    print("Идет скачивание файла")
    f = open('schedule.xlsx', 'wb')
    ufr = requests.get("https://www.mirea.ru/upload/medialibrary/9b0/IK-1k-17_18-vesna.xlsx")
    f.write(ufr.content)
    f.close()
    print("Скачивание файла завершено")

def parser_HTML() :

    s = requests.get('https://www.mirea.ru/')

    b = bs4.BeautifulSoup(s.text, "html.parser")
    data = b.select('.date_text')
    data_real = data[0].getText()

    #print("Сейчаc:" + data_real)

    data_real = str(data_real)

    l = len(data_real)
    integ = []
    i = 0
    while i < l:
        data_real_int = ''
        a = data_real[i]
        while '0' <= a <= '9':
            data_real_int += a
            i += 1
            if i < l:
                a = data_real[i]
            else:
                break
        i += 1
        if data_real_int != '':
            integ.append(int(data_real_int))

    return integ

def input_vallues() :
    vallues=input("Введите ваше значение:")
    vallues=vallues.upper()
    vallues=vallues.strip()
    vallues="text:"+"'"+str(vallues)+"'"
    return vallues

def collumn_and_line(vallues) :
    for collumn in range(92):
        for line in range(153):
            name_cells=worksheet.cell(collumn,line)
            name_cells=str(name_cells)
            if name_cells==vallues:
                return collumn, line
                break

