import math

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
    """Вычисление детерминированных масштабов тора"""
    primes = get_primes_basis(n)
    
    # 1. Емкость локальной корзины (L = P_{n-1} * P_n)
    L = primes[-2] * primes[-1]
    
    # 2. Количество интервалов на полном периоде (I_n = M_n / L)
    # Вычисляется как произведение первых n-2 простых чисел
    I_n = 1
    for p in primes[:-2]:
        I_n *= p
        
    # 3. Глобальный объем гиперграфа G(k) для k=0 (уголок = 1)
    G_0 = primes[0] - 1
    for p in primes[1:]:
        G_0 *= (p - 1)
        
    # 4. Теоретическая макроплотность (Операция деления масштабов)
    theory = G_0 / I_n
    
    print(f"--- Verification for Step n = {n} ---")
    print(f"Basis Prime P_n: {primes[-1]}")
    print(f"Bucket Length (L): {L}")
    print(f"Number of Intervals (I_n): {I_n}")
    print(f"Theoretical Density (G(0)/I_n): {theory:.4f}")
    print(f"Constraint Checked (L < P_{{n+1}}^2): {L < get_primes_basis(n+1)[-1]**2}")

if __name__ == "__main__":
    # Демонстрационная верификация для шага n=5
    calculate_torus_invariants(5)
