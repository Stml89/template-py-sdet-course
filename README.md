Content:
1. [English instruction](#eng-how-to-use-this-repository)
   - [Repository Structure](#repository-structure)
   - [How to Use the Repository](#how-to-use-the-repository)
   - [Setting Up the Environment](#setting-up-the-environment)
   - [Project Preparation](#project-preparation)
   - [Completing the Homework Assignment](#completing-the-homework-assignment)
   - [Linters](#linters)
   - [How to Run Linters Locally](#how-to-run-linters-locally)
   - [Automated Tests](#automated-tests)
   - [How to Run Pytest Locally](#how-to-run-pytest-locally)
2. [Инструкция или как пользоваться этим репозиторием](#title1)
   - [Структура репозитория](#title2)
   - [Как пользоваться репозиторием](#title3)
   - [Окружение](#title4)
   - [Подготовка проекта](#title5)
   - [Выполнение домашнего задания](#title6)
   - [Линтеры](#title7)
   - [Как запускать на локальной машине](#title8)
   - [Автотесты](#title9)
   - [Как включить тесты для домашних работ](#title10)
   - [Как запускать автотесты pytest на локальной машине](#title11)

# [Eng] How to use this repository

This repository was created for students who want to learn automated testing with Python. The repository follows 
a specific structure that students must adhere to in order to ensure everything works as intended. To get access, 
send me your GitHub username. You can find it in the link format: `https://github.com/<Your GitHub Username>`. Once 
I add you to the project as a collaborator, you will be able to fork it. Learn more about how to 
[fork](https://docs.github.com/ru/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) a repository. 
When the repository appears in your GitHub account, you can [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) 
it to your local computer.

## Repository Structure
```
/pyjan2025
├── .github
│   ├── workflows       <-- Contains files for code validation and automated test execution
│   │   ├── flake8.yaml
│   │   ├── ...
├── config
│   ├── tasks.json                <-- Configuration file for running automated tests
├── homeworks                     <-- Directory for homework assignments
│   ├── hw5                       <-- Homework #5 folder
│   │   ├── hw5_solution.py       <-- Solution file for Homework #5
│   ├── ...
│   ├── hw7                       <-- Homework #7 folder
│   │   ├── bulls_and_cows        <-- Directory for the first task of Homework #7
│   │   │   ├── hw7_solution.py   <-- Solution file for Homework #7
│   ├── ...
├── tests
│   ├── test_hw5.py               <-- Tests for Homework #5
│   ├── ...
│   ├── test_hw7.py               <-- Tests for Homework #7
│   ├── ...
├── .gitignore
├── README.md
├── conftest.py
├── requirements.txt
└── LICENSE
```

## How to Use the Repository

All subsequent steps must be performed only after you have cloned the repository to your local computer.

### Setting Up the Environment

1. Before you begin, create a virtual environment and install the required dependencies
```bash
    $ python3 -m venv ./venv
    $ source venv/bin/activate
    $ python3 -m pip install -r requirements.txt
```

### Project Preparation

Let's take Homework #5 as an example

2. Navigate to the `hw5` folder inside the `homeworks` directory
```bash
    $ cd homeworks/hw5
```
3. Create a new branch
```bash
    $ git checkout -b homework5
```
4. If the required folders and files do not exist, create them. (For the first homework assignments, these are 
already provided. For later assignments, you will need to create them yourself)
```bash
    $ mkdir hw7
    $ cd hw7
    $ touch hw7_solution.py
    $ touch __init__.py
```

### Completing the Homework Assignment

Homework #5 consists of 10 tasks. To submit the assignment, all tasks must be successfully completed. The assignment 
is considered accepted if all automated checks pass.

5. Write your solution

Example: You need to write a program that appends `ing` to given words.

- In `hw5_solution.py`, find the function `add_ing`
```python
def add_ing(s: str) -> str:
    pass
```
- The variable `s` receives a string to which you need to append `ing`
- Remove the pass keyword `pass`
```python
def add_ing(s: str) -> str:

```
- Write your code to solve the task
```python
def add_ing(s: str) -> str:
    s += 'ing'
```
- Return the result using the `return` keyword
```python
def add_ing(s: str) -> str:
    s += 'ing'
    return s
```
6. Run [autotests](#title3)
7. Run [linters](#title2)
8. If all previous checks passed, add the file (or changes) to Git for tracking
```bash
    $ git add .
```
or
```bash
    $ git add hw5
```
9. Commit your changes
```bash
    $ git commit -am <commit message>
```
10. Push the changes to YOUR remote GitHub repository
```bash
    $ git push -u origin homework5
```
11. `(*)` In the `Actions` menu, click the large green button: `I understand my workflows, go ahead and enable them`.
12. Create a [Pull Request](https://docs.github.com/ru/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) 
from your working branch(`<branch name>`) to the main branch(`main` | `master`) of YOUR repository.
12. Wait until all automated checks pass successfully.
13. If everything is correct, merge your changes into the main repository branch.

Note 1: Starting from Homework #7, you will need to create nested directories, such as: `homeworks/hw7/bulls_and_cows`, 
where solution files for specific tasks should be placed.

Note 2: You can always check the tests (for HW#5: `tests/test_hw5.py`) that will be used to verify your work.

Note 3: Look at the imports at the top of the test module. They will indicate the expected project structure, 
module names, function names, methods, and classes.

`(*)` This step should have been completed while working on HW#3. If you have already done this, you can skip it now.

## Linters

- https://habr.com/en/companies/oleg-bunin/articles/433480/
- https://semakin.dev/2020/05/python_linters/

### How to Run Linters Locally

**Important! Linters must be run from the project root**. Read some articles about linters and their importance:

- flake8
```bash
    $ flake8 tests/ homeworks/ --count --select=E9,F63,F7,F82 --show-source --statistics
    $ flake8 tests/ homeworks/ --count --max-complexity=10 --max-line-length=100 --statistics --ignore E501
```

- mypy
```bash
    $ mypy --ignore-missing-imports --install-types --non-interactive --exclude venv .
```

- pylint
```bash
    $ pylint --disable=C0112,C0114,C0115,C0116,C0103,R1705,R0903 *.py
```

- ruff
```bash
    $ ruff check --output-format=github .
```

## Automated Tests
### How to Enable Tests for Homework Assignments
Tests are enabled via a flag in `config/tasks.json`. Before running the tests, PyTest reads the configuration file 
and disables specific modules if necessary.  
- `"hw5": true` - enables tests for Homework #5
- `"hw5": false` - disables tests for Homework #5

### How to Run Pytest Locally
```bash
    $ pytest --tb=short --disable-warnings -v
```


# <a id="title1">[Rus] Инструкция или как пользоваться этим репозиторием</a>

Этот репозиторий был создан для студентов, которые хотят изучить автоматизированное тестирование на Python. Репозиторий имеет определенную структуру, которой стедунты должны придерживаться, чтобы все работало так как это задумывалось.
Для этого отправьте мне ваш никнейм на GitHub, найти его можно в ссылке, вида: `https://github.com/<Ваш никнейм на GitHub>`.
После того, как я добавлю вас в проект в качестве коллабораторов, вы сможете его форкнуть. Подробнее о том, как сделать [форк](https://docs.github.com/ru/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) репозитория.
Как только репозиторий появится у Вас в аккаунте, Вы можете его [склонировать](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) на локальный компьютер.

## <a id="title2">Структура репозитория</a>

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

## <a id="title3">Как пользоваться репозиторием</a>

Все последующие шаги необходимо делать, только после того, как вы склонировали репозиторий на локальный компьютер. 

### <a id="title4">Окружение</a>
1. Перед началом использования создайте виртуальное окружение и установите необходимые зависимости
```bash
    $ python3 -m venv ./venv
    $ source venv/bin/activate
    $ python3 -m pip install -r requirements.txt
```

### <a id="title5">Подготовка проекта</a>
Рассмотрим на примере домашнего задания #5

2. Для выполнения, перейдите в папку `hw5`, она находится в папке `homeworks`.
```bash
    $ cd homeworks/hw5
```
3. Создайте новую ветку
```bash
    $ git checkout -b homework5
```
4. Создайте папку и файл, если их нету(для первых домашних работ они уже созданы). Для последующих домашних работ 
папки и файлы необходимо будет создавать самостоятельно.
```bash
    $ mkdir hw7
    $ cd hw7
    $ touch hw7_solution.py
    $ touch __init__.py
```

### <a id="title6">Выполнение домашнего задания</a>
Домашняя работа #5 состоит из 10 задач. Для того чтобы сдать домашнюю работу - необходимо успешно выполнить все задания. 
Работа считается принятой - все автоматические проверки прошли успешно.

5. Напишите решение задачи

Пример: Вам необходимо разработать программу, которая добавляет `ing` к словам
- В файле `hw5_solution.py`, найдите функцию `add_ing`
```python
def add_ing(s: str) -> str:
    pass
```
- В переменную `s` будет передаваться строка к которой Вам надо будет добавить окончание `ing` 
- Удалите ключевое слово `pass`
```python
def add_ing(s: str) -> str:

```
- Напишите Ваш код, который будет решать эту задачу
```python
def add_ing(s: str) -> str:
    s += 'ing'
```
- Верните результат работы функции по средствам использования ключевого слова `return`
```python
def add_ing(s: str) -> str:
    s += 'ing'
    return s
```

6. Запустите [автотесты](#title9)
7. Запустите [линтеры](#title7)
8. Если все предыдущие проверки прошли успешно, то добавьте файл(изменения в нем) в отслеживаемые(индексируемые) Git
```bash
    $ git add .
```
или
```bash
    $ git add hw5
```
9. Зафиксируйте изменения по средством коммита
```bash
    $ git commit -am <commit message>
```
10. Загрузите изменения на СВОЙ удаленный репозиторий GitHub'a
```bash
    $ git push -u origin homework5
```
11. `(*)` В меню `Actions` нажмите на большую зеленую кнопку: `I understand my forkflows, go ahead and enable them`
12. Создайте [Pull Request](https://docs.github.com/ru/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) из рабочей ветки(`<branch name>`) в основную ветку(`main` | `master`) ВАШЕГО репозитория 
12. Подождите пока не пройдут(ушпешно!) все автоматические проверки 
13. Если все хорошо, то можете делать мерж ваших изменений в основную ветку репозитория

Note: Начиная с домашней работы #7, необходимо будет создавать вложенные папки, на пример:
`homeworks/hw7/bulls_and_cows`, в которых и будет располагаться файлы с решениями для конкретной задачи

Note 2: Вы всегда можете посмотреть на тесты(для HW#5: `tests/test_hw5.py`), которые будут запускаться для проверки Вашей работы. 

Note 3: Смотрите на импорты вверху модуля с тестами, они всегда подскажут Вам какая структура проекта, название модулей, функций, методов и классов ожидается.

`(*)` Это действие должно было быть пройденным еще во время работы над HW#3, если вы уже это сделали, то сейчас его можно пропустить.

## <a id="title7">Линтеры</a>
- https://habr.com/ru/companies/oleg-bunin/articles/433480/
- https://semakin.dev/2020/05/python_linters/

### <a id="title8">Как запускать на локальной машине</a>

**Внимание! Линтеры запускаются из корня проекта**. Прочитайте пару статей про линтеры и зачем они нужны:

- flake8
```bash
    $ flake8 tests/ homeworks/ --count --select=E9,F63,F7,F82 --show-source --statistics
    $ flake8 tests/ homeworks/ --count --max-complexity=10 --max-line-length=100 --statistics --ignore E501
```

- mypy
```bash
    $ mypy --ignore-missing-imports --install-types --non-interactive --exclude venv .
```

- pylint
```bash
    $ pylint --disable=C0112,C0114,C0115,C0116,C0103,R1705,R0903 *.py
```

- ruff
```bash
    $ ruff check --output-format=github .
```

## <a id="title9">Автотесты</a>
### <a id="title10">Как включить тесты для домашних работ</a>
Тесты включаются посредством флага в файле `config/tasks.json`. Перед запуском тестов PyTest считывает, файл конфигурации и по необходимости отключает необходимый модуль.  
- `"hw5": true` - включает тесты для домашней работы #5
- `"hw5": false` - выключает тесты для домашней работы #5

### <a id="title11">Как запускать автотесты pytest на локальной машине</a>
```bash
    $ pytest --tb=short --disable-warnings -v
```
