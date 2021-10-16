from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse
from addpeople.models import Item
from main.models import UserData
from .models import Page, Estimation
from django.contrib.auth.models import User
import random 


def check_pages_dupl(page1_first, page1_second, page1_third, page1_two_like, page1_third_chosen, page2_first, page2_second, page2_third, page2_two_like):


    if not page1_first or not page2_first:
        return True


    if page1_third:

        if page2_third:
            sorted1 = sorted([page1_first, page1_second, page1_third])
            sorted2 = sorted([page2_first, page2_second, page2_third])
            return sorted1 != sorted2

        elif page1_third_chosen is not None:
            if page1_third_chosen == 0:
                sorted1 = sorted([page1_second, page1_third])
                other1 = page1_first
            elif page1_third_chosen == 1:
                sorted1 = sorted([page1_first, page1_third])
                other1 = page1_second
            else:
                sorted1 = sorted([page1_first, page1_second])
                other1 = page1_third

            sorted2 = sorted([page2_first, page2_second])

            if page2_two_like:
                return sorted1 != sorted2
            else:
                return other1 not in sorted2 or (page2_first not in sorted1 and page2_second not in sorted1)


        
    else:

        if not page2_third and page1_two_like == page2_two_like:
            sorted1 = sorted([page1_first, page1_second])
            sorted2 = sorted([page2_first, page2_second])
            return sorted1 != sorted2
            

    return True




def create_page(user, items, step):

    if step <= 10:

        pages = user.page_set.all()
        items = list(items)
        variants = []

        for i in range(3):

            cnt = 3
            if random.random() > 0.7:
                cnt = 2
            
            bad = True
            
            while bad:

                bad = False

                random_items = random.sample(items, cnt)
                two_like = False
                if cnt == 2 and random.random() > 0.6:
                    two_like = True
                first = random_items[0] 
                second = random_items[1] 
                third = None 
                if cnt == 3:
                    third = random_items[2] 
                thirdname = third.name if third else None

                for page in pages:

                    bad = not check_pages_dupl(page.first1, page.second1, page.third1, page.two_like1, page.third_chosen1, first.name, second.name, thirdname, two_like)
                    if bad:
                        break
                    bad = not check_pages_dupl(page.first2, page.second2, page.third2, page.two_like2, page.third_chosen2, first.name, second.name, thirdname, two_like)
                    if bad:
                        break
                    bad = not check_pages_dupl(page.first3, page.second3, page.third3, page.two_like3, page.third_chosen3, first.name, second.name, thirdname, two_like)
                    if bad:
                        break

                if not bad and i > 0:
                    bad = not check_pages_dupl(variants[0][0].name, variants[0][1].name, variants[0][2].name if variants[0][2] else None, variants[0][3], None, first.name, second.name, thirdname, two_like)

                if not bad and i == 2:
                    bad = not check_pages_dupl(variants[1][0].name, variants[1][1].name, variants[1][2].name if variants[1][2] else None, variants[1][3], None, first.name, second.name, thirdname, two_like)

            variants.append([first, second, third, two_like])

        user.page_set.create(number=step, first_item1=variants[0][0], second_item1=variants[0][1], third_item1=variants[0][2], two_like1=variants[0][3], first_item2=variants[1][0], second_item2=variants[1][1], third_item2=variants[1][2], two_like2=variants[1][3], first_item3=variants[2][0], second_item3=variants[2][1], third_item3=variants[2][2], two_like3=variants[2][3])
    else:
        user.page_set.create(number=step)
        


def index(request):
    user = request.user
    data = UserData.objects.get_or_create(user=request.user)[0]
    
    if not data.has_added_people:
        return redirect('/addpeople/')

    cur_step = data.current_estimate_step
    pages = user.page_set.all()

    if len(pages) == 0:
        user.page_set.create(number=0) 
    return redirect('/estpeople/' + str(cur_step))


