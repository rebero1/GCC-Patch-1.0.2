# modify this function, and create other functions below as you wish
def question06(portfolio):
    # modify and then return the variable below
    first_answer = len(portfolio[0])
       
        start = portfolio[0][0]
        ends   = portfolio[0][first_answer-1]
         

        answer =  len(portfolio)
        portfolio.reverse()

        for data in portfolio:
            data =str(data)
            if (data.startswith(start)) and data.endswith(ends):
                if answer-1 == 0:
                    return -1
                else:
                    return (answer  -1)
            answer = answer - 1
    
