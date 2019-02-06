
e = 65537
n = 12796607342635867111206754476734515274718837882652630320699835607357836615892898261251694715974446864300133443315964076375933065313087826889545590450998241072867960082450440909642001164550224137499843995414227306329440598213258451035441031649398419008555310993301624577813292628817351740474227802982542142388129715454491365814743445153621218842992170003982738890195309574702656412538814929331740441758425194796047751973319188106048483461368595350857504850357379487861493013405052514833172010793237290057564383810415229359198575717816836939352390318412629222560024279634074941631880839626864093142138628443200473731691

c_fracs = continued_fraction(e / n).convergents()

test_message = 42
test_message_encrypted = pow(test_message, e, n)
d = 0
for i in xrange(len(c_fracs)):
    if pow(test_message_encrypted, c_fracs[i].denom(), n) == test_message:
        d = c_fracs[i].denom()
        break
print(d)