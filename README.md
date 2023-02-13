# Django-Todolist-CBM
Django Todolist App based on ClassBasedModels

Описание проекта:

Список дел - это приложение, в котором пожно просматривать, создавать, изменять и удалять записи, которые являются описанием задач. Например "помыть посуду", "вынести мусор" или "приготовить суп". .

В каждой задаче есть название, говорящее о том, что нужно сделать, например "купить в магазине новый утюг". В каждой задаче есть отметка, выполнена она или нет (по умолчанию не выполнена). У каждой задачи есть дата и время создания, дата и время завершения. Время завершения задачи проставляется в момент проставления галочки о завершении задачи. Время завершения задачи убирается (становится null) в момент снятия галочки о завершении задачи.

Через админ сайт можно создавать, изменять и удалять задачи. Через админ сайт можно найти задачу по названию.

Admin Site-
http://127.0.0.1:8000/admin/

Креды superuser'a - admin admin

В браузере можно открыть страницу со списком всех незавершенных задач. В браузере можно открыть страницу с формой на добавление новой задачи и добавить ее. В браузере можно через форму изменить задачу. В браузере по кнопке можно удалить задачу.

Главная страница приложения-
http://127.0.0.1:8000/


Дополнительно в приложении реализована разбивка по категориям дел и фильтрация по категориям и отметке о выполнении.

Использованные зависимости устанавливаются с помощью команды *pip install -r requirements.txt*.

Запуск приложения осуществляется командой *python manage.py* runserver из папки с одноимённым файлом

![image](https://user-images.githubusercontent.com/88885135/218396629-6f5c3b12-a89d-4c0e-bab7-2ed56a2c1722.png)
