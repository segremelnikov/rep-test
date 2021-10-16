from django.shortcuts import render, redirect 
from .models import Item
from main.models import UserData
from django.contrib.auth.models import User


def index(request):
    
    user = request.user
    items = user.item_set.all()
    udt = UserData.objects.get_or_create(user=user)[0]

    if request.method == "POST":
        dct = {}
        for key in request.POST:
            spl = key.split("-")
            if len(spl) == 2:
                if (spl[0] in dct):

                    dct[spl[0]][spl[1]] = request.POST[key]
                    nm = dct[spl[0]]["name"] if "name" in dct[spl[0]] else ""
                    cl = dct[spl[0]]["color"] if "color" in dct[spl[0]] else ""

                    if nm.strip() != "" and cl.strip() != "":
                        itm = user.item_set.create(name=nm, color=cl)
                        dct["id"+str(itm.id)]=True
                else:
                    dct[spl[0]] = {spl[1] : request.POST[key]}

            if len(spl) == 3:
                id = spl[2]
                if (id in dct):

                    dct[id][spl[1]] = request.POST[key]
                    nm = dct[id]["name"] if "name" in dct[id] else ""
                    cl = dct[id]["color"] if "color" in dct[id] else ""

                    if nm.strip() != "" and cl.strip() != "":
                        item = Item.objects.get(id=int(id[2:]))
                        item.name = nm
                        item.color = cl
                        item.save()
                else:
                    dct[id] = {spl[1] : request.POST[key]}

                    
        for item in items:
            if not ("id"+str(item.id)) in dct:
                item.delete()
        items = user.item_set.all()
        if len(items) >= 12:
            udt.has_added_people = True
            udt.save()
            return redirect('/estpeople/')
        else:
            udt.has_added_people = False
            udt.save()


    items = sorted(user.item_set.all(), key=lambda item : item.id)
    added = udt.has_added_people
    estimated = udt.has_estimeted_people


    context = {'user' : user, 'items': items, 'n': range(24), 'itemscnt' : len(items), 'not_added' : not added, 'not_estimated' : not estimated, 'pth': 'add' }
    return render(request, 'addpeople/index.html', context)



def show_people(request, user_id):

    user = request.user

    if request.method == "POST":
        return redirect("/")

    user1 = User.objects.get(id=user_id)
    items = sorted(user1.item_set.all(), key=lambda item : item.id)

    context = {'user' : user, 'items': items, 'n': range(24), 'itemscnt' : len(items) }
    return render(request, 'addpeople/index.html', context)

