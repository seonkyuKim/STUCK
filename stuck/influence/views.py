from django.shortcuts import render, redirect
from influence.models import UserDatabase, AuthUser, Influence
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.



@login_required
def index(request):
    context = {}
    if request.method == 'GET':
        is_first = False
        uu = ''

        try:
            username = str(request.user)
            uu = username
            user = UserDatabase.objects.get(username=username)
            

            followers = user.followers
            influence_points = user.influence_points
            print('b')

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
            us = AuthUser.objects.get(username=uu)
            UserDatabase(username=us, followers=1, influence_points=1, flag=1).save()

        context['is_first'] = is_first

    return render(request, 'index_influence.html', context)




@login_required
def update_info(request):

    if request.method == 'POST':
        username = request.user.username
        parameters = {"source": "twitter", "username": username}
        response = requests.get("https://kred-exp-v2.p.rapidapi.com/kred/score/twitter/" + username,
                                headers={
                                    "X-RapidAPI-Host": "kred-exp-v2.p.rapidapi.com",
                                    "X-RapidAPI-Key": "1c9e6a311fmsha6886b0dd447173p13096bjsnfd5b64c58107"
                                },
                                params=parameters
                                )

        parameter1 = {"screen_name": username}
        response1 = requests.get("https://peerreach.p.rapidapi.com/user/lookup.json?screen_name=" + username,
                                 headers={
                                     "X-RapidAPI-Host": "peerreach.p.rapidapi.com",
                                     "X-RapidAPI-Key": "93f9fbcb4cmsh077ae042f813545p198404jsn63ed6dfe8961"
                                 },
                                 params=parameter1
                                 )
        if response and response1:
            print("Response has succeeded")
            data = response.json()
            data1 = response1.json()

            print(data)
            print(data1)

            followers = data["followers"]
            influence_points = data["influence_points"]

            auth_user = AuthUser.objects.get(username=username)

            user = UserDatabase.objects.get(username=auth_user)
            user.followers = followers
            user.influence_points = influence_points


            user.save()

            categories = data1['peergroups']
            for category in categories:
                try:
                    in_obj = Influence.objects.filter(username=auth_user, name=category['topic'])[0]
                    in_obj.points=category['score']
                    in_obj.save()

                except:
                    Influence(username=auth_user, name=category['topic'], points=category['score']).save()

                

        else:
            print("Response failed")
    else:
        print("request metod did not enter post")

    return redirect('influence:index')
