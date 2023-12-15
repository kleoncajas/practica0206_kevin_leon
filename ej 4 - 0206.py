import urllib.request

url = "http://textfiles.com/adventure/aencounter.txt"
file = urllib.request.urlopen(url)
palabras = []
for line in file:
    decoded_line = line.decode("utf-8")
    palabras_n = decoded_line.split()
    palabras.extend(palabras_n)
print(len(palabras))