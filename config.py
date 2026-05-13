import os
from dotenv import load_dotenv

load_dotenv()

# System identity
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = "MARKDEW Terminal"
VERSION = "2.0.0"
PHASE = "Phase 2: Active ⬛️⚡"

# Database tools
tools_db = {
    "image_ai": [
        {"name": "Midjourney v6", "desc": "Флагманська нейромережа для генерації зображень.", "power": "Дозволяє створювати преміум контент", "link": "https://midjourney.com"},
        {"name": "Leonardo AI", "desc": "Універсальний генератор артів з безліччю моделей.", "power": "Найкраще співвідношення якості", "link": "https://leonardo.ai"},
    ],
    "coding_ai": [
        {"name": "GitHub Copilot", "desc": "Твій AI-асистент прямо в IDE.", "power": "Пише код за коментарями, шукає баги", "link": "https://github.com/features/copilot"},
    ],
    "music_ai": [
        {"name": "Suno v3", "desc": "Генерація повноцінних треків із вокалом.", "power": "Створює аудіо для реліс та подкастів", "link": "https://suno.ai"},
    ],
    "automation_ai": [
        {"name": "Make (Integromat)", "desc": "Візуальний конструктор автоматизацій.", "power": "З'єднує 1000+ сервісів без коду", "link": "https://make.com"},
    ],
    "business_ai": [
        {"name": "Claude 3 Opus", "desc": "AI для глибокої аналітики та бізнес-стратегій.", "power": "Обробляє 150+ сторінок тексту", "link": "https://claude.ai"},
    ]
}
