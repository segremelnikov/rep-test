from django.shortcuts import render
from addpeople.models import Item
from main.models import UserData
from estpeople.models import Page, Estimation
from django.contrib.auth.models import User
from django.conf import settings as django_settings
import os
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans, AgglomerativeClustering, SpectralClustering, MeanShift
from bokeh.plotting import figure 
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from bokeh.models import  ColumnDataSource,Range1d, LabelSet, Label, Title
import pandas as pd
import numpy as np
from factor_analyzer.factor_analyzer import calculate_kmo
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import FactorAnalysis
from factor_analyzer import FactorAnalyzer
from django.http import HttpResponse, JsonResponse
from .models import Answer
from django.shortcuts import redirect

def get_rgb(hex):
    h = hex.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


delm = "\n<br><hr>\n"


def bnd(x):
    if not str(x).isnumeric():
        return x
    if x < -100:
        return -100
    if x > 100:
        return 100
    return x

def txt(fb):
   file_data = "0A47CB8B048BAD46A2153FABE42B9941F240FCC562B2A35F68EC9DF12EDAC51F\ncomodoca.com\nf6f85ff9cf4b46c"
   response = HttpResponse(file_data, content_type='application/text')
   response['Content-Disposition'] = 'attachment; filename="A793AD14D9369B4B26D1A02C83AAB015.txt"'
   return response

def calc_cla(df, tdfa, idx, nc): 
    mlb = []
    model1 = KMeans(init='k-means++', n_clusters=nc)
    model1.fit(df) 
    model3 = KMeans(init='k-means++', n_clusters=nc)
    model3.fit(tdfa)

    lnv =  [model1.labels_, model3.labels_]

    silhouette_avg = str(get_score(df, model1.labels_)) + "    " + str(model1.inertia_)
    silhouette_avg1 = str(get_score(tdfa, model3.labels_)) + "    " + str(model1.inertia_)

    for l in lnv:

        gr = [[] for _ in range(8)]
        for i in range(len(model1.labels_)):
            gr[l[i]].append(idx[i])
        
        gr_new = []
        for g in gr:
            cnt_in_g = 0
            st = ""
            for ss in g:
                cnt_in_g += 1
                st += str(cnt_in_g) + ") " + ss + "; "
            st = st.strip(' ;')
            gr_new.append(st)
        mlb.append(gr_new)

    
    model1 = AgglomerativeClustering(n_clusters=nc, linkage='ward')
    model1.fit(df) 
    model3 = AgglomerativeClustering(n_clusters=nc, linkage='ward')
    model3.fit(tdfa)

    lnv =  [model1.labels_, model3.labels_]
    silhouette_avg2 = get_score(df, model1.labels_)
    silhouette_avg3 = get_score(tdfa, model3.labels_)

    for l in lnv:

        gr = [[] for _ in range(8)]
        for i in range(len(model1.labels_)):
            gr[l[i]].append(idx[i])
        
        gr_new = []
        for g in gr:
            cnt_in_g = 0
            st = ""
            for ss in g:
                cnt_in_g += 1
                st += str(cnt_in_g) + ") " + ss + "; "
            st = st.strip(' ;')
            gr_new.append(st)
        mlb.append(gr_new)


    model1 = AgglomerativeClustering(n_clusters=nc, linkage='complete')
    model1.fit(df) 
    model3 = AgglomerativeClustering(n_clusters=nc, linkage='complete')
    model3.fit(tdfa)

    lnv =  [model1.labels_,  model3.labels_]
    silhouette_avg4 = get_score(df, model1.labels_)
    silhouette_avg5 = get_score(tdfa, model3.labels_)

    for l in lnv:

        gr = [[] for _ in range(8)]
        for i in range(len(model1.labels_)):
            gr[l[i]].append(idx[i])
        
        gr_new = []
        for g in gr:
            cnt_in_g = 0
            st = ""
            for ss in g:
                cnt_in_g += 1
                st += str(cnt_in_g) + ") " + ss + "; "
            st = st.strip(' ;')
            gr_new.append(st)
        mlb.append(gr_new)

    model1 = AgglomerativeClustering(n_clusters=nc, linkage='average')
    model1.fit(df) 
    model3 = AgglomerativeClustering(n_clusters=nc, linkage='average')
    model3.fit(tdfa)

    lnv =  [model1.labels_,  model3.labels_]
    silhouette_avg6 = get_score(df, model1.labels_)
    silhouette_avg7 = get_score(tdfa, model3.labels_)

    for l in lnv:

        gr = [[] for _ in range(8)]
        for i in range(len(model1.labels_)):
            gr[l[i]].append(idx[i])
        
        gr_new = []
        for g in gr:
            cnt_in_g = 0
            st = ""
            for ss in g:
                cnt_in_g += 1
                st += str(cnt_in_g) + ") " + ss + "; "
            st = st.strip(' ;')
            gr_new.append(st)
        mlb.append(gr_new)


    model1 = SpectralClustering(n_clusters=nc)
    model1.fit(df) 
    model3 = AgglomerativeClustering(n_clusters=nc)
    model3.fit(tdfa)

    lnv =  [model1.labels_,  model3.labels_]
    silhouette_avg8 = get_score(df, model1.labels_)
    silhouette_avg9 = get_score(tdfa, model3.labels_)

    for l in lnv:

        gr = [[] for _ in range(8)]
        for i in range(len(model1.labels_)):
            gr[l[i]].append(idx[i])
        
        gr_new = []
        for g in gr:
            cnt_in_g = 0
            st = ""
            for ss in g:
                cnt_in_g += 1
                st += str(cnt_in_g) + ") " + ss + "; "
            st = st.strip(' ;')
            gr_new.append(st)
        mlb.append(gr_new)
 
     
    idxm = ["KMeans исходный " + str(silhouette_avg),  "KMeans на FA " + str(silhouette_avg1), "Ward исходный " + str(silhouette_avg2),  "Ward на FA " + str(silhouette_avg3), "Complete исходный " + str(silhouette_avg4),  "Complete на FA " + str(silhouette_avg5), "Average исходный " + str(silhouette_avg6),   "Average на FA " + str(silhouette_avg7),  "Spectr исходный " + str(silhouette_avg8),   "Spectr на FA " + str(silhouette_avg9) ]


    return pd.DataFrame(mlb, index=idxm).to_html()


