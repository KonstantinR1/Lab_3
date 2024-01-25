class StringManipulator:
    def getstring(self):
        self.a = input()

    def printstring(self):
        print(self.a.upper())
        
# Создаем экземпляр класса
stringManipulator = StringManipulator()

# Вызываем метод getstring для ввода строки с консоли
stringManipulator.getstring()

# Вызываем метод printstring для вывода строки в верхнем регистре
stringManipulator.printstring()