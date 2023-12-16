def count_numbers(L, R, primes):
    count = 0
    for num in range(L, R+1):
        divisible = False
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                divisible = True
                break
        if not divisible:
            count += 1
    return count

def generate_primes(N):
    primes = []
    is_prime = [True] * (N+1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= N:
        if is_prime[p]:
            for i in range(p * p, N+1, p):
                is_prime[i] = False
        p += 1

    for num in range(2, N+1):
        if is_prime[num]:
            primes.append(num)

    return primes

# Đọc input
while True:
    L, R = map(int, input().split())
    if L == -1 and R == -1:
        break
    N = int(input())

    # Tạo danh sách các số nguyên tố từ 2 đến N
    primes = generate_primes(N)

    # Gọi hàm đếm số lượng số thỏa mãn và in ra kết quả
    result = count_numbers(L, R, primes)
    print(result)