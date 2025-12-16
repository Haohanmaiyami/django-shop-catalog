# 🛍️ Django Shop Catalog

A small Django web app that demonstrates a **product catalog + blog + authentication & permissions**. 
It’s built as a portfolio-style project with **clean UI**, **CRUD**, and **demo data loading** via fixtures.

---

## ✨ Features

### 🧾 Catalog
- 📦 Products list + product details
- ➕ Create / ✏️ Edit / 🗑️ Delete products (access depends on permissions)
- 🗂️ Categories support
- 🖼️ Product images via Django `MEDIA` (local files)

### 📰 Blog
- 📝 Posts list + post details
- ➕ Create posts (permissions-based)

### 👤 Users & Permissions
- 🔐 Registration / Login / Logout
- ✅ Permission checks (e.g. `@permission_required`, CBV mixins like `LoginRequiredMixin`)
- 🛡️ Admin panel (`/admin/`) for full control

---

## 🧰 Tech Stack
- 🐍 Python
- 🌐 Django
- 🐘 PostgreSQL
- 🎨 Bootstrap 5
- 🐳 Docker (recommended to run PostgreSQL locally)

---

## 🚀 Quick Start (the exact “clean clone → run” flow)

### 1) Clone (SSH recommended)
```bash
git clone git@github.com:Haohanmaiyami/django-shop-catalog.git
cd django-shop-catalog
```

### 2) Create & activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -U pip
```

### 3) Install dependencies
If your `requirements.txt` installs normally:
```bash
pip install -r requirements.txt
```

If `requirements.txt` is in UTF‑16 (common on Windows), convert once:
```bash
iconv -f utf-16 -t utf-8 requirements.txt > requirements-utf8.txt
pip install -r requirements-utf8.txt
```

### 4) Start PostgreSQL via Docker (recommended)
This creates a **fresh** local database on port **5432**:
```bash
docker rm -f djangoshop_db 2>/dev/null

docker run --name djangoshop_db -e POSTGRES_DB=djangoshop -e POSTGRES_USER=djangoshop_user -e POSTGRES_PASSWORD=strong_password -p 5432:5432 -d postgres:16
```

### 5) Create `.env`
Create a file named `.env` in the project root:
```env
DB_NAME=djangoshop
DB_USER=djangoshop_user
DB_PASSWORD=strong_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

> ⚠️ Never commit `.env` (it must stay local).

### 6) Migrations
```bash
python manage.py migrate
```

### 7) Load demo data (products & categories)
```bash
python manage.py loaddata fixtures/catalog.json
```

### 8) Create an admin user (superuser)
```bash
python manage.py createsuperuser
```

### 9) Run the server
```bash
python manage.py runserver
```

Open in browser:
- 🛒 Products: http://127.0.0.1:8000/products/
- 📰 Blog: http://127.0.0.1:8000/blog/
- 🔐 Login: http://127.0.0.1:8000/users/login/
- 🛠️ Admin: http://127.0.0.1:8000/admin/

---

## 📦 Demo Data Notes
- Demo products are stored in `fixtures/catalog.json`.
- In a “clean database”, fixtures load without requiring specific existing users.
- After creating a superuser, you can open `/admin/` and manage everything there.

---

## 🖼️ Images / Media
This project uses Django `MEDIA` for product images. 
Depending on your Git settings, `media/` might be **ignored** (recommended) and not included in the repository.

If you don’t see images after cloning:
1) Ensure `MEDIA_URL` / `MEDIA_ROOT` are configured in `settings.py`.
2) Add your own images by creating products in the UI / admin.
3) (Optional) Keep a small `demo_media/` folder for portfolio screenshots instead of committing `media/`.

---

## 📄 License
This project is for learning & portfolio purposes.

---

# 🛍️ Django Shop Catalog

Небольшой Django‑проект для портфолио: **каталог товаров + блог + аутентификация и права доступа**. 
Цель — показать **CRUD**, работу с **PostgreSQL**, шаблонами и **permissions**.

---

## ✨ Что умеет проект

### 🧾 Каталог
- 📦 Список товаров + страница товара
- ➕ Создание / ✏️ редактирование / 🗑️ удаление товаров (с учётом прав)
- 🗂️ Категории
- 🖼️ Картинки товаров через `MEDIA`

### 📰 Блог
- 📝 Список постов + страница поста
- ➕ Создание постов (по правам)

### 👤 Пользователи и права
- 🔐 Регистрация / Вход / Выход
- ✅ Проверки прав (например, `@permission_required`, `LoginRequiredMixin` и т.п.)
- 🛡️ Админка (`/admin/`)

---

## 🧰 Стек
- 🐍 Python
- 🌐 Django
- 🐘 PostgreSQL
- 🎨 Bootstrap 5
- 🐳 Docker (рекомендуется для локального PostgreSQL)

