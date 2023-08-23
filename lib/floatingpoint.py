# 浮動小数点誤差への対応

# 整数に近い数はround()で丸める
# 四捨五入ではなく偶数丸めなので0.5には注意

print(round(0.999999))  # 1 (int)
print(round(1.000001))  # 1 (int)

# Fractionクラス
# 誤差なしで計算できるがprint結果にクセあり

from fractions import Fraction

f = Fraction("123.456789")
print(f)  # 123456789/1000000
print(f * 1000000)  # 123456789

# Decimalクラス
# 誤差なしで計算できるがprint結果にクセあり
# getcontext().prec で有効数字桁数を指定できる

from decimal import Decimal, getcontext

d = Decimal("123.456789")
print(d)  # 123.456789
print(d * 1000000)  # 1.23E+8
print(int(d * 1000000))  # 123000000
getcontext().prec = 10
print(d * 1000000)  # 123456789.0
