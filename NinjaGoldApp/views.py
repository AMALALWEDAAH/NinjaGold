from django.shortcuts import render, HttpResponse , redirect

import random
from time import gmtime, strftime
def index(request):
    if not 'ygold' in request.session:
        request.session['ygold']=0
    return render(request,"index.html")



def process(request):
    transactions=[]
    if request.method == 'POST':
        if request.POST['gold'] == '4487':
            trans =random.randint(-50,50)
            request.session['ygold']+=trans 
            if trans < 0 :
                transactions.append(f" You failed a quest and lost {trans} gold.({strftime('%Y-%m-%d %H:%M %p', gmtime())})")
            else:
                transactions.append(f" You entered a quest and earned {trans} gold.({strftime('%Y-%m-%d %H:%M %p', gmtime())})")
        elif request.POST['gold'] == '1487':
            trans =random.randint(10,20)
            request.session['ygold']+=trans
            transactions.append(f" You entered a farm and earned {trans} gold.({strftime('%Y-%m-%d %H:%M %p', gmtime())})")

        elif request.POST['gold'] == '3487':
            trans =random.randint(10,20)
            request.session['ygold']+=trans
            transactions.append(f" You entered a house and earned {trans} gold.({strftime('%Y-%m-%d %H:%M %p', gmtime())})")

        else:
            trans =random.randint(10,20)
            request.session['ygold']+=trans
            transactions.append(f" You entered a cave and earned {trans} gold.({strftime('%Y-%m-%d %H:%M %p', gmtime())})")
        if 'transactions' not in request.session:
            request.session['transactions']=[]
        else:
            request.session['transactions']+=transactions
    return render(request,'index.html')

def reset(request):
    request.session.clear()
    return redirect('/')
