Для запуска приложения необходимо:
1. Загрузить в папку со скриптом файл sqlite "domains.db", содержащий список доменов.

   1.1. Файл "domains.db" должен иметь структуру:
     
   Таблица domains - содержит колонки name, project_id. Таблица заполнена набором доменов.
Таблица rules содержит колонки regexp, project_id. Таблица пустая.
2. Запустить файл main.py интерпретатором python 3.8 версии и выше