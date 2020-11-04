def coversion(a):
    convert = a * 2
    return convert

print("Enter (MYR) amount")
myr = float(input())

result = float(coversion(myr))
formatted_float = "{:.2f}".format(result)
print(formatted_float)
