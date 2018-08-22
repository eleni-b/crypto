#! /usr/bin/env python

from Crypto.Hash import SHA256

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in xrange(ord(c1), ord(c2)+1):
        yield chr(c)

c = 'the_password_is_'

text = '1600d5e39d9f0451302b4aef0c48f24d575bf01f8213233de705b9f1a3ab28db'       

for c1 in char_range('a','z') :
    for c2 in char_range('a','z') :
        for c3 in char_range('a','z') :
            for c4 in char_range('a','z') :
                for c5 in char_range('a','z') :
                    for c6 in char_range('a','z') :
                        a = [c1,c2,c3,c4,c5,c6]
                        b = ''.join(a)
			d = c + b
			h = SHA256.new()
			h.update(d)
                        if h.hexdigest() == text : 
                            print 'found!'
			    print d

