from flask import Blueprint, render_template, abort, request, redirect, url_for, flash, session

from webapp import app, db
from webapp.market.models import bikes, parts, lessons, Category
from webapp.registration.models import User
from webapp.registration.views import login

# Создаем мини-приложение market для управления магазином
market = Blueprint('market', __name__)


# Создаем маршрут к магазину с выводом доступных категорий
@app.route('/market/')
def market_page():
    categories = Category.query.order_by(Category.category_name.asc()).all()
    return render_template('market/market.html',
                           title='Магазин', categories=categories)


# Создаем маршрут согласно выбранной категории
@market.route('/market/<category>/', methods=['GET', 'POST'])
def category_page(category):
    categories = Category.query.order_by(Category.category_name.asc()).all()
    if not categories:
        abort(404)
    if category == 'bikes':
        return render_template('market/market_bikes.html',
                               title='Велосипеды', bikes=bikes)
    elif category == 'parts':
        return render_template('market/market_parts.html',
                               title='Запчасти', parts=parts)
    elif category == 'lessons':
        return render_template('market/market_lessons.html',
                               title='Занятия', lessons=lessons)
    elif category == 'category_create':
        flash('Пожалуйста авторизуйтесь для доступа к этой странице', 'danger')
        redirect(url_for('login'))
        if login:
            return redirect(url_for('category_create'))
    elif category == 'category_list':
        return redirect(url_for('category_list'))
    elif category == 'category_delete':
        return redirect(url_for('category_delete'))


# CREATE CATEGORY // Создаем новую категорию в магазине
@market.route('/market/category_create/', methods=['GET', 'POST'])
def category_create():
    if not login:
        flash('Пожалуйста авторизуйтесь для доступа к этой странице', 'danger')
    if request.method == 'POST':
        category_name = request.form.get('category_name')
        category_route = request.form.get('category_route')
        if not category_name or not category_route:
            flash('Пожалуйста заполните все поля', 'danger')
            return redirect(url_for('category_create'))
        category = Category(category_name=category_name, category_route=category_route)
        category_count = Category.query.filter_by(category_name=category_name).count()
        if category_count > 0:
            flash('Такая категория уже существует. Выберите другое имя','danger')
        else:
            db.session.add(category)
            db.session.commit()
            flash('Категория добавлена!', 'success')
            return redirect(url_for('market_page'))
    return render_template('market/category_create.html', title='Добавление категории')


# DELETE CATEGORY // Удаляем категорию category_name из базы данных
@market.route('/market/category_delete/', methods=['GET', 'POST'])
def category_delete():
    if request.method == 'POST':
        category_name = request.form.get('category_name')
        if not category_name:
            flash('Пожалуйста укажите имя категории для удаления', 'danger')
            return redirect(url_for('category_delete'))
        category = Category.query.filter_by(category_name=category_name).first()
        category_count = Category.query.filter_by(category_name=category_name).count()
        if category_count == 0:
            flash('Такой категории нет в базе','danger')
        else:
            db.session.delete(category)
            db.session.commit()
            flash('Категория удалена!', 'success')
            return redirect(url_for('market_page'))
    return render_template('market/category_delete.html', title='Удаление категории')


# LIST CATEGORY // Вывести список существующих категорий
@market.route('/market/category_list/', methods=['GET', 'POST'])
def category_list():
    if request.method == 'POST':
        categories_list = Category.query.order_by(Category.category_name.asc()).all()
        for category in categories_list:
            flash(f'{category.category_name}, {category.category_route}', 'success')
    return render_template('market/category_list.html', title='Список категорий')