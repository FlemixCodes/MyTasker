strings = {
    "ru": {
        # basic.py
        "get_privacy_text": "Этот документ описывает политику конфиденциальности для бота 'MyTasker'. \nЕсли у вас есть вопросы, свяжитесь с нами @whynoet @deathrideeet\n\nСобираемая информация\nМы собираем следующие данные:\n- Личные данные указанные в профиле, такие как имя, фамилия, username, ID (IDentificator) пользователя*\n- Сообщения, отправленные боту в личных сообщениях*\n- Команды, отправленные боту в личных сообщениях*\n* - наш бот не работает ни с чем кроме личных сообщений, данный функционал не умеет работать с чатами и так далее.\n\nИспользование данных\nСобранные данные используются для:\n- Обработки запросов пользователей\n- Исправления ошибок связанных с командами\n- Улучшения работы бота\n- Анализа использования сервиса\n\nХранение данных\nДанные хранятся на сервере без срока хранения.\nНекоторые данные могут удаляться по мере необходимости.\n\nПередача данных третьим лицам\nМы не передаем ваши данные третьим лицам без вашего согласия, за исключением случаев, предусмотренных законом.\n\nИзменения в политике конфиденциальности\nМы оставляем за собой право обновлять эту политику. Обо всех изменениях мы уведомим вас через наш бот или канал в телеграме (https://t.me/+9m0F4Kkww4Y0YTg6)\n\nКонтактная информация\nЕсли у вас есть вопросы, свяжитесь с нами @whynoet @deathrideeet.",
        "get_start_text": "Приветствую! Я бот который поможет тебе с планировкой задач и напомнит об их выполнении!",
        "get_ping_text": "{ej} Бот ответил за: <b>{lat}</b>мс.",
        "get_menu_text": "Выберите действие: ",
        # tasks.py
        "get_tasks_text": "Tasks",
        "get_task_text": "Task",
        "get_task_add_text": "Task_add",
        "get_task_delete_text": "Tasks_delete",
    }
}


def get_string(trackme, local="ru") -> str | None:
    if local == "ru":
        _str = strings.get(local, strings.get("ru"))

        if _str is None:
            return

        return str.get(trackme)
