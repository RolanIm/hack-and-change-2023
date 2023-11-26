
# Трек Web от QIWI
## Кэширование запросов для уменьшения зависимости от внешних тестовых сред партнеров от QIWI

<p align="center">
<img src="https://img.shields.io/badge/Python-100000?style=for-the-badge&logo=python&logoColor=FFFFFF&labelColor=306998&color=black">

<img src="https://img.shields.io/badge/Redis-100000?style=for-the-badge&logo=redis&logoColor=FFFFFF&labelColor=d82c20&color=black">

<img alt='django' src='https://img.shields.io/badge/django-100000?style=for-the-badge&logo=django&logoColor=white&labelColor=black&color=black'/>

<img alt='postgreSQL' src='https://img.shields.io/badge/postgreSQL-100000?style=for-the-badge&logo=postgreSQL&logoColor=FFFFFF&labelColor=4169E1&color=black'/>

<img alt='Vue.js' src='https://img.shields.io/badge/Vue JS-100000?style=for-the-badge&logo=Vue.js&logoColor=000000&labelColor=4FC08D&color=black'/>

<img alt='Tailwind CSS' src='https://img.shields.io/badge/TailwindCSS-100000?style=for-the-badge&logo=Tailwind CSS&logoColor=FFFFFF&labelColor=06B6D4&color=black'/>
</p>

### Описание задачи
Разработайте приложение, которое будет автоматически запоминать запросы и соответствующие ответы от тестовых
сред партнеров, а при повторных запросах — использовать сохраненные данные. Цель создания приложения —
снижение зависимости тестовой среды QIWI от состояния внешних тестовых сред партнеров, например банковэквайеров или Системы быстрых платежей (СБП). 

## Установка
Клонируйте репозиторий на свой ПК:

```
git clone https://github.com/RolanIm/api_final_yatube-master.git
```

Install and create the virtual environment:

```
python3 -m venv venv
```

Activate a virtual environment:
- for windows:

  ```
  source venv/Scripts/activate
  ```
- for Unix/macOS:

  ```
  source venv/bin/activate
  ```

Install dependencies from the file requirements.txt: 

```
pip install -r requirements.txt
```
Go to the yatube_api directory:

```
cd reqs_caching/
```

Make migrations

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Run the `manage.py` file: 

```
python manage.py runserver
```

## Команда

- Орлова Екатерина - [@katikovka](https://t.me/katikovka)

- Худоёров Хисрав - [@kh_tj](https://t.me/kh_tj)

- Имангулов Ролан - [@rolan555](https://t.me/rolan555)

- Безбородова Виктория - [@vicitoriy](https://t.me/vicitoriy)

- Ханниев Сулейман - [@Hannyyew19](https://t.me/Hannyyew19)
