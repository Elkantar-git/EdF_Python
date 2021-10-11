arg = input('')
argl = len(arg)
argf = ''
etape = 0

for i in range(0, argl):
    etape += 1
    if arg[i] == ' ':
        etape -= 1
        next
    if etape % 2 == 0:
        argf = argf + arg[i].upper()
    else:
        argf = argf + arg[i].lower()

print(argf)