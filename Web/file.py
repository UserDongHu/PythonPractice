fr = open('Web/text.txt', 'rb')
fw = open('Web/text_copy.txt', 'wb')
data = fr.read()
print(data.decode('utf8'))
print(data)
fw.write(data)
fw.close()
fr.close()