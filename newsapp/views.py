from django.shortcuts import render
from newsapi import NewsApiClient
  
# Create your views here. 
def index(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(country ='in')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def usa(request):
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(country ='us')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def business(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='business')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def entertainment(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='entertainment')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def general(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='general')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def health(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='health')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def science(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='science')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def sports(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='sports')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def technology(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='technology')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def search(request):
      

    searchObj = request.POST
    q = searchObj.get('search')
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_everything(q=q)
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})