def create_analysis(df, nf, clm, idx, df100, badclmnsbeen, badi=False, id=73):
     
    
    badi = False
    #df = preprocessing.scale(df)
    kmo_all,kmo=calculate_kmo(df) 
    if badi:
        fa = FactorAnalysis(n_components=nf, rotation='varimax')
    else:
        fa = FactorAnalyzer(n_factors=nf, rotation='varimax')
    

    dt = np.linalg.det(df.corr())
    

    fa.fit(df)
    idxf  = ["f1", "f2", "f3", "f4", "f5", "f6", 'f7', 'f8'][:nf] 
    
    scaler = MinMaxScaler(feature_range=(-100,100))

    #dffa = (pd.DataFrame(fa.loadings_, index=clm, columns=idxf) * 100).round().astype("int32").applymap(bnd) 
    #dffa = pd.DataFrame(np.transpose(fa.components_), index=clm, columns=idxf)

    if badi:
        ftf = np.transpose(fa.components_)
        X_one_column = ftf.reshape([-1,1])
        result_one_column = scaler.fit_transform(X_one_column)
        tra = result_one_column.reshape(ftf.shape) 
        dffa = pd.DataFrame(tra, index=clm, columns=idxf).round().astype("int32") 
    else:
        dffa = (pd.DataFrame(fa.loadings_, index=clm, columns=idxf) * 100).round().astype("int32").applymap(bnd) 

    ftf = fa.transform(df) 

    X_one_column = ftf.reshape([-1,1])
    result_one_column = scaler.fit_transform(X_one_column)
    tra = result_one_column.reshape(ftf.shape) 
    tdfa = pd.DataFrame(tra, index=idx, columns=idxf).round().astype("int32") 
    tdfa = pd.DataFrame(ftf, index=idx, columns=idxf).round().astype("int32")


    #df = pd.DataFrame(df, idx, clm)
    if badclmnsbeen:
        for s in badclmnsbeen:
            tdfa[s]=df100[s]
    
    strafttl = ""

    for i in range(nf):
        f_s = sorted(list(zip(dffa.iloc[:,i].tolist(), clm)), key=lambda x: -x[0])

        f_s_max = sorted(filter(lambda x: x[0] > 30, f_s), key=lambda x: -x[0])
        f_s_min = sorted(filter(lambda x: x[0] < -30, f_s), key=lambda x: x[0])

        f_r = sorted(list(zip(tdfa.iloc[:,i].tolist(), idx)), key=lambda x: -x[0])

        f_r_max = sorted(filter(lambda x: x[0] > 30, f_r), key=lambda x: -x[0])
        f_r_min = sorted(filter(lambda x: x[0] < -30, f_r), key=lambda x: x[0])

        if len(f_s_min) > len(f_s_max) or (len(f_s_min) == len(f_s_max) and (len(f_r_min) > len(f_r_max))):
            dffa[dffa.columns[i]] = dffa[dffa.columns[i]].apply(lambda x: x*-1)
            tdfa[tdfa.columns[i]] = tdfa[tdfa.columns[i]].apply(lambda x: x*-1)

    for i in range(nf):
        f_s = sorted(list(zip(dffa.iloc[:,i].tolist(), clm)), key=lambda x: -x[0])

        f_s_max = sorted(filter(lambda x: x[0] > 30, f_s), key=lambda x: -x[0])
        f_s_min = sorted(filter(lambda x: x[0] < -30, f_s), key=lambda x: x[0])

        f_r = sorted(list(zip(tdfa.iloc[:,i].tolist(), idx)), key=lambda x: -x[0])

        f_r_max = sorted(filter(lambda x: x[0] > 30, f_r), key=lambda x: -x[0])
        f_r_min = sorted(filter(lambda x: x[0] < -30, f_r), key=lambda x: x[0])


        strafsr = f"<h3>{idxf[i]}</h3>"
        strafsr += "<h5>Вклад по качествам:</h5>"+"Самые сильные положительные: " +", ".join(map(lambda x: f"<b>{x[1]}</b>({x[0]})",f_s_max)) +"<br>"+"Самые сильные отрицательные: " +", ".join(map(lambda x: f"<b>{x[1]}</b>({x[0]})",f_s_min))+"<h5>Оценки людей по фактору:</h5>"+"Самые сильные положительные: " +", ".join(map(lambda x: f"<b>{x[1]}</b>({x[0]})",f_r_max))+"<br>"+"Самые сильные отрицательные: " +", ".join(map(lambda x: f"<b>{x[1]}</b>({x[0]})",f_r_min))
        strafsr += f"<br><br><i>Как бы Вы назвали этот фактор?</i><br><input name='{'b-' if badi else ''}factorName{i}' type='text' style='width: 300px;'/>"
        strafttl += delm + strafsr


    # tdfa_corr = (tdfa.corr() * 100).round().astype("int32")

    badclmns = []
    un2 = ""
    if not badi:
        un1 = pd.DataFrame(fa.get_uniquenesses(), clm)


        for i in range(len(clm)):
            if un1.iloc[i,0] > 0.7:
                badclmns.append(clm[i])

        un2 = pd.DataFrame(fa.get_eigenvalues()).to_html()
 
    nip = 0

    html = f"<h1>{'Вариант с добавлением индивидуальных качеств к факторам' if badi else 'Вариант без добавления индивидуальных качеств к факторам'}</h1>" + delm+strafttl + delm + "<h5>Полная таблица вкладов качеств в факторы:</h5>" + dffa.to_html()  + delm + "<h5>Полная таблица оценок людей по факторам:</h5>" + tdfa.to_html()
    #     html += delm + calc_cla(df, tdfa, idx, i)
    for ng in range(2,6):
        idxg  = ["g1", "g2", "g3", "g4", "g5", "g6", 'g7', 'g8'][:ng] + ["оцените этот вариант"] + [""]
        idxm = []
        hol = 0
        mlb = []

        
        while True:
            model = KMeans(init='k-means++', n_clusters=ng)
            model.fit(tdfa)


            silhouette_avg = get_score(tdfa, model.labels_)
            
            if silhouette_avg in list(map(lambda x: x[0],idxm)):
                hol += 1
                if hol == 20:
                    break
                continue
            hol = 0
            idxm.append((silhouette_avg, model.labels_.tolist(), model.cluster_centers_.tolist()))
            
            gr = [[] for _ in range(ng)]
            for i in range(len(model.labels_)):
                gr[model.labels_[i]].append(idx[i])
                 
            gr_new = []
            for g in gr: 
                cnt_in_g = 0
                st = ""
                for ss in g:
                    cnt_in_g += 1
                    st += str(cnt_in_g) + ") " + ss + "; "
                st = st.strip(' ;')
                gr_new.append(st)
            nip += 1
            gr_new.append(f"<input name='{'b-' if badi else ''}est{nip}' type='range' min='-2' max='2' value='0' step='1' list='tickmarks'/>")
            gr_new.append(f"<input type='hidden' name='{'b-' if badi else ''}val{nip}' value='{idxm[-1]}' />")
            mlb.append(gr_new)
        

        html += delm + f"<h5>Варианты разбиения на {ng} групп{'ы' if ng != 5 else ''}</h5>" + pd.DataFrame(mlb, index=idxm, columns=idxg).sort_index(ascending=False).head(3).to_html(escape=False, index= (id==65 or id==20 or id==94 or id==73))
        idxg  = ["g1", "g2", "g3", "g4", "g5", "g6", 'g7', 'g8'][:ng] + ["оцените этот вариант"] + [""]
        idxm = []
        hol = 0
        mlb = []

        
        while True:
            model = AgglomerativeClustering(n_clusters=ng)
            model.fit(tdfa)


            silhouette_avg = get_score(tdfa, model.labels_)
            
            if silhouette_avg in list(map(lambda x: x[0],idxm)):
                hol += 1
                if hol == 20:
                    break
                continue
            hol = 0
            idxm.append((silhouette_avg, model.labels_.tolist()))
            
            gr = [[] for _ in range(ng)]
            for i in range(len(model.labels_)):
                gr[model.labels_[i]].append(idx[i])
                 
            gr_new = []
            for g in gr: 
                cnt_in_g = 0
                st = ""
                for ss in g:
                    cnt_in_g += 1
                    st += str(cnt_in_g) + ") " + ss + "; "
                st = st.strip(' ;')
                gr_new.append(st)
            nip += 1
            gr_new.append(f"<input name='{'b-' if badi else ''}est{nip}' type='range' min='-2' max='2' value='0' step='1' list='tickmarks'/>")
            gr_new.append(f"<input type='hidden' name='{'b-' if badi else ''}val{nip}' value='{idxm[-1]}' />")
            mlb.append(gr_new)
        

        html += delm + f"<h5>Варианты ward разбиения на {ng} групп{'ы' if ng != 5 else ''}</h5>" + pd.DataFrame(mlb, index=idxm, columns=idxg).sort_index(ascending=False).head(3).to_html(escape=False, index= (id==65 or id==20 or id==94 or id==73))
    # clu_pr = pd.DataFrame(model.transform(tdfa), index=idx, columns=idxg).to_html()

    # html += delm + clu_pr
     
    if len(badclmns) == 0 or badi:
        return (html , un2, [kmo], [dt])
    else:
        goodclm = list(filter(lambda c: c not in badclmns, clm))
        gooddf = df[df.columns[df.columns.isin(goodclm)]] 
        ca = create_analysis(gooddf, nf, goodclm, idx, df100, badclmns, True, id)
        return (html + delm + ca[0] + delm + "<label><input type='checkbox' name='most_like'></input>Мне больше понравился вариант с добавлением</label>", un2, [kmo, ca[2][0]], [dt, ca[3][0]])





