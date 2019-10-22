# Розвертання проекту
1. Налаштування віртуального середовища та встановлення залежностей
    - встановити пітон та додати його в PATH
    - pip install virtualenv
    - py -m venv env
    - pip install -r requirements.txt
2. Запуск тестів з консолі
    - cd /*path_to_project*/
        pytest --browser-name /*назва браузера*/ --environment /*назва середовища*/ --html=report.txt
    - для запуску на декількох CPU додати до запуску опцію
        pytest -n /*кількість CPU*/
3. Результати тестів у корні проекту у файлі report.html