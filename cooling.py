T = 100
T_air = 20
rate_of_change = (.055)
t = 0
print "Temperature: 100"
print "number of Minutes:20"
print "Temperature Per Minute Listed Below"
print "(Time, Temperature)"
while t<=19:
    print (t, T)
    T -= .055 * (T - T_air)
    t = t + 1
