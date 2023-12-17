# Testicus
Testicus - это приложение в котором вы можете проходить чужие и создавать собственные тесты.  
Добавлять тесты могут только администраторы и авторизированные пользователи.  
Неавторизированным пользователям доступно только прохождение чужих тестов.  

Изменение чужого контента запрещено.  

### Используемые технологии:

Python  
Django  
DjangoRestFramework  

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone <web URL/SSH key>
```
```
cd testicus
```

Cоздать и активировать виртуальное окружение:  

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Перейти в директорию с файлом manage.py по адресу Tescticus/testicus

Выполнить миграции:

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Документация
Документация к проекту доступна по эндпоинту: http://127.0.0.1:8000/redoc/ 

### Проверка решения
Для проверки решения теста необходмио на ендпоинт http://127.0.0.1:8000/api/v1/tests/{id}/solution  
где {id} - id теста,  
Передать JSON следующего образца:
```
{
    "solutions": [
        {"question_id": id,
         "answer_id": id},
        {"question_id": id,
         "answer_id": id}
]
}
```
где:  
"solutions" - список вопросов и ответов,
"question_id" - id вопроса,
"answer_id" - id ответа на соответствующий вопрос
