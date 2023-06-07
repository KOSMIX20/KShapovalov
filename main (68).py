def data(day,month,year):
    if day <= 0 or month <= 0 or year <0:
        return false 
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 31]
        if year % 4 == 0: months[1] = 29
        if day <= months[month - 1]:
            if month <= 12:
                return True
            return False
if __name__ == '__main__':
   день = int(input('день'))
   месяц = int(input('месяц'))
   год = int(input('год'))
   print(data(день, месяц, год))