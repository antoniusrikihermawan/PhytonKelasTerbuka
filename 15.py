data = 'ini adalah string'
print(data)
print(type(data))

# 1. cara membuat string
'''
 1. dengan menggunakan sigle quote '...'
 2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)
data = "menggunakan double quote"
print(data)

print("'Halo, apa kabar?'")
print('"Halo, apa kabar?"')
print("ini adalah string")

# 2. menggunakan tanda \
# membuat tanda ' menjadi string
print("mari shalat jum'at")
print('mari shalat jum\'at')

# backslash
print("c : \\user\\ucup")

# tab
print("ucup\t\t\t\totong, semakin jauh spasi nya")

# backspace
print("ucup \botong, spai jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed ->
print("baris pertama.\rbaris kedua.")
print("baris pertama.\r\nbaris kedua.")

# 3. String Literal atau raw

#hati hati
print('C :\nnew folder')
#menggunakan raw string
print(r'C:\new folder')
#multiline literal string
print("""
Nama : Riki
Kelas : XII RPL 1
""")
#multiline literal string dan raw
print(r"""
Nama : Riki
Kelas : XII RPL 1\new class
Website : https://riki.id
""")










