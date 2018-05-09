from Def_Parser import download,parser_HTML,input_vallues,collumn_and_line
import xlrd

excel_data_file=xlrd.open_workbook('./schedule.xlsx')
worksheet = excel_data_file.sheet_by_index(0)


print("Введите вашу группу")
gpoup=input_vallues()
fale,size_group=collumn_and_line(gpoup)


print("Введите день недели")
week=input_vallues()
size_week,fale=collumn_and_line(week)

fale,number_of_week=parser_HTML()


parity=number_of_week%2
schedule=[]
if parity==0 :
    size_week=size_week
else :
    size_week=size_week+1

for size_week in range(size_week,size_week+12,2):

    name_cells = worksheet.cell(size_week, size_group)
    schedule.append(str(name_cells).replace("empty:", "").replace("text:", "").replace(":", " ").replace("'", ""))

for i, value_list in enumerate(schedule, 1): # Аттрибут 1 - начало сортировки
     print(str(i)+")", value_list)
