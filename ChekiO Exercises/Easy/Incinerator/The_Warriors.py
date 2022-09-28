"""One day, on a typical spring afternoon, Sir Ronald has been looking around his land, riding a horse. Nothing foretold troubles, when suddenly Sir Ronald heard a scream for help, coming from somewhere nearby:
- "Help! Help!" - shouted a piercing young girl's voice.
As a true knight, Sir Ronald couldn’t stay away and went to the lady’s rescue. Rushing in the direction from which the cry came, he saw a carriage. The girl peered out the window hoping to see someone who could help her.
- "Stop!"- ordered Sir Ronald to the coachman. - "By what right are you on my land?"
The coachman didn’t get a chance to open his mouth, as his master came out of the carriage.
- "My respects, noble sir. I had no idea that this land is yours. My bride and I were just going to my estate, not wanting to give anyone any trouble. "
- "A flat-out lie! I'm not his bride!" - the girl exclaimed from the window.
- "Explain yourself, Sir. What does that mean?",- said Sir Ronald.
- "Of course. The king of a neighboring country has promised his daughter and half his kingdom to the one who’ll save her from the outlaws who took her. I’ve defeated those bastards and now I’m taking the princess to her father. "
- "It's not true! They were in on it together They’ve kidnapped me on his order! I saw how he paid them a bag of gold!" - The princess didn’t stop taking for a second, trying to quickly describe the situation to the miraculously appeared savior.
- "Such behavior is unworthy of a knight! Prepare to die!",- exclaimed Sir Ronald, drawing his sword. - "Ha-ha-ha, simple-hearted nobleman! We’ll see about that..."
I'm sure that many of you have some experience with computer games. But have you ever wanted to change the game so that the characters or a game world would be more consistent with your idea of the perfect game? Probably, yes.
In this mission (and in several subsequent ones, related to it) you’ll have a chance "to sit in the developer's chair" and create the logic of a simple game about battles.
Let's start with the simple task - one-on-one duel. You need to create the class Warrior , the instances of which will have 2 parameters - health (equal to 50 points) and attack (equal to 5 points), and 1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case). In addition you have to create the second unit type - Knight, which should be the subclass of the Warrior but have the increased attack - 7. Also you have to create a function fight() , which will initiate the duel between 2 warriors and define the strongest of them. The duel occurs according to the following principle:
Every turn, the first warrior will hit the second and this second will lose his health in the same value as the attack of the first warrior. After that, if he is still alive, the second warrior will do the same to the first one.
The fight ends with the death of one of them. If the first warrior is still alive (and thus the other one is not anymore), the function should return True , False otherwise.

Example :

	chuck = Warrior()
	bruce = Warrior()
	carl = Knight()
	dave = Warrior()

	fight(chuck, bruce) == True
	fight(dave, carl) == False
	chuck.is_alive == True
	bruce.is_alive == False
	carl.is_alive == True
	dave.is_alive == False
	
Input: The warriors.

Output: The result of the duel (True or False).

How it is used: For computer games development. """

class Warrior:
    """The Warrior class
    
    parameters:
        health: The live of the warrior decrease every enemy attack.
        attack: The attack power of the warrior.
        is_alive: If the health is less or equal 0 this is False otherwise is True
        
    default parameters:
        health: 50
        attack: 5
        is_alive: True"""
    
    def __init__(self, is_alive=True, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = is_alive

class Knight(Warrior):
    """The Knight class
    
    parameters:
        health: The live of the knight decrease every enemy attack.
        attack: The attack power of the knight.
        is_alive: If the health is less or equal 0 this is False otherwise is True
        
    default parameters:
        health: 50
        attack: 7
        is_alive: True"""
    
    def __init__(self, is_alive=True, health=50, attack=7):
        self.health = health
        self.attack = attack
        self.is_alive = is_alive

def fight(unit_1, unit_2):
    """This is the fight fuction where we can watch the battle between our 2 warriors,
    and know who is the winner using the attack and resting the health 
    returning True if the first warrior wins, and False other wise
    
    parameters:
        unit_1: the first warrior (Knight or Warrior)
        unit_2: the second warrior (Knight or Warrior)
        
    output:
        True: if the unit_1 wins
        False: otherwise"""
    #print("The fight starts, The total health is: {}={} | {}={}".format(type(unit_1).__name__, unit_1.health, type(unit_2).__name__, unit_2.health))

    first_attack = 1
    while unit_1.health > 0 and unit_2.health > 0:
        if first_attack:
            first_attack = 0
            unit_2.health -= unit_1.attack
            #print("Attack made by {}, The total health is: {}={} | {}={}".format(type(unit_1).__name__, type(unit_1).__name__, unit_1.health, type(unit_2).__name__, unit_2.health))
        else:
            first_attack = 1
            unit_1.health -= unit_2.attack
            #print("Attack made by {}, The total health is: {}={} | {}={}".format(type(unit_2).__name__, type(unit_1).__name__, unit_1.health, type(unit_2).__name__, unit_2.health))
    if unit_1.health >0 and unit_2.health<=0:
        unit_2.is_alive = False
        return True
    else:
        unit_1.is_alive = False
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")