def render_step(request, cur_step):
    
    user = request.user
    
    data = UserData.objects.get_or_create(user=request.user)[0]
    
    if not data.has_added_people:
        return redirect('/addpeople/')

    
    items = user.item_set.all()

    page = Page.objects.filter(user=user, number=cur_step).first()
    


    if request.method == "POST":  
        if "btnAllReady" in request.POST and request.POST["notSaved"] == "true":
            page.is_saved = False
            page.save()
            data.current_estimate_step = cur_step if cur_step == 12 else cur_step + 1
            data.has_estimeted_people = True
            data.save()
            return redirect('/results/')

        page.is_saved = True
        page.save()
        if cur_step > 0:
            page.prop_name = request.POST["propName"]
            page.save()
            for key in request.POST:
                spl = key.split("-")
                if len(spl) == 2 and spl[0] == "est":
                    cur_item = items.get(id=int(spl[1]))
                    cur_est = Estimation.objects.get(item=cur_item, number=cur_step)
                    cur_est.value = int(request.POST[key])
                    cur_est.save()
        if "btnAllReady" in request.POST:
            data.current_estimate_step = cur_step if cur_step == 12 else cur_step + 1
            data.has_estimeted_people = True
            data.save()
            return redirect('/results/')

    
    pages = list(sorted(user.page_set.all(), key=lambda p : p.number))

    if len(pages) == 0:
        user.page_set.create(number=0) 
     

    pages_bool = [False for i in range(13)]
    pages_names = ['' for i in range(13)]
    lastOpenedStep = len(pages) - 1
    first_non_est_step = lastOpenedStep + 1 

    for i in range(13):

        if i == len(pages):
            break

        p = pages[i]
        isEst = p.is_saved
        if isEst and i > 0:
            for itm in items:
                est = Estimation.objects.filter(item=itm, number=i).first()
                if not est or est.value == -1000:
                    isEst = False
                    break
        if not isEst and first_non_est_step == lastOpenedStep + 1:
            first_non_est_step = i
        pages_bool[i] = isEst
        pages_names[i] = p.prop_name

    pages_names[0] = "инструкция"

    if request.method == "POST":
        return redirect('/estpeople/' + str(first_non_est_step if first_non_est_step <= 12 else cur_step))
     
    if cur_step < 0 or (cur_step > lastOpenedStep and (cur_step != first_non_est_step or cur_step > 12)):
        return redirect('/estpeople/' + str(min(first_non_est_step, 12)))
    
    if not page:
        create_page(user, items, cur_step)
        page = Page.objects.filter(user=user, number=cur_step).first()
        pages_bool.append(False)
        lastOpenedStep += 1

    if page.first_item1:
        page.first1 = page.first_item1.name 
    if page.first_item2:
        page.first2 = page.first_item2.name 
    if page.first_item3:
        page.first3 = page.first_item3.name 
    if page.second_item1:
        page.second1 = page.second_item1.name 
    if page.second_item2:
        page.second2 = page.second_item2.name 
    if page.second_item3:
        page.second3 = page.second_item3.name 
    if page.third_item1:
        page.third1 = page.third_item1.name 
    if page.third_item2:
        page.third2 = page.third_item2.name 
    if page.third_item3:
        page.third3 = page.third_item3.name 
    page.save()

    data.current_estimate_step = cur_step
    data.save()
 
    cnt_bad = 0
    bad_index = 0
    for i in range(11):
        if not pages_bool[i]:
            cnt_bad += 1
            bad_index = i
            if cnt_bad == 2:
                break
    
    show_end_btn = cnt_bad == 0 or (cnt_bad == 1 and bad_index == cur_step)
     

    estims = [Estimation.objects.get_or_create(item=itm, number=cur_step)[0] for itm in items] if cur_step > 0 else []

    
    estimated = UserData.objects.get_or_create(user = user)[0].has_estimeted_people

    context = {'user': user, 'lastOpenedStep': lastOpenedStep, 'firstNonEstStep' : first_non_est_step, 'cur_step': cur_step, 'n': range(13),
               'data': data, 'estims': estims, 'page': page, 'pages': pages_bool, 'pagesNames': pages_names, 'showEndBtn': show_end_btn, 'not_estimated': not estimated, 'pth': 'est' + str(cur_step)}
    return render(request, "estpeople/index.html", context)


