def ham_dist(num1, num2):
    return bin(num1 ^ num2).count('1')



print(ham_dist(0b10, 0b11))
print(ham_dist(0b1100, 0b0011))


def encode_val(n, k, val):
    return int(''.join(['1' * k if bit == '1' else '0' * k for bit in bin(val)[2:].zfill(n)]), 2)


def decode_val(n, k, encoded_val):
    val = bin(encoded_val)[2:]
    decoded_str = ''
    one = 0
    zero = 0
    for i in range(len((str(bin(encoded_val)[2:])))):
        if i % k == 0:
            if one > zero:
                decoded_str += '1'
            elif zero > one:
                decoded_str += '0'
            one = 0
            zero = 0
        if val[i] == '1':
            one += 1
        if val[i] == '0':
            zero += 1
    if one > zero:
        decoded_str += '1'
    elif zero > one:
        decoded_str += '0'
    return int(decoded_str, 2)



print(bin(encode_val(4, 3, 0b1011)))
print(bin(decode_val(4, 3, 0b111_000_111_111)))
print(ham_dist(encode_val(4, 3, 0b1001), encode_val(4, 3, 0b1000)))
print(bin(decode_val(4, 3, 0b110_010_011_101)))
ms = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912,
      2067455, 2093116, 1044928, 2064407, 6262776, 2027968, 4423680, 2068231,
      2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903,
      2067967, 2068456]
def decode_message(msg):
    decoded_msg = []
    for val in msg:
        decoded_val = decode_val(8, 3, val)
        decoded_msg.append(decoded_val)
    return decoded_msg
def decode_text(msg):
    decoded_msg = decode_message(msg)
    text = ''.join([chr(val) for val in decoded_msg])
    return text

decoded_text = decode_text(ms)
print(decoded_text)



def lev_dist(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[len(a)][len(b)]

string1 = "столб"
string2 = "слон"
distance = lev_dist(string1, string2)
print(f"Расстояние Левенштейна между '{string1}' и '{string2}': {distance}")


def lev_dist_ops(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    ops = [[''] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        dp[i][0] = i
        ops[i][0] = 'удаление' * i
    for j in range(len(b) + 1):
        dp[0][j] = j
        ops[0][j] = 'вставка' * j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            insert_cost = dp[i][j - 1] + 1
            delete_cost = dp[i - 1][j] + 1
            replace_cost = dp[i - 1][j - 1] + cost
            min_cost = min(insert_cost, delete_cost, replace_cost)
            dp[i][j] = min_cost
            if min_cost == replace_cost:
                if cost == 1:
                    ops[i][j] = 'замена'
                else:
                    ops[i][j] = 'равно'
            elif min_cost == insert_cost:
                ops[i][j] = 'вставка'
            else:
                ops[i][j] = 'удаление'

    return [ops[i][j] for i, j in zip(range(1, len(a) + 1), [len(b)] * len(a))]



operations = lev_dist_ops(string1, string2)
print(f"Операции для преобразования строки '{string1}' в строку '{string2}': {operations}")


def lev_dist_gen(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    operations = []
    i, j = len(a), len(b)
    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(f"del x[{i - 1}]")
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            operations.append(f"x.insert({i}, y[{j - 1}])")
            j -= 1
        else:
            if cost == 1:
                operations.append(f"x[{i - 1}] = y[{j - 1}]")
            i -= 1
            j -= 1

    return operations[::-1]


def test_lev_dist_gen():
    import random
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(10):
        a = ''.join(random.choices(alphabet, k=random.randint(5, 10)))
        b = ''.join(random.choices(alphabet, k=random.randint(5, 10)))
        operations = lev_dist_gen(a, b)
        print(f"Source: {a}, Target: {b}")
        print("Operations:")
        for op in operations:
            print(op)


test_lev_dist_gen()
