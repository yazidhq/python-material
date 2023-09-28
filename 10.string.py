data = "Ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)
data = "Menggunakan double quote"
print(data)

# string dalam string
print('"hallo, apakabar?"')
print("'hallo, apakabar?'")
print("Ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari solat jum\'at')
print('g\'day, ins\'t it?')

# backslash
print("C:\\user\\yazid")

# tab
print("user\t\t\totong, jauhan")

# backspace
print("yazid \botong, jadi deketan")

# newline
# LF -> line feed (untuk unix dan macos)
print("baris pertama. \nbaris kedua.")
# CR -> carriage return (untuk commodore, acorn (old os))
print("baris pertama. \rbaris kedua.")
# CRLF -> line feed carriage return (windows)
print("baris pertama. \r\nbaris kedua.")

# 3. String Literal atau raw
print('C:\new folder')  # hati hati
# menggunakan raw string
print(r'C:\new folder')  # akan dianggap string semua

# multiline literal string
print("""
    Nama : Yazid
    NPM : 31120173
""")

# multiline literal string dan raw
print(r"""
    Nama : Yazid
    NPM : 31120173
    website : www.yazidsblog.com/data
""")