def savesettings(request): 

    if request.method == "GET":
        raise Http404("URL doesn't exists")
    
    user = request.user

    data = UserData.objects.get(user=request.user)
    data.background_image_index = request.POST["imageindex"]
    data.background_color = request.POST["color"]
    data.backgruond_opacity = request.POST["opacity"]
    data.fontcolor = request.POST["fontcolor"] 
    data.tickline_color = request.POST["ticklineColor"] 
    data.imptickline_color = request.POST["impticklineColor"] 
    data.tickline_lbl_color = request.POST["ticklineLblColor"] 
    data.imptickline_lbl_color = request.POST["impticklineLblColor"] 
    data.speed = request.POST["speed"] 

    data.save()
    return HttpResponse(status=204)


def saveitem(request): 

    if request.method == "GET":
        raise Http404("URL doesn't exists")
   
    user = request.user
    item = Item.objects.get(user=user, id=request.POST["itemId"])
    est = item.estimation_set.filter(number=request.POST["step"]).first()
     
    if not est:
        Estimation.objects.create(item=item,number=request.POST["step"], x=request.POST["xp"], y=request.POST["yp"], value=request.POST["val"])
    else:
        est.x = request.POST["xp"]
        est.y = request.POST["yp"]
        est.value = request.POST["val"]
        est.save()

    page = Page.objects.get(user=user, number=request.POST["step"])
    page.cur_item = item
    page.save()

    return HttpResponse(status=204)


def savequestion(request):

    if request.method == "GET":
        raise Http404("URL doesn't exists")

    
    user = request.user
    page = Page.objects.get(user=user, number=request.POST["step"])
    page.index = request.POST["index"]
    page.third_chosen1 = request.POST["thirdChosen1"]
    page.third_chosen2 = request.POST["thirdChosen2"]
    page.third_chosen3 = request.POST["thirdChosen3"]   
    page.prop1 = request.POST["prop1"]
    page.prop2 = request.POST["prop2"]
    page.prop3 = request.POST["prop3"] 
    page.prop_name = request.POST["propName"]
    page.save() 

    return HttpResponse(status=204)



def show_people(request, user_id, cur_step):

    user = User.objects.get(id=user_id)
    
    data = UserData.objects.get(user=user)
    
    items = user.item_set.all()

    page = Page.objects.filter(user=user, number=cur_step).first()
    
    pages = list(sorted(user.page_set.all(), key=lambda p : p.number))

    pages_bool = [False for i in range(13)]
    pages_names = ['' for i in range(13)]
    lastOpenedStep = len(pages) - 1
    first_non_est_step = lastOpenedStep + 1 

    for i in range(13):

        if i == len(pages):
            break

        p = pages[i]
        isEst = p.is_saved
        if isEst and i > 0:
            for itm in items:
                est = Estimation.objects.filter(item=itm, number=i).first()
                if not est or est.value == -1000:
                    isEst = False
                    break
        if not isEst and first_non_est_step == lastOpenedStep + 1:
            first_non_est_step = i
        pages_bool[i] = isEst
        pages_names[i] = p.prop_name

    pages_names[0] = "инструкция"

 

    estims = [Estimation.objects.get(item=itm, number=cur_step) for itm in items] if cur_step > 0 else []

    context = {'user': user, 'lastOpenedStep': lastOpenedStep, 'firstNonEstStep' : first_non_est_step, 'cur_step': cur_step, 'n': range(13),
               'data': data, 'estims': estims, 'page': page, 'pages': pages_bool, 'pagesNames': pages_names, 'pth': 'est' + str(cur_step)  }
    return render(request, "estpeople/index.html", context)


