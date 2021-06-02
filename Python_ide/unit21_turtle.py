import turtle as t

n,line = map(int, input().split())

t.shape("turtle")
t.color("green")
#t.speed("fastest")
t.speed("fast")
#t.speed("slow")
#t.speed("slowest")

t.begin_fill()

for i in range(n):
    t.fd(line)
    t.rt((360/n)*2)
    t.fd(line)
    t.lt(360/n)

t.end_fill()


