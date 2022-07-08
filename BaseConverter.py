class Transformer(object):
    decimal_digits = '0123456789'

    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)

    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))

    def _convert(self, number, fromdigits, todigits):
        rev_base = ''
        if len(fromdigits)==10:# fromdigits의 길이가 10인 경우== 10진수에서 n진수로 변환
            while number > 0:
                number, mod = divmod(number, len(todigits))
                rev_base +=todigits[mod]
            return rev_base[::-1]#역순으로 정리.
        else:
            ans=0
            for i,n in enumerate(number):
                num=fromdigits.find(n)#CODEC에서 n이 위치한 자리
                ans+= (len(fromdigits)**(len(number)-(i+1)))*num# (n^자리수)*CODEC에서 n이 위치한 자리
            return ans

print('1.base20,CODEC=0123456789abcdefghij')
base20 = Transformer('0123456789abcdefghij')
print(base20.from_decimal(1234))
print(base20.to_decimal('31e'),'\n')

print('2.binary,CODEC=01')
binary_transformer = Transformer('01')
print(binary_transformer.from_decimal(8))
print(binary_transformer.to_decimal('1000'),'\n')

print('3.hex,CODEC=0123456789ABCDEF')
hex_transformer = Transformer('0123456789ABCDEF')
print(hex_transformer .from_decimal(1234))
print(hex_transformer .to_decimal('4D2'),'\n')

print('4.base62,CODEC=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
base62_transformer =Transformer('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
print(base62_transformer.from_decimal(1234))
print(base62_transformer.to_decimal('Tu'),'\n')