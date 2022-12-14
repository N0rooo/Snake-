def saveScore(score):
    with open('score.txt', 'w') as f:
        f.write(str(score))
        
def getHighScore():
    with open('score.txt', 'r') as f:
        hight_score = 0
        for line in f:
            if int(line) > hight_score:
                hight_score = int(line)
        return hight_score