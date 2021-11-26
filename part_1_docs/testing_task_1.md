### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card): 
    if card.value = 1: # to check if the card.value equals 1 '=' needs to be changed to '=='
      return True
    else # missing colon after 'else'
      return False
   

  dif highest_card(self, card1 card2): # typo - 'dif' needs to be changed to 'def', no comma after 'card1'
  if card1.value > card2.value: # this line (and the following lines) should be indented
    return card # 'card' has not been defined, it should be changed to 'card1'
  else:
    return card2
  


def cards_total(self, cards):
  total # no value assigned to the variable, it should be changed to 'total = 0'
  for card in cards:
    total += card.value
    return "You have a total of" + total # this line should not be indented, int cannot be added to a string, should be changed to str(total)
  
```
