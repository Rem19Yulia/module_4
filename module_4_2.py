def test_function():
    #inner_function()- ошибка
    def inner_function():
        return("Я в области видимости функции test_function")

# Вызов вложенной функции внутри test_function и вывод результата
    result = inner_function()
    print(result)

    inner_function()

# Попытка вызвать inner_function вне функции test_function
try:
    result = inner_function()
    print(result)

 #ошибка, так как inner_fuction не видна за пределами test_function
