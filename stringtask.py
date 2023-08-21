s = 'foo'
t = 'bar'
#('barf' in 2 * (s + t))
#print(ord('foo'))
#s = 'foobar'
r=s[0] + s[-1]
print(r)
r=s[::-1][-1] + s[len(s)-1]
print(r)
r=s[::-1][::-5]
print(r)
r=s[::5]
print(r)
r=s[::-5]
print(s)
