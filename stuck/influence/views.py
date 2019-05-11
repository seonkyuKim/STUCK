from django.shortcuts import render, redirect
from influence.models import UserDatabase, AuthUser, Influence
from django.contrib.auth.decorators import login_required

import requests

# Create your views here.

@login_required
def index(request):
<<<<<<< HEAD
    return render(request, 'index_influence.html')


def update_info(request):
    user = UserDatabase.objects().get(username=request.user.username)
    data = None
    if request.method == 'POST':
        parameters = {"source": twitter, "username": requests.user.username}
        response = requests.get("https://kred-exp-v2.p.rapidapi.com/kred/score/twitter/neilhimself",
                                headers={
                                    "X-RapidAPI-Host": "kred-exp-v2.p.rapidapi.com",
                                    "X-RapidAPI-Key": "93f9fbcb4cmsh077ae042f813545p198404jsn63ed6dfe8961"
=======
    context = {}
    if request.method == 'GET':
        is_first = False
        
        try:
            
            user = UserDatabase.objects.get(username=request.user.username)
            username = user.username
            followers = user.followers
            influence_points = user.influence_points

            auth_user = AuthUser.objects.get(username=username)
            first_name = auth_user.first_name
            last_name = auth_user.last_name

            categories = Influence.objects.filter(username=auth_user)
            category_list = []
            print(categories)
            for category in categories:
                category_list.append(category.name)
                

            context['username'] = username
            context['first_name'] = first_name
            context['last_name'] = last_name
            context['followers'] = followers
            context['influence_points'] = influence_points
            context['categories'] = category_list

        except:
            print('except')
            is_first = True

        context['is_first'] = is_first
    
    return render(request, 'index_influence.html', context)

@login_required
def update_info(request):
    
    if request.method == 'POST':
        username = request.user.username
        parameters = {"source": "twitter", "username": username}
        response = requests.get("https://kred-exp-v2.p.rapidapi.com/kred/score/twitter/"+username,
                                headers={
                                    "X-RapidAPI-Host": "kred-exp-v2.p.rapidapi.com",
                                    "X-RapidAPI-Key": "1c9e6a311fmsha6886b0dd447173p13096bjsnfd5b64c58107"
>>>>>>> ab9c39eac2f3edc2093526603274bd25066c9add
                                },
                                params=parameters
                                )

<<<<<<< HEAD
#new
        parameter1 = {"screen_name": requests.user.username}
        response1 = requests.get("https://peerreach.p.rapidapi.com/user/lookup.json?screen_name=fredwilson",
=======
        parameter1 = {"screen_name": username}
        response1 = requests.get("https://peerreach.p.rapidapi.com/user/lookup.json?screen_name="+username,
>>>>>>> ab9c39eac2f3edc2093526603274bd25066c9add
                                 headers={
                                     "X-RapidAPI-Host": "peerreach.p.rapidapi.com",
                                     "X-RapidAPI-Key": "93f9fbcb4cmsh077ae042f813545p198404jsn63ed6dfe8961"
                                 },
                                 params=parameter1
                                 )
<<<<<<< HEAD

 #newend
        if response and response1:
            print("Response has succeeded")
            data = response.json()


#new
            
            user.followers = data["followers"]
            user.influence_points = data["influence_points"]
            user.save(update_fields=['followers', 'influence_points'])
=======
        if response and response1:
            print("Response has succeeded")
            data = response.json()
            data1 = response1.json()

            print(data)
            print(data1)

            followers = data["followers"]
            influence_points = data["influence_points"]

            auth_user = AuthUser.objects.get(username=username)
            user = UserDatabase(username=auth_user, followers=followers, influence_points=influence_points, flag=1)
            user.save()
            
            categories = data1['peergroups']
            for category in categories:
                in_obj = Influence(username=auth_user, name=category['topic'], points=category['score'])
                in_obj.save()
            
>>>>>>> ab9c39eac2f3edc2093526603274bd25066c9add
        else:
            print("Response failed")
    else:
        print("request metod did not enter post")

<<<<<<< HEAD
    temp = {'user': user}
    data.update(temp)

    return render(request, 'index_influencer.html', data)
=======

    return redirect('influence:index')

    
>>>>>>> ab9c39eac2f3edc2093526603274bd25066c9add
