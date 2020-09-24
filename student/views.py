from sklearn import linear_model
from django.shortcuts import render

import pandas as pd
import numpy as np


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
    df = pd.read_csv('studentsdata.csv')
    regr = linear_model.LinearRegression()
    x = np.array(df[["1st-sem", "2nd-sem", "3rd-sem",'4th-sem']])
    y = np.array(df['5th-sem'])
    regr.fit(x, y)
    predicted = regr.predict([[first],[second],[third],[fourth]])
    return predicted

    
