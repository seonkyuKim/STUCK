from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecommerce.models import UserDatabase, Influence, AuthUser
from django.views.decorators.csrf import csrf_exempt
import requests

got_user = "whatever"

# Create your views here.
def get_user(request):
    context = {}
    if request.method == 'POST':
        user_name = request.POST['username']
        global got_user
        got_user = user_name
        user = UserDatabase.objects.get(username=user_name)

        followers = user.followers
        influence_points = user.influence_points

        auth_user = AuthUser.objects.get(username=user_name)
        first_name = auth_user.first_name
        last_name = auth_user.last_name

        categories = Influence.objects.filter(username=auth_user)
        category_list = []
        print(categories)
        for category in categories:
            category_list.append(category.name)

        context['username'] = user_name
        context['first_name'] = first_name
        context['last_name'] = last_name
        context['followers'] = followers
        context['influence_points'] = influence_points
        context['categories'] = category_list

    print(got_user)
    return render(request, 'index_influence-2.html', context)

def index(request):

    category_set = get_influences()
    total_category_list = list(category_set)

    user_list = []
    categories = Influence.objects.select_related('username').all()

    for category in categories:
        user_dict = {}
        user = UserDatabase.objects.get(username=category.username)
        user_dict['username'] = user.username
        user_dict['followers'] = user.followers
        user_dict['influence_points'] = user.influence_points
        user_dict['category'] = category.name
        user_dict['points'] = category.points

        user_list.append(user_dict)



    context = { 'users': user_list, 'total_category_list': total_category_list }

    return render(request, 'ecommerce.html', context)



def see_influencer(request):
    context = {}


    global got_user
    username = got_user

    # user = AuthUser.objects.get(username=username)

    try:
        user = UserDatabase.objects.get(username=username)

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

    return render(request, 'index_influence-2.html', context)


def get_influences():
    influences = set()
    influence_list = Influence.objects.values('name')

    for row in influence_list:
        influences.add(row['name'])

    return influences


# def get_user(request):
#     if request.method == 'POST':

#         username = request.POST['username']
#         print(username)




def email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        content = request.POST['content']
        from_email = request.user.email
        global got_user
        user_name = got_user
        print(user_name)
        print("AaAaAAASFSFNAKSFBASKFB")
        profile_user = AuthUser.objects.filter(username=user_name)[0]
        to_email = profile_user.email


        parameters = {"to_email":to_email,"subject":subject, "from_email":from_email, "content": content }

        response = requests.post("https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send",
                             headers={
                                 "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com",                           
                                 "X-RapidAPI-Key": "93f9fbcb4cmsh077ae042f813545p198404jsn63ed6dfe8961",
                                 "Content-Type": "application/json"
                             },
                             data=(
                                 "{\"personalizations\":[{\"to\":[{\"email\":\"" + parameters["to_email"] + "\"}],\"subject\":\"" + parameters["subject"] + "\"}],\"from\":{\"email\":\"" + parameters["from_email"] + "\"},\"content\":[{\"type\":\"text/plain\",\"value\":\"" + parameters["content"] + "\"}]}")
                             )
        if response:
            print("Response has suceeded")


    else: print("request metod did not enter post")

    #TO DO: SELECT THE RETURN VALUE FOR THE FUNCTION
    return redirect('ecommerce:see')