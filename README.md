# aviato.kz.test

В данном репозитории находится код для тестового задания в компанию aviata.kz 

Проект написан на Flask, отображение с помощю REST API

# Реализация

Изначально в бд присуствуют записи рейсов на месяц с ценой boking_token и другими параметрами

Каждый день в 00:00 удаляются все записи предыдущего дня  записываются новы, день на 32 дня вперёд. При поиске билетов указывается город (fly_from fly_to), количество пассажиров, дата, а на стороне api идёт поиск нужных рейсов, проверка рейса по boking_token, перевод цен в KZT, фильтр по цене и отправка клиенту
