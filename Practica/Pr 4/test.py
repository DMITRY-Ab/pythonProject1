import Hand

print(Hand.read_file('read'))
Hand.write_file('save', Hand.read_file('read'))