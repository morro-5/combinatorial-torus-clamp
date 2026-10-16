def get_primes_basis(n_count):
    """Генерация базиса первых n простых чисел"""
    primes = []
    chk = 2
    while len(primes) < n_count:
        if all(chk % p != 0 for p in primes):
            primes.append(chk)
        chk += 1
    return primes

def calculate_torus_invariants(n):
    """Вычисление детерминированных масштабов тора для любого n"""
    if n < 3:
        print("Ошибка: Для формирования локальной корзины шаг n должен быть не менее 3.")
        return
        
    primes = get_primes_basis(n)
    
    # 1. Емкость локальной корзины (L = P_{n-1} * P_n)
    L = primes[-2] * primes[-1]
    
    # 2. Количество интервалов на полном периоде (I_n = M_n / L)
    I_n = 1
    for p in primes[:-2]:
        I_n *= p
        
    # 3. Глобальный объем гиперграфа G(k) для k=0 (все уголки равны 1)
    # Формула: G(0) = (P_1 - 1) * (P_2 - 1) * ... * (P_n - 1)
    G_0 = 1
    for p in primes:
        G_0 *= (p - 1)
        
    # 4. Теоретическая макроплотность (Операция деления масштабов: G(0) / I_n)
    theory = G_0 / I_n
    
    print(f"\n==========================================")
    print(f"   РЕЗУЛЬТАТ СКАНИРОВАНИЯ ТОРА ДЛЯ n = {n}")
    print(f"==========================================")
    print(f"Базисные простые числа тора: {primes}")
    print(f"Стартовый резонансный интервал (L): {L}")
    print(f"Количество дискретных корзин (I_n): {I_n}")
    print(f"Теоретическая макроплотность (G(0)/I_n): {theory:.4f}")
    
    # Проверка ограничения: L < P_{n+1}^2
    next_prime = get_primes_basis(n + 1)[-1]
    constraint_met = L < next_prime**2
    print(f"Проверка КТО-зажима (L < P_{{n+1}}^2): {L} < {next_prime**2} -> {'ВЕРИФИЦИРОВАНО (Составные исключены)' if constraint_met else 'Вне резонанса'}")
    print(f"==========================================\n")

if __name__ == "__main__":
    print("--- Модуль детерминированного анализа числового кристалла ---")
    try:
        user_n = int(input("Введите интересующий шаг n для расчета тора: "))
        calculate_torus_invariants(user_n)
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")
