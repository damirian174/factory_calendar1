# Импортирование библиотек
import psycopg2
import datetime
# Подключение базы данных к питону
conn = psycopg2.connect(dbname="your dbname", user="postgres", password="Your password", host="127.0.0.1", port="5432")
cursor = conn.cursor()
# Установка курсора на область видимости
cursor.execute('select * from daysfactory')

p = input("Введите дату: ")# Установка необходимой,даты
p1 = [int(x) for x in p.split('-')]
#print(datetime.date(p1[0],p1[1],p1[2]))
m = 0# Переменная счетчика

u = []# Переменная списка
print('Введите срок выполнения')
srok = int(input())# Установка срока пользователем

values = cursor.fetchall() #Переменная базы данных в формате списка из набора кортежей

for i in values:
    if i[1] == datetime.date(p1[0],p1[1],p1[2]) and i[2] == 'workday': # Проверка условия на соответствие дате
#        s = i[0]+srok-1
#        print(i[2])
        for j in values[i[0]:]: # Проверка на соответсвие числу
            u.append(p)
            m+=1 #Счетчик
            if j[2] =='workday': # Логика работы по рабочим дням
                u.append(j[1])

                print(j[1], j[2])
            if j[2] =='weekend':
                continue
            elif m>srok:
                break

print(u[-1]) # Вывод итоговой даты в соответствии со сроком



#        for j in values:
 #           if s==j[0] and j[2]=='workday':

#                print(j[1])

#cursor.execute('select * from daysfactory')
#print(cursor.fetchall())

#for i in cursor.fetchall():
#    if i[2] =="weekend":
#        print(i[1], i[2])

# Закрытие баз данных
cursor.close()
conn.close()
