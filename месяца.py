def season(num):
   if num == 12 or 1 <= num <= 2:
       print("Zima")
   elif  3 <= num <= 5:
       print("Vesna")
   elif 6 <= num <= 8:
       print("Leto")
   elif 9 <= num <= 11:
       print("Osen")
   else:
       print("Неправиольный число!")
n = int(input("Введите номер месяца: "))
season(n)