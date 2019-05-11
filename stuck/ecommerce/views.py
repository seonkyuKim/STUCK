from django.shortcuts import render
from django.http import HttpResponse
from ecommerce.models import UserDatabase, Influence, AuthUser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

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


@csrf_exempt
def see_influencer(request):
    context = {}
    if request.method == 'POST':
        
        username = request.POST
        print(request.POST)
        
        # username = request.POST['data']
        # username = str('realdonaldtrump')
        
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

    
    return render(request, 'index_influence.html', context)


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
        