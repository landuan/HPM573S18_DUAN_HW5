import numpy as np
import scr.FigureSupport as cls


class Game:
    def __init__(self,id):
        self.id=id
        self.rnd=np.random
        self.rnd.seed(self.id)
        self.random = np.random.random(size=20)
        self.game_list = list(self.random)
    def simulation(self):
        for k in range(0, 20):
            if self.random[k] > 0.5:
                self.game_list[k] = 'H'
            else:
                self.game_list[k] = 'T'
        m = 0
        for j in range(0, len(self.game_list) - 2):
            if self.game_list[j] == 'T' and self.game_list[j + 1] == 'T' and self.game_list[j + 2] == 'H':
                m += 1
                j = j + 3
            else:
                m += 0
                j = j + 1
        total_score = 100 * m - 250
        return total_score

class Cohort:
    def __init__(self,id,pop_size):

        self.game_list=[]
        self.cal_total_score=[]
        n=1
        while n<=pop_size:
            GameUnit=Game(id*pop_size+n)
            self.game_list.append(GameUnit)
            n+=1

    def simulatecohort(self):
        for game in self.game_list:
            value=game.simulation()
            self.cal_total_score.append(value)

    def get_expected_score(self):
        return sum(self.cal_total_score)/len(self.cal_total_score)


CohortTest=Cohort(2,1000)
CohortTest.simulatecohort()
Hist=CohortTest.cal_total_score
Min_score=min(Hist)
Max_score=max(Hist)
cls.graph_histogram(
    observations=Hist,
    title='Histogram',
    x_label='Values',
    y_label='Counts',
    legend='Number of patients')
print('The max score in the test is',Max_score)
print('The min score in the test is',Min_score)

count=0
for i in range(0,len(Hist)):
    if Hist[i]<0:
        count+=1
    else:
        count+=0
probability=count/float(1000)
print('The probability of losing money is',probability)