import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from collections import Counter


# ==================== ЗАГРУЗКА ДАННЫХ ====================

def load_data():
    """Загружает данные из XML файлов"""
    try:
        # Загрузка пользователей
        users = []
        for user in ET.parse('users.xml').getroot().findall('user'):
            users.append({
                'user_id': int(user.find('user_id').text),
                'name': user.find('name').text,
                'age': int(user.find('age').text),
                'weight': int(user.find('weight').text),
                'fitness_level': user.find('fitness_level').text,
                'workouts': []
            })

        # Загрузка тренировок
        workouts = []
        for workout in ET.parse('workouts.xml').getroot().findall('workout'):
            w = {
                'user_id': int(workout.find('user_id').text),
                'type': workout.find('type').text,
                'duration': int(workout.find('duration').text),
                'distance': float(workout.find('distance').text or 0),
                'calories': int(workout.find('calories').text)
            }
            workouts.append(w)

            # Связываем с пользователем
            for user in users:
                if user['user_id'] == w['user_id']:
                    user['workouts'].append(w)
                    break

        print(f"Загружено: {len(users)} пользователей, {len(workouts)} тренировок")
        return users, workouts

    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return [], []


# ==================== ГРАФИКИ ====================

def show_workout_types_pie(workouts):
    """Показывает круговую диаграмму типов тренировок"""
    if not workouts:
        return

    types = Counter(w['type'] for w in workouts)
    colors = ['#FFFF00', '#CC0000', '#00FF00', '#FF0099', '#0000FF']

    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        types.values(),
        labels=types.keys(),
        autopct='%1.1f%%',
        colors=colors[:len(types)],
        startangle=90
    )

    # Улучшаем отображение текста
    for text in texts + autotexts:
        text.set_fontsize(11)

    ax.set_title('Распределение типов тренировок', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


def show_user_activity_bar(users):
    """Показывает столбчатую диаграмму активности пользователей"""
    if not users:
        return

    names = [u['name'] for u in users]
    counts = [len(u['workouts']) for u in users]

    # Сортируем по активности
    sorted_data = sorted(zip(names, counts), key=lambda x: x[1], reverse=True)
    names_sorted, counts_sorted = zip(*sorted_data)

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(names_sorted, counts_sorted, color='#00FFFF', edgecolor='black')

    # Подписываем значения
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.1,
                f'{int(height)}', ha='center', va='bottom', fontsize=10)

    ax.set_title('Активность пользователей (количество тренировок)',
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Пользователи', fontsize=12)
    ax.set_ylabel('Количество тренировок', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()


def show_calories_by_user_bar(users):
    """Показывает столбчатую диаграмму сожженных калорий по пользователям"""
    if not users:
        return

    names = [u['name'] for u in users]
    calories = [sum(w['calories'] for w in u['workouts']) for u in users]

    # Сортируем по калориям
    sorted_data = sorted(zip(names, calories), key=lambda x: x[1], reverse=True)
    names_sorted, calories_sorted = zip(*sorted_data)

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(names_sorted, calories_sorted, color='#000033', edgecolor='black')

    # Подписываем значения
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 10,
                f'{int(height)}', ha='center', va='bottom', fontsize=10)

    ax.set_title('Общее количество сожженных калорий по пользователям',
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Пользователи', fontsize=12)
    ax.set_ylabel('Калории', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()


def show_workout_types_stats(workouts):
    """Показывает столбчатую диаграмму средней длительности по типам тренировок"""
    if not workouts:
        return

    # Собираем статистику по типам
    type_stats = {}
    for w in workouts:
        t = w['type']
        if t not in type_stats:
            type_stats[t] = {'total_duration': 0, 'count': 0}
        type_stats[t]['total_duration'] += w['duration']
        type_stats[t]['count'] += 1

    # Рассчитываем среднюю длительность
    types = list(type_stats.keys())
    avg_durations = [type_stats[t]['total_duration'] / type_stats[t]['count'] for t in types]

    # Сортируем по длительности
    sorted_data = sorted(zip(types, avg_durations), key=lambda x: x[1], reverse=True)
    types_sorted, durations_sorted = zip(*sorted_data)

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(types_sorted, durations_sorted, color='#FF00CC', edgecolor='black')

    # Подписываем значения
    for bar, duration in zip(bars, durations_sorted):
        ax.text(bar.get_x() + bar.get_width() / 2, duration + 1,
                f'{duration:.0f} мин', ha='center', va='bottom', fontsize=10)

    ax.set_title('Средняя длительность тренировок по типам',
                 fontsize=14, fontweight='bold')
    ax.set_xlabel('Тип тренировки', fontsize=12)
    ax.set_ylabel('Средняя длительность (мин)', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()


# ==================== СТАТИСТИКА И ВЫВОД ====================

def print_stats(users, workouts):
    """Выводит статистику в консоль"""
    print("=" * 60 + "\nАНАЛИЗ ДАННЫХ ФИТНЕС-ТРЕНИРОВОК\n" + "=" * 60)

    if not users or not workouts:
        print("Нет данных для анализа")
        return

    # Общая статистика
    print(f"\n📊 ОБЩАЯ СТАТИСТИКА")
    print(f"   Всего тренировок: {len(workouts)}")
    print(f"   Всего пользователей: {len(users)}")
    print(f"   Сожжено калорий: {sum(w['calories'] for w in workouts)}")
    print(f"   Общее время: {sum(w['duration'] for w in workouts) / 60:.1f} часов")
    print(f"   Пройдено дистанции: {sum(w['distance'] for w in workouts):.1f} км")

    # Топ-3 пользователей
    user_stats = []
    for user in users:
        if user['workouts']:
            stats = {
                'name': user['name'],
                'workouts': len(user['workouts']),
                'calories': sum(w['calories'] for w in user['workouts']),
                'time': sum(w['duration'] for w in user['workouts']) / 60
            }
            user_stats.append(stats)

    user_stats.sort(key=lambda x: x['workouts'], reverse=True)

    print(f"\n🏆 ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ")
    for i, stats in enumerate(user_stats[:3], 1):
        print(f"   {i}. {stats['name']}: {stats['workouts']} тренировок, "
              f"{stats['calories']} калорий, {stats['time']:.1f} часов")

# ==================== ГЛАВНАЯ ФУНКЦИЯ ====================

def main():
    """Основная функция программы"""
    # Загрузка данных
    users, workouts = load_data()
    if not users or not workouts:
        return

    # Вывод статистики
    print_stats(users, workouts)

    # Построение графиков (будут показываться по одному)

    # График 1
    show_workout_types_pie(workouts)

    # График 2
    show_user_activity_bar(users)

    # График 3
    show_workout_types_stats(workouts)

    # График 4
    show_calories_by_user_bar(users)



if __name__ == "__main__":
    main()