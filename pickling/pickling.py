import pickle

#Имя файла в котором мы сохраним объект
shoplistfile = 'shoplist.data'
#Список покупок
shoplist = ['яблоки','манго','морковь']

#Запись в файл
f = open(shoplistfile,'wb') #Открываем файл для записи
pickle.dump(shoplist,f) #Помещаем (сбрасываем - "dump") объект в файл
f.close()

del shoplist  #Уничтожаем переменную "shoplist"

#Считываем из хранилища
f = open(shoplistfile,'rb')
storedlist = pickle.load(f) #Выгружаем объект из файла
print(storedlist)

