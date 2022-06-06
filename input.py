push(10)
push(20)
pop()
push(30)

for i in range(0, 5):
    pop()

for i in range(0, 5):
    push(10)
    multiPop(2)
    push(10)
    push(10)

