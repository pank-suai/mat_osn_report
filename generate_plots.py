import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# Настройка шрифтов для русского языка
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 1. Метод прямоугольников
def plot_rectangles():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Функция
    def f(x):
        return (x - 2)**2 / 4 + 1
    
    a, b = 0.5, 3.5
    n = 4
    h = (b - a) / n
    
    # График функции
    x = np.linspace(a, b, 100)
    ax.plot(x, f(x), 'b-', linewidth=2, label='f(x)')
    
    # Прямоугольники (левые)
    for i in range(n):
        x_i = a + i * h
        x_next = x_i + h
        y_i = f(x_i)
        ax.bar(x_i + h/2, y_i, width=h, alpha=0.3, 
               edgecolor='red', linewidth=2, align='center')
    
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Метод левых прямоугольников', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig('images/003_rectangles.png', dpi=150, bbox_inches='tight')
    plt.close()

# 2. Метод трапеций
def plot_trapezoids():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    def f(x):
        return (x - 2)**2 / 4 + 1
    
    a, b = 0.5, 3.5
    n = 4
    h = (b - a) / n
    
    # График функции
    x = np.linspace(a, b, 100)
    ax.plot(x, f(x), 'b-', linewidth=2, label='f(x)')
    
    # Трапеции
    for i in range(n):
        x_i = a + i * h
        x_next = x_i + h
        y_i = f(x_i)
        y_next = f(x_next)
        
        # Рисуем трапецию
        vertices = [(x_i, 0), (x_i, y_i), (x_next, y_next), (x_next, 0)]
        from matplotlib.patches import Polygon
        poly = Polygon(vertices, alpha=0.3, facecolor='orange', 
                      edgecolor='red', linewidth=2)
        ax.add_patch(poly)
    
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Метод трапеций', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig('images/004_trapezoids.png', dpi=150, bbox_inches='tight')
    plt.close()

# 3. Метод Эйлера
def plot_euler():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Параметры
    x0 = 1.0
    t_start, t_end = 0.0, 2.0
    T = 0.5  # шаг
    
    # Функция f(t, x) = -x
    def f(t, x):
        return -x
    
    # Точное решение
    def exact(t):
        return x0 * np.exp(-t)
    
    # Точное решение (график)
    t_exact = np.linspace(t_start, t_end, 100)
    ax.plot(t_exact, exact(t_exact), 'b--', linewidth=2, 
            label='Точное решение')
    
    # Метод Эйлера
    t_euler = [t_start]
    x_euler = [x0]
    t = t_start
    x = x0
    
    while t < t_end:
        x = x + T * f(t, x)
        t = t + T
        t_euler.append(t)
        x_euler.append(x)
    
    ax.plot(t_euler, x_euler, 'ro-', linewidth=2, markersize=8,
            label='Метод Эйлера')
    
    ax.set_xlabel('t', fontsize=12)
    ax.set_ylabel('x', fontsize=12)
    ax.set_title('Метод Эйлера: dx/dt = -x, x(0) = 1', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig('images/005_euler.png', dpi=150, bbox_inches='tight')
    plt.close()

# 4. Метод Рунге-Кутта 4
def plot_rk4():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Параметры
    x0 = 1.0
    t_start, t_end = 0.0, 2.0
    T = 0.5  # шаг
    
    def f(t, x):
        return -x
    
    def exact(t):
        return x0 * np.exp(-t)
    
    # Точное решение
    t_exact = np.linspace(t_start, t_end, 100)
    ax.plot(t_exact, exact(t_exact), 'b--', linewidth=2,
            label='Точное решение')
    
    # Метод RK4
    t_rk4 = [t_start]
    x_rk4 = [x0]
    t = t_start
    x = x0
    
    while t < t_end:
        k1 = f(t, x)
        k2 = f(t + T/2, x + (T/2) * k1)
        k3 = f(t + T/2, x + (T/2) * k2)
        k4 = f(t + T, x + T * k3)
        
        x = x + (T/6) * (k1 + 2*k2 + 2*k3 + k4)
        t = t + T
        t_rk4.append(t)
        x_rk4.append(x)
    
    ax.plot(t_rk4, x_rk4, 'go-', linewidth=2, markersize=8,
            label='Метод RK4')
    
    ax.set_xlabel('t', fontsize=12)
    ax.set_ylabel('x', fontsize=12)
    ax.set_title('Метод Рунге-Кутта 4: dx/dt = -x, x(0) = 1', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig('images/006_rk4.png', dpi=150, bbox_inches='tight')
    plt.close()

# Генерация всех графиков
if __name__ == '__main__':
    print("Генерация графиков...")
    plot_rectangles()
    print("✓ Метод прямоугольников")
    plot_trapezoids()
    print("✓ Метод трапеций")
    plot_euler()
    print("✓ Метод Эйлера")
    plot_rk4()
    print("✓ Метод Рунге-Кутта 4")
    print("Все графики созданы!")