---

## 🚀 Быстрый старт (чистый клон → запускается)

### 1) Клонирование (лучше SSH)
```bash
git clone git@github.com:Haohanmaiyami/django-shop-catalog.git
cd django-shop-catalog
```

### 2) Виртуальное окружение
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -U pip
```

### 3) Установка зависимостей
Если `requirements.txt` ставится нормально:
```bash
pip install -r requirements.txt
```

Если `requirements.txt` в UTF‑16 (часто после Windows) — конвертни один раз:
```bash
iconv -f utf-16 -t utf-8 requirements.txt > requirements-utf8.txt
pip install -r requirements-utf8.txt
```

### 4) Поднять PostgreSQL через Docker (рекомендуется)
Создаём чистую БД на порту **5432**:
```bash
docker rm -f djangoshop_db 2>/dev/null

docker run --name djangoshop_db -e POSTGRES_DB=djangoshop -e POSTGRES_USER=djangoshop_user -e POSTGRES_PASSWORD=strong_password -p 5432:5432 -d postgres:16
```

### 5) Создай `.env`
В корне проекта создай файл `.env`:
```env
DB_NAME=djangoshop
DB_USER=djangoshop_user
DB_PASSWORD=strong_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

> ⚠️ `.env` не коммитим (только локально).

### 6) Миграции
```bash
python manage.py migrate
```

### 7) Загрузить демо‑данные (товары и категории)
```bash
python manage.py loaddata fixtures/catalog.json
```

### 8) Создать суперюзера (админа)
```bash
python manage.py createsuperuser
```

### 9) Запустить сервер
```bash
python manage.py runserver
```

Открывай:
- 🛒 Товары: http://127.0.0.1:8000/products/
- 📰 Блог: http://127.0.0.1:8000/blog/
- 🔐 Вход: http://127.0.0.1:8000/users/login/
- 🛠️ Админка: http://127.0.0.1:8000/admin/

---

## 📦 Демо‑данные
- Демо‑товары лежат в `fixtures/catalog.json`.
- В “чистой” базе они загружаются без привязки к конкретным user_id.
- Дальше через `/admin/` можно назначать владельцев и управлять контентом.

---

## 🖼️ Картинки / Media
Проект использует Django `MEDIA` для картинок товаров. 
Чаще всего `media/` **не хранят в Git** (и это правильно). Поэтому после клона картинки могут не появиться.

Если картинок нет:
1) Проверь `MEDIA_URL` / `MEDIA_ROOT` в `settings.py`.
2) Добавь свои картинки через создание товара (UI или админку).
3) Для портфолио лучше хранить маленький набор скриншотов/демо‑медиа отдельно (`demo_media/`), а не коммитить `media/`.

---

## 📄 Лицензия
Учебный/портфолио проект.






# ДЗ Номер 1

# 🛍️ DjangoShop

Учебный проект интернет-магазина на Django. Реализованы главная страница и страница контактов с использованием шаблонов и Bootstrap.

## Возможности

- Главная страница с товаром
- Страница контактов с формой
- Навигация между страницами
- Стилизация через Bootstrap 5 (CDN)

## Технологии
Django 5.2

Bootstrap 5

Python 3.11

Git/GitHub

# ДЗ Номер 2

## Возможности

- Модели Category и Product
- Подключение PostgreSQL вместо SQLite
- Настройка админки с фильтрацией и поиском
- Загрузка тестовых данных через фикстуры
- Кастомная команда load_test_data

## Технологии
Django 5.2

PostgreSQL

Python 3.11

Pillow, ipython

# ДЗ Номер 3

Апдейт онлайн-магазина. Приложению добавлена динамика и страницы стали более привлекательны


## Возможности

- Страница со списком товаров (`products_list`)
- Страница одного товара (`products_detail`)
- Базовый шаблон (`base.html`) и подшаблон меню (`includes/inc_menu.html`)
- Обрезка описания товара до 100 символов
- Отображение изображений товаров
- Навигация между страницами

## Технологии

Django 5.2

PostgreSQL

Python 3.11

Bootstrap 5, Pillow

## ДЗ Номер 4

Добавлено приложение блога с полным CRUD, CBV и дополнительной логикой.

### Возможности

- Приложение `blog`, зарегистрировано в `INSTALLED_APPS`
- Модель `Blog` с полями:
  - `title`, `content`, `preview`, `created_at`, `is_published`, `views_count`
- Полный CRUD через CBV:
  - `BlogListView`, `BlogDetailView`, `BlogCreateView`, `BlogUpdateView`, `BlogDeleteView`
- Шаблоны:
  - `blog_list.html`, `blog_detail.html`, `blog_form.html`, `blog_confirm_delete.html`
- Все шаблоны используют `base.html` и `block content`
- Логика:
  - При просмотре статьи увеличивается `views_count`
  - В список выводятся только опубликованные записи (`is_published=True`)
  - После редактирования идёт редирект на `blog_detail`

