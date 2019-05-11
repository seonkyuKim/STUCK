from django.shortcuts import render
from django.http import HttpResponse
from ecommerce.models import UserDatabase, Influence


# Create your views here.

def index(request):

    category_set = get_influences()
    total_category_list = list(category_set)

    category_list = ['Seoul', 'Junction']
    user_list = []

    for category in category_list:

        categories = Influence.objects.select_related('username').filter(name=category)    

        for category in categories:
            user_dict = {}
            user = UserDatabase.objects.get(username=category.username)
            user_dict['username'] = user.username
            user_dict['followers'] = user.followers
            user_dict['influence_points'] = user.influence_points
            user_dict['category'] = category.name
            user_dict['points'] = category.points

            user_list.append(user_dict)

    

    context = { 'users': user_list }

    # for user in users:
    #     print(user)

    # users = UserDatabase.objects.filter(flag=True).order_by('followers')
    # user_list = []

    # for user in users:
    #     user_dict = {}
    #     username = user.username
    #     followers = user.followers
    #     influence_points = user.influence_points

    #     user_dict["username"] = username
    #     user_dict["followers"] = followers
    #     user_dict["influence_points"] = influence_points

    #     influences = Influence.objects.filter(username=username).order_by('points')
    #     # influences = Influence.objects.all()
    #     influence_dict = {}
        
    #     for influence in influences:
    #         influence_dict[influence.name] = influence.points
            
    #     user_dict["influence"] = influence_dict

    #     user_list.append(user_dict)

    # context = { "users": user_list}
    


    return render(request, 'ecommerce.html', context)


def get_influences():
    influences = set()
    influence_list = Influence.objects.values('name')
    
    for row in influence_list:
        influences.add(row['name'])

    return influences