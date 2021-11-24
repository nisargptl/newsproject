from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient
  
# Create your views here. 
def index(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(page_size=100)
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def usa(request):
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(country ='us',page_size=100)
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def india(request):
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(country ='in',page_size=100)
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'index.html', context ={"mylist":mylist})


def business(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='business',page_size=100)
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def entertainment(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='entertainment',page_size=100)
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def general(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='general',page_size=100)
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def health(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='health',page_size=100)
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def science(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='science',page_size=100)
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def sports(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='sports',page_size=100)
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def technology(request):
      
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_top_headlines(category ='technology',page_size=100)
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'index.html', context ={"mylist":mylist})

def search(request, name):
      

    searchObj = request.POST
    q = searchObj.get('search')
    print(name,q)
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_everything(q=q+ " AND " +name,page_size=100)
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'search.html', context ={"mylist":mylist})

def search_index(request):
      

    searchObj = request.POST
    q = searchObj.get('search')
    newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
    top = newsapi.get_everything(q=q,page_size=100)
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
  
    return render(request, 'search.html', context ={"mylist":mylist})

# def search_india(request):
      

#     searchObj = request.POST
#     q = searchObj.get('search')
#     newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
#     top = newsapi.get_everything(q = q+" AND india",page_size=100)
#     l = top['articles']
#     desc =[]
#     news =[]
#     img =[]
#     url = []
  
#     for i in range(len(l)):
#         f = l[i]
#         news.append(f['title'])
#         desc.append(f['description'])
#         img.append(f['urlToImage'])
#         url.append(f['url'])
#     mylist = zip(news, desc, img, url)
  
#     return render(request, 'index.html', context ={"mylist":mylist})

# def search_usa(request):
      

#     searchObj = request.POST
#     q = searchObj.get('search')
#     newsapi = NewsApiClient(api_key ='eaacdd1e29b6408bbdda371f9bebe91f')
#     top = newsapi.get_everything(q = q +" AND (usa OR america OR united states of america)",page_size=100)
#     l = top['articles']
#     desc =[]
#     news =[]
#     img =[]
#     url = []
  
#     for i in range(len(l)):
#         f = l[i]
#         news.append(f['title'])
#         desc.append(f['description'])
#         img.append(f['urlToImage'])
#         url.append(f['url'])
#     mylist = zip(news, desc, img, url)
  
#     return render(request, 'index.html', context ={"mylist":mylist})