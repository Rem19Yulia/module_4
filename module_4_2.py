def test_function():
   
    def inner_function():
        return("Я в области видимости функции test_function")

    result = inner_function()
    print(result)

    test_function()

# Попытка вызвать inner_function вне функции test_function
try:
    result = inner_function()
    print(result)

 #ошибка, так как inner_fuction не видна за пределами test_function