### Технологии

Django 5.2  
Python 3.11  
Bootstrap 5  
Git/GitHub  
Работа с CBV, шаблонами, `get_object()`, `get_queryset()`, `get_success_url()`

## ДЗ Номер 5

Реализован CRUD для модели продуктов через django.forms с валидацией и стилизацией.

### Возможности

- Приложение `catalog`, зарегистрировано в `INSTALLED_APPS`
- Модель `Product` с полями:
  - `name`, `description`, `photo`, `category`, `price`, `created_at`, `updated_at`
- Форма `ProductForm` на основе `ModelForm`
- Полный CRUD через CBV:
  - `ProductCreateView`, `ProductUpdateView`, `ProductDeleteView`
- Маршруты:
  - `product_create`, `product_update`, `product_delete`
- Шаблоны:
  - `product_form.html`, `product_confirm_delete.html`
- Валидация:
  - `clean_name`, `clean_description` — запрещены слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар
  - `clean_price` — цена не может быть отрицательной
- Стилизация формы:
  - Через `__init__`, классы Bootstrap (`form-control`, `form-select`, `form-check-input`)

### Технологии

Django 5.2  
Python 3.11  
Bootstrap 5  
Git/GitHub  
Работа с ModelForm, ValidationError, CBV

# ДЗ Номер 6

## Аутентификация и ограничение доступа

Добавлено приложение пользователей и реализована базовая авторизация.

### Возможности

- Приложение `users`
- Модель пользователя от `AbstractUser`
  - Авторизация по email
  - Доп. поля: аватар, телефон, страна
- Регистрация с формой и отправкой письма
- Авторизация по email и паролю
- Ограничение доступа:
  - CRUD продуктов — только для авторизованных
  - Список товаров — доступен всем

### Технологии

Django 5.2  
Python 3.11  
PostgreSQL  
Bootstrap 5  
Pillow  
Git/GitHub  


# ДЗ Номер 7

## 🔐 Ограничение прав и роли модератора

Добавлены группы, кастомные права и логика доступа для владельцев и модераторов.

### ✅ Возможности

- 🧑‍💼 Добавлено поле `owner` в модель `Product`, связанное с пользователем
- 🛠️ При создании нового продукта поле `owner` заполняется автоматически текущим пользователем
- ✏️ Редактирование и удаление продукта разрешено только владельцу
- 🧹 Удаление также доступно модератору
- 📦 Добавлено поле `is_active` для управления публикацией товара
- 🛡️ Кастомное право `can_unpublish_product` — «может отменять публикацию»
- 🚫 Реализована функция `unpublish_product`, доступная только при наличии соответствующего права
- 👥 Группа **«Модератор продуктов»**:
  - Имеет право `can_unpublish_product`
  - Имеет стандартное право `delete_product`
- 🗃️ Фикстура с группой и назначенными правами добавлена в проект
- 💻 Шаблоны:
  - Кнопки редактирования и удаления отображаются только владельцу
  - Кнопка `Unpublish` отображается только модератору

### 🧰 Технологии

- Django 5.2  
- Python 3.11  
- PostgreSQL  
- Bootstrap 5  
- Git/GitHub  
- Работа с CBV, группами, правами, `@permission_required`, `LoginRequiredMixin`

Пароли: 
newuserwithnoaccess@mail.ru Xinkehu123 - есть один продукт с напитком,
brandnewuser@mail.ru Xinyonghu123 - ничего нет, просто юзер,  
justuser@mail.ru Zhishiyonghu123 - просто юзер,
moderator1@mail.ru password madelatuoli123 - модератор,
testuser@mail.ru 12345678, 

admin@mail.ru, 12345

# ДЗ Номер 8

## 🚀 Кеширование и бизнес-логика

Добавлено кеширование с использованием Redis, реализована сервисная функция для отображения товаров по категориям.

### Возможности

- Низкоуровневое кеширование списка товаров на главной (`products_list`)
  - Используется Redis и `django.core.cache`
  - Для неавторизованных пользователей данные берутся из кеша
  - Ключ кеша: `products_list`
- Кеш сбрасывается автоматически при изменении данных
- Кеширование страницы одного товара (`product_detail`) с помощью декоратора `@cache_page` на 15 минут
- Сервисная функция `get_products_by_category(category_id)`
  - Возвращает активные продукты в категории
- Представление `ProductsByCategoryView` (на основе `View`)
  - Получает данные через сервис
  - Отображает шаблон `products_by_category.html`
- URL: `/category/<int:category_id>/`
- Шаблон оформлен с использованием Bootstrap

## Технологии

- Django 5.2  
- Python 3.11  
- PostgreSQL  
- Redis  
- Bootstrap 5  
- Git/GitHub  

