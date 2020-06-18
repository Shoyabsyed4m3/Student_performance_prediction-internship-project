from sklearn import linear_model
from django.shortcuts import render

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def index(request):
    return render(request,'index.html')

def performance(request):
   
    name = request.POST['name']
    first = float(request.POST['first'])
    second = float(request.POST['second'])
    third = float(request.POST['third'])
    fourth = float(request.POST['fourth'])

    ans=ml(name,first,second,third,fourth)
    ans=round(ans,2)
    if ans> 8.5:
        status="Awesome!"
    elif ans>7:
        status = "Good!Try to improve.."
    elif ans>5.5:
        status="Average!.."
    else:
        status="If you dont study you will fail.."
    return render(request,'result.html',{'result':ans,'names':name,'status':status})

def ml(name,first,second,third,fourth):
    


    df = pd.DataFrame({"name": ["shoyab", "harish", "faizan", "nivas", "reddy", "anil", "ganesh", "kishore", name],
                    "1st-sem": [7.5, 3.2, 6.2, 8.5, 7.4, 7.5, 4.2, 9.2, first],
                    "2nd-sem": [7.6, 3.1, 5.9, 8.3, 7.4, 8.5, 4.5, 9.5, second],
                    "3rd-sem": [8.2, 2.9, 5.6, 8.8, 8.4, 7.9, 3.8, 9.0, third],
                    "4th-sem": [7.9, 3.4, 6.4, 8.2, 7.4, 8.5, 4.8, 9.1, fourth]})


    train = df.head(9)
    #im taking test data and trained data same

    regr = linear_model.LinearRegression()
    x = np.array(train[["1st-sem", "2nd-sem", "3rd-sem"]])
    y = np.array(train[['2nd-sem']])
    regr.fit(x, y)


    y_hat = regr.predict(train[["1st-sem", "2nd-sem", "3rd-sem"]])


    l = y_hat.tolist()
    pre = []
    for i in l:
        pre.append(i[0])
    j = 0

    accuracy = []
    for i in df["4th-sem"]:
        accuracy.append(round(((i-pre[j])/i)*100, 5))
        j += 1

    result = pre[-1]
    return result

    
