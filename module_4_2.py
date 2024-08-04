def test_function():
    #inner_function()- ошибка
    def inner_function(x):
        print("Я в области видимости функции test_function")

    inner_function()


    #inner_function() #ошибка, так как inner_fuction не видна за пределами test_function
