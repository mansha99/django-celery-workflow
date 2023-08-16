from celery import Celery
import time
import requests
from celery import group,chord
app = Celery('celery_tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')

@app.task(bind=True)#first argument self refers to Celery "app"
def sayHello(self,name):
    print('Hello '+name);

@app.task(bind=True)
def calculateFactorial(self,n):
    f=1
    for i in range(1,n+1):
        time.sleep(1)
        f = f * i
    return f;    

@app.task(bind=True)
def add(self,n1,n2):
    return n1+n2

@app.task(bind=True)
def square(self,n):
    return n*n


@app.task(bind=True)
def getDataFromRepository(self,username):
    u='https://api.github.com/users/'+username
    r = requests.get(u)
    data = r.json()#.items()
    return {'login':data['login'],'name':data['name'],'followers':data['followers']}
@app.task(bind=True)
def mergeRepoData(self):
    callback = processResult.s()
    header= group([
             getDataFromRepository.s('twitter'),
             getDataFromRepository.s('amazon')
    ])
    c= chord(header)(callback)
    return c()   
   
@app.task(bind=True)
def processResult(self,results):
    results.sort(key=lambda x: x['followers'], reverse=True)
    message ='Winner is '+results[0][u'login']+' with '+str(results[0][u'followers'])+' Followers';
    emails=['user1@gmail.com','user2@rediff.com','user3@yahoo.com'];
    #g = group(sendEmail.s(phone, smstask.text) for phone in phones)
    calls=[]
    for email in emails:
        calls.append(sendEmail.s(email,message))
    g = group(calls)
    g()
@app.task(bind=True)
def sendEmail(self,to,message):
    time.sleep(1)#just for testing
    print('To: '+to)
    print('Message: '+message)
    print('----------------Done-------------------------')
