## СБЕР. Тестовое задание.

FastAPI wеb-сервис для учета посещенных ресурсов

Сервис принимает список ссылок, которые были посещены работником.
* время посещения ссылок/ки считается временем принятия запроса сервисом 
* поле _status_ служит для передачи любых возникающих ошибок при обработке запроса

Сервис предоставляет полный список доменов, посещенных работником.
* список уникальных посещенных доменов
* можно задавать временные интервалы через параметры запроса
* поле _status_ служит для передачи любых возникающих ошибок при обработке запроса


***
### How to install
#### 1. Clone this repository
```
    git clone https://github.com/Boison88/Sber-GIGA
```

#### 2. Change Directory
```
    cd Sber-GIGA
```

#### 3. Install required packages from requirements.txt
```
    make install
```

#### 4. Run application
```
    make run
```

#### 5. Run tests
```
    make test
```