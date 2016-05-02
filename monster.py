  
import random
COLORS = ['yellow','red', 'blue']  
  
print("Hello from Beth")
  
class Monster(object):

  min_hit_points = 1
  max_hit_points = 1
  min_experience = 1
  max_experience = 1
  weapon = 'sword'
  sound = 'roar'
  
  #attributes of a default monster
  def __init__(self, **kwargs):
    self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
    self.experience = random.randint(self.min_experience, self.max_experience)
    self.color = random.choice(COLORS)
    
    for key, value in kwargs.items():
      setattr (self, key, value)

  def battlecry(self):
    return self.sound.upper()

class Goblin (Monster):
    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'
  
class Troll (Monster):
    min_hit_points = 2
    max_hit_points = 6
    min_experience = 3
    max_experience = 4
    sound = 'growl'
    
class Dragon (Monster):
    min_hit_points = 2
    max_hit_points = 6
    min_experience = 3
    max_experience = 4
    sound = 'sworkf'
  
