from django.shortcuts import render
from influence.models import UserDatabase

# Create your views here.


def index(request):
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
                                },
                                params=parameters
                                )

#new
        parameter1 = {"screen_name": requests.user.username}
        response1 = requests.get("https://peerreach.p.rapidapi.com/user/lookup.json?screen_name=fredwilson",
                                 headers={
                                     "X-RapidAPI-Host": "peerreach.p.rapidapi.com",
                                     "X-RapidAPI-Key": "93f9fbcb4cmsh077ae042f813545p198404jsn63ed6dfe8961"
                                 },
                                 params=parameter1
                                 )

 #newend
        if response and response1:
            print("Response has succeeded")
            data = response.json()


#new
            
            user.followers = data["followers"]
            user.influence_points = data["influence_points"]
            user.save(update_fields=['followers', 'influence_points'])
        else:
            print("Response failed")
    else:
        print("request metod did not enter post")

    temp = {'user': user}
    data.update(temp)

    return render(request, 'index_influencer.html', data)
