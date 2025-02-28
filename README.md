### [Eng]
TBD

# [Rus] Инструкция или как пользоваться этим репозиторием

Этот репозиторий был создан для студентов, которые хотят изучить автоматизированное тестирование на Python. Репозиторий имеет определенную структуру, которой стедунты должны придерживаться, чтобы все работало как это задумывалось.
Для этого отправьте мне ваш никнейм на GitHub, найти его можно в ссылке, вида: `https://github.com/<Ваш никнейм на GitHub>`.
После того, как я добавлю вас в проект в качестве коллабораторов, вы сможете его форкнуть. Подробнее о том, как сделать [форк](https://docs.github.com/ru/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) репозитория.
Как только репозиторий появился у Вас в аккаунте, Вы можете его [склонировать](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) на локальный компьютер.

## Структура репозитория

```
/pyjan2025
├── .github
│   ├── workflows       <-- Здесь лежат файлы для проверки вашего кода и запуска автоматических тестов 
│   │   ├── flake8.yaml
│   │   ├── ...
├── config
│   ├── tasks.json                <-- Файл конфигурации для запуска автотестов
├── homeworks                     <-- Папка с домашними заданиями
│   ├── hw5                       <-- Папка с домашним заданием #5
│   │   ├── hw5_solution.py       <-- Файл с решением для домашнего задания #5
│   ├── ...
│   ├── hw7                       <-- Папка с домашним заданием #7
│   │   ├── bulls_and_cows        <-- Папка для 1й задачи домашнего задания #7
│   │   │   ├── hw7_solution.py   <-- Файл с решением для домашнего задания #7
│   ├── ...
├── tests
│   ├── test_hw5.py               <-- Тесты для домашнего задания #5
│   ├── ...
│   ├── test_hw7.py               <-- Тесты для домашнего задания #7
│   ├── ...
├── .gitignore
├── README.md
├── conftest.py
├── requirements.txt
└── LICENSE
```

## Как пользоваться репозиторием
1. Перед началом использования создайте виртуальное окружение и установите необходимые зависимости
```bash
    $ python3 -m venv ./venv
    $ source venv/bin/activate
    $ python3 -m pip install -r requirements.txt
```
2. Для выполнения, на пример, домашнего задания #5 перейдите в папку
```bash
    $ cd homeworks/hw5`
```
3. Создайте новую ветку 
```bash
    $ git checkout -b homework<#>
```
4. Создайте файл, если его нету
```bash
    $ touch hw5_solution.py
```
6. Напишите решение задачи
6. Запустите тесты (см. подробности ниже)
7. Запустите линтеры (см. подробности ниже)
8. Выполните команду
```bash
    $ git add <.>/<filename>
```
9. Зафиксируйте изменения по средством коммита
```bash
    $ git commit -am <commit message>
```
10. Пуш изменений на удаленный репозиторий GitHub'a
```bash
    $ git push -u origin <branch name>
```
11. В меню `Actions` нажмите на большую зеленую кнопку: `I understand my forkflows, go ahead and enable them`
12. Создайте [Pull Request](https://docs.github.com/ru/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) из рабочей ветки(`<branch name>`) в основную ветку(`main` | `master`) ВАШЕГО репозитория 
12. Подождите пока не пройдут(ушпешно!) все автоматические проверки 
13. Если все хорошо, то можете делать мерж ваших изменений в основную ветку репозитория

Note: начиная с домашней работы #7, необходимо будет создавать вложенные папки, на пример:
`homeworks/hw7/bulls_and_cows`, в которых и будет располагаться файлы решение для конкретной задачи

Note 2: смотрите на импорты вверху модуля с тестами, они всегда подскажут Вам какая структура проекта, название модулей, функций, методов и классов ожидается. 

Note 3: для домашней работы #5 папка и файл в `homeworks` уже созданы, для последующих работ это надо будет делать самостоятельно 

## Линтеры
### Как запускать на локальной машине
- flake8
```commandline
flake8 tests/ homeworks/ --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 tests/ homeworks/ --count --max-complexity=10 --max-line-length=100 --statistics --ignore E501
```

- mypy
```commandline
mypy --ignore-missing-imports --install-types --non-interactive --exclude venv .
```

- pycodestyle
```commandline
pycodestyle --max-line-length=120 tests/ homeworks/
```

- pylint
```commandline
pylint --disable=C0112,C0114,C0115,C0116,C0103,R1705,R0903 *.py
```

- ruff
```commandline
ruff check --output-format=github .
```

## Автотесты
### Как включить тесты для домашних работ
Тесты включаются посредством флага в файле `config/tasks.json`. Перед запуском тестов PyTest считывает, файл конфигурации и по необходимости отключает необходимый модуль.  
- `"hw5": true` - включает тесты для домашней работы #5
- `"hw5": false` - выключает тесты для домашней работы #5

### Как запускать автотесты pytest на локальной машине
```commandline
pytest --tb=short --disable-warnings -v
```
