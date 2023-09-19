r_gray = int(input())
g_gray = int(input())
b_gray = int(input())

min_value = r_gray
if g_gray < min_value:  # searching for lowest value in r g b
    min_value = g_gray

if b_gray < min_value:  # still searching for lowest value in r g b
    min_value = b_gray

#  subtracting the minimum value from r g b to remove gray
r_nogray = r_gray - min_value
g_nogray = g_gray - min_value
b_nogray = b_gray - min_value

print(r_nogray, g_nogray, b_nogray)

# the more efficient way to subtract minval from rgb would be
print(r_gray - min_value,
      g_gray - min_value,
      b_gray - min_value)

# the most efficient way to do this whole thing would be
rgb = [r_gray, g_gray, b_gray]
min_value = min(rgb)
print(r_gray - min_value,
      g_gray - min_value,
      b_gray - min_value)
