from pythonisms.pythonisms import ShowStuffOff

def test_class():
    person3 = ShowStuffOff('Test person', 'Fake Python', 10)
    
    assert print(person3) == 'Software Dev Test person with current skills of Fake Python and money available $10'
