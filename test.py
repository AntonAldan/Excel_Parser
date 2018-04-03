#подключение библиотеки для чтение Excel файла 
import xlrd


#создаем переменную и открываем книгу указав путь к файлу 
excel_data_file=xlrd.open_workbook('/home/zyarx/Parser/Pass.xlsx')
#берем файл и обращаемся к нулевой странице (она же первая)
sheet=excel_data_file.sheet_by_index(0)

#создание массива что берет имена из Excel файла
batch_Names_wanted=[]
#оператор подсчета количества строк в файле
row_number=sheet.nrows


#  

if row_number >0 :
	for row in range(0,row_number):
		batch_Names_wanted.append(str(sheet.row(row)[145]).replace("empty:''",""))
	print("Количество запрашиваемых пакетов: ",len(batch_Names_wanted))
else :
	print ("Excel файл с данными пуст")
print('\n'.join(batch_Names_wanted))
