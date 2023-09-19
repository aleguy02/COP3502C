area_code, prefix, line_number = input().split()

print("Country  Phone Number")
print("-------  ------------")
print('U.S.     +1', end=' ')
print(f'({area_code}){prefix}-{line_number}')

print(f'Brazil   +55 ({area_code}){int(prefix) + 100}-{line_number}')
print(f'Croatia  +385 ({area_code}){prefix}-{int(line_number) + 50}')
print(f'Egypt    +20 ({int(area_code) + 30}){prefix}-{line_number}')
print(f'France   +33 ({prefix}){area_code}-{line_number}')