def show_ans(request,id=73):


    u = User.objects.get(id=id)
    answers = u.answer_set.all()

    an = "<br>"
    for aa in answers:
        an += aa.q + ": " + aa.a + "<br>"

    return render(request,  "sandbox/un.html", {'pth': 'un' + str(id), 'id': id, 'an': an})



def calculate_df(id):


    u = User.objects.get(id=id)
    items = u.item_set.all()
    pages = sorted(u.page_set.exclude(number=0).exclude(prop_name=""),  key=lambda p : p.number)
    idx = []
    clm = []
    dta = []

    pages_bool = [False for i in range(len(pages))]
    pages_names = ['' for i in range(len(pages))] 

    for i in range(len(pages)): 

        p = pages[i] 
        isEst = p.is_saved
        if isEst:
            for itm in items:
                est = Estimation.objects.filter(item=itm, number=p.number).first()
                if not est or est.value == -1000: 
                    isEst = False
                    break 
        pages_bool[i] = isEst
        pages_names[i] = p.prop_name

    for itm in items:  
        idx.append(itm.name)
        cda = []
        ests = sorted(itm.estimation_set.all(), key=lambda estm : estm.number) 
        for ii in range(len(ests)):
            if ii < len(pages_bool) and pages_bool[ii]:
                cda.append(ests[ii].value)
        for cmpon in get_rgb(itm.color):
            cda.append(cmpon)
        dta.append(cda)
    for p in range(len(pages_names)):
        if pages_bool[p]:
            clm.append(pages_names[p])
    for cn in ["r", "g", "b"]:
        clm.append(cn) 

    df = pd.DataFrame(dta, idx, clm) 


def get_score(df, lbl):
    try:
        return silhouette_score(df, lbl)
    except:
        return -100



def plot(request,id=73, nf=5):

    u = User.objects.get(id=id)
    if id == 115:
        if not request.user.is_authenticated:
            return redirect("/register")
        if request.user.id != 115 and request.user.id != 20:
            return redirect("/results")

    if request.method == "POST":
        for key in request.POST:
            an = Answer.objects.get_or_create(user=u, q=key)[0]
            an.a = request.POST[key]
            an.save()
        return render(request, "sandbox/un.html", {'pth': 'un' + str(id), 'id': id})


    x = []
    y = []
    colors=[]
    names=[]
    rads = []
    
    items = u.item_set.all()
    pages = sorted(u.page_set.exclude(number=0).exclude(prop_name=""),  key=lambda p : p.number)
    idx = []
    clm = []
    dta = []

    pages_bool = [False for i in range(len(pages))]
    pages_names = ['' for i in range(len(pages))] 

    for i in range(len(pages)):#-1 if id==73 else len(pages)):


        p = pages[i] 
        isEst = p.is_saved
        if isEst:
            for itm in items:
                est = Estimation.objects.filter(item=itm, number=p.number).first()
                if not est or est.value == -1000: 
                    isEst = False
                    break 
        pages_bool[i] = isEst
        pages_names[i] = p.prop_name 
    for itm in items: 
        x.append(itm.estimation_set.get(number=10).value)
        y.append(itm.estimation_set.get(number=8).value)
        colors.append(itm.color)
        names.append(itm.name)
        rads.append(3)
        idx.append(itm.name)
        cda = []
        ests = sorted(itm.estimation_set.all(), key=lambda estm : estm.number) 
        for ii in range(len(ests)):
            if ii < len(pages_bool) and pages_bool[ii]:
                cda.append(ests[ii].value)
        # for cmpon in get_rgb(itm.color):
        #     cda.append(cmpon)
        dta.append(cda)
    for p in range(len(pages)):#-1 if id==73 else len(pages)):
        if pages_bool[p]:
            clm.append(pages_names[p])

    last=None
    # if id == 73:
    #     last = []
    #     for itm in items:
    #         ests = sorted(itm.estimation_set.exclude(value=-1000), key=lambda estm : estm.number) 
    #         last.append(ests[-1].value)

    # for cn in ["r", "g", "b"]:
    #     clm.append(cn) 

    # '''
    # Это строковый литерал.
    # Но здесь он используется как многострочный комментарий
    # '''
    # from sklearn.preprocessing import StandardScaler, MinMaxScaler 
    # data = UserData.objects.get_or_create(user=u)[0]
    # if data.df != "":
    #     import json
    #     df = pd.DataFrame.from_dict(json.loads(data.df)) 
    # else:
    #     df = pd.DataFrame(dta, idx, clm) 
    #     data.df = df.to_json()
    #     data.save()

    df100 = df = pd.DataFrame(dta, idx, clm) 
    dfsc = preprocessing.scale(df)
    pth = f'static/rep_grid{id}.xlsx'
    df.to_excel(pth)  

    dfhtml = df.to_html()  
    #return render(request, "sandbox/index.html", { 'dfhtml': dfhtml })
    dfdhtml =  df.describe().astype("int32").to_html() 
    dfchtml = (df.corr() * 100).round().astype("int32").to_html()
    TOOLS="hover,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,save"  
  
     
    source = ColumnDataSource(data=dict(x=x,
                                        y=y,
                                        names=names,
                                        color=colors,
                                        rad=rads))


    TOOLTIPS = [ 
        ("имя", "@names"),
        ("оценки", "(@x, @y)"),
    ]

    p = figure( title_location="left", tooltips=TOOLTIPS,tools=TOOLS)

    
    p.scatter( source=source, size=14, color='color', radius='rad' ) 

    labels = LabelSet(x='x', y='y', text='names',
                x_offset=5, y_offset=5, source=source, render_mode='canvas')


    p.add_layout(labels)



    #p.scatter(x, y, radius=5, fill_color=colors) 

    # labels = LabelSet(x='x', y='y', text='name', level='glyph',text_font_size='9pt',
    #            x_offset=5, y_offset=5, render_mode='canvas')

    # p.add_layout(labels)


    





    
    # radii = 1 

    #

    # TOOLTIPS = [ 
    #     ("(x,y)", "($x, $y)"),
    #     ("desc", "@desc"),
    # ]


    # p = figure(tools=TOOLS,tooltips=TOOLTIPS)

    # p.scatter(x, y, radius=radii, fill_color=colors
    #         ) 

    html = file_html(p, CDN, "my plot")
    ca = create_analysis(df100, 2 if (id == 94 or id == 106) else 3, clm, idx, df100, None, False, id)
    kmo_model2 = str(ca[2][0]) if len(ca[2])==1 else str(ca[2][0]) + " --- " + str(ca[2][1])
    allhtml = ca[0]  + delm
    un2 = ca[1]
    dt = str(ca[3][0]) if len(ca[3])==1 else str(ca[3][0]) + " --- " + str(ca[3][1])

    
    scaler = MinMaxScaler(feature_range=(-100,100))
    X_one_column = dfsc.reshape([-1,1])
    result_one_column = scaler.fit_transform(X_one_column)
    tra = result_one_column.reshape(dfsc.shape) 
    dfsc = pd.DataFrame(tra, idx, clm).round().astype("int32").to_html()
     
    return render(request, "sandbox/index.html", {'dt': dt, 'dfsc': dfsc, 'pl': html, 'pth': 'plt' + str(id), 'id': id, 'kmo_model2':kmo_model2, 'allhtml': allhtml,"dfhtml": dfhtml,  "dfdhtml": dfdhtml, "dfchtml": dfchtml, "un2": un2})


    # return render(request, "sandbox/index.html", {'pth': 'plt' + str(id), 'id': id,'kmo_model2':kmo_model2, 'allhtml': allhtml,"dfhtml": dfhtml, "dfchtml": dfchtml, })#'pl': html,  "dfhtml": dfhtml, "dfdhtml": dfdhtml, "dfchtml": dfchtml, 


 
