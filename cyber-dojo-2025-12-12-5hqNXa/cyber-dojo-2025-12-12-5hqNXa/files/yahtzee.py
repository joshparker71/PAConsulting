class Yahtzee():

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        total = 0
        total += d1
        total += d2
        total += d3
        total += d4
        total += d5
        return total

    @staticmethod
    def yahtzee(dice):
        match = True
        for die in range(len(dice)-1):
            if dice[die] !=dice[die+1]:
                match = False
        if match == True:
            return 50
        return 0
    
          
    @staticmethod
    def ones( d1,  d2,  d3,  d4,  d5):
        sum=[d1, d2,  d3,  d4,  d5].count(1)
        return sum
    

    @staticmethod
    def twos( d1,  d2,  d3,  d4,  d5):
        sum=([d1, d2,  d3,  d4,  d5].count(2))*2
        return sum
    
    @staticmethod
    def threes( d1,  d2,  d3,  d4,  d5):
        sum=([d1, d2,  d3,  d4,  d5].count(3))*3
        return sum
    

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
    def fours(self):
        sum = (self.dice.count(4))*4
        return sum
    

    def fives(self):
        sum = (self.dice.count(5))*5
        return sum

    def sixes(self):
        sum = (self.dice.count(6))*6
        return sum
    
    
    @staticmethod
    def score_pair( d1,  d2,  d3,  d4,  d5):
        max=0
        for die in range(1,7):
            if (([d1,  d2,  d3,  d4,  d5].count(die)) == 2):
                max = die*2       
        return (max)
    
    @staticmethod
    def two_pair( d1,  d2,  d3,  d4,  d5):
        max=[0]*6
        count=0
        for die in range(1,7):
            if (([d1,  d2,  d3,  d4,  d5].count(die)) == 2):
                max[die-1] = die*2
                count +=1
        if (count==2):
            return (sum(max))
        return 0
                    
                    
                    
    @staticmethod
    def four_of_a_kind( d1,  d2,  d3,  d4,  d5):
        for die in range(1,7):
            if (([d1,  d2,  d3,  d4,  d5].count(die)) == 4):
                max = die*4       
        return (max)
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        max=0
        for die in range(1,7):
            if (([d1,  d2,  d3,  d4,  d5].count(die)) == 3):
                max = die*3       
        return (max)
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        array = [d1,  d2,  d3,  d4,  d5]
        array.sort()
        if array == [1,2,3,4,5]:
            return 15
        return 0

        
        
        
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        array = [d1,  d2,  d3,  d4,  d5]
        array.sort()
        if array == [2,3,4,5,6]:
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        three = Yahtzee.three_of_a_kind( d1,  d2,  d3,  d4,  d5)
        pair =  Yahtzee.score_pair( d1,  d2,  d3,  d4,  d5)
        if (three !=0 and pair!=0):
                 return (three + pair)
        return 0
