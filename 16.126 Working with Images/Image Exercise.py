from PIL import Image

matrix1 = Image.open('word_matrix.png')
mask1 = Image.open('mask.png')

#matrix.show()
#mask.show()

print(type(matrix1))
print(type(mask1))
print(matrix1.info)
print(mask1.info)
print(matrix1.format_description)
print('-------')
print(matrix1.size)
print(mask1.size)

mask1_rez = mask1.resize((1015,559))
mask1_rez.putalpha(128)

mask1_rez_rot = mask1_rez.rotate(180)
#matrix1.putalpha(255)

#matrix1.paste(mask1_rez_rot,box=(0,0),mask=mask1_rez_rot)
matrix1.paste(mask1_rez,box=(0,0),mask=mask1_rez)

matrix1.show()