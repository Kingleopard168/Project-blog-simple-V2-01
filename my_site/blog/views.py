from xml.dom.minidom import Identified
from django.shortcuts import render

from datetime import date

all_posts = [
    {
         "slug":"the-Mountains",
         "image":"mountains.png",
         "author":"MAXIMILIAN",
         "date": date(2021,7,21),
         "title":"Mountain Hiking",
         "excerpt":"There's nothing like the views you get when hiking in the Mountain And I wasn't even prepared for  what happened whilst I was enjoying the view",
         "content":""" 
         Lorem ipusm dolor amet consectetor adipisicing elit.Officiis nobis
            aperiam est prasentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero cula ad mollitia? quis architecto ipsam nemo. Odio.

            Lorem ipusm dolor amet consectetor adipisicing elit.Officiis nobis
            aperiam est prasentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero cula ad mollitia? quis architecto ipsam nemo. Odio.

            Lorem ipusm dolor amet consectetor adipisicing elit.Officiis nobis
            aperiam est prasentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero cula ad mollitia? quis architecto ipsam nemo. Odio.

         """
    },
    {
         "slug":"woods",
         "image":"woods.jpg",
         "author":"MAXIMILIAN",
         "date": date(2021,7,21),
         "title":"woods",
         "excerpt":"There's nothing like the views you get when hiking in the Mountain And I wasn't even prepared for  what happened whilst I was enjoying the view",
         "content":""" 
         Lorem ipusm dolor amet consectetor adipisicing elit.Officiis nobis
            aperiam est prasentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero cula ad mollitia? quis architecto ipsam nemo. Odio.

            Lorem ipusm dolor amet consectetor adipisicing elit.Officiis nobis
            aperiam est prasentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero cula ad mollitia? quis architecto ipsam nemo. Odio.

            Lorem ipusm dolor amet consectetor adipisicing elit.Officiis nobis
            aperiam est prasentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero cula ad mollitia? quis architecto ipsam nemo. Odio.

         """
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts= sorted(all_posts,key=get_date)
    latest_posts= sorted_posts[-3:]
    return render(request, "blog/index.html",{
        "posts":latest_posts
    }
    
    )

def posts(request):
    return render(request, "blog/all-posts.html" , {
        "all_posts": all_posts
    })
    
    

def post_datail(request, slug):
    Identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post":Identified_post
    })