Задание: запуск автотестов для разных языков интерфейса

1. Создать GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
2. В файле conftest.py находится обработчик, который считывает из командной строки параметр language.
3. В файле conftest.py реализована логика запуска браузера с указанным языком пользователя. 
Браузер объявляется в фикстуре browser и передается в тест как параметр.
4. В файл test_items.py тест, который проверяет, что страница товара на сайте (http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/) содержит кнопку "Добавить в корзину"
5. Тест должен запускается с параметром language следующей командой:
pytest --language=es test_items.py и проходить успешно. 
6. Достаточно, чтобы код работал только для браузера Сhrome.