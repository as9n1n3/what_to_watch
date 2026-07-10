from flask import Flask
from flask_migrate import Migrate
from opinions_app.models import db
from opinions_app.views import register_views
from opinions_app.error_handlers import register_error_handlers
from opinions_app.cli_commands import register_commands
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()


def create_app():
    app = Flask(__name__)
    
    # Загрузка конфигурации
    app.config.from_object('settings.Config')
    
    # Инициализация расширений
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Регистрация обработчиков
    register_error_handlers(app)
    register_views(app)
    register_commands(app)
    
    return app