import face_recognition as fc
import pandas as pd
import cv2
import list_
from datetime import datetime, timedelta, date

def camera_on():
    v = cv2.VideoCapture(0)
    data = pd.read_csv("My_faces.csv")
    dn = (data["Name"].values)
    q = list(set(dn))
    de = data.drop("Name" , axis = 1)
    de = de.to_numpy()
    dic = {}
    for i in q:
        dic[i] = []
    for i in range(len(dn)):
        dic[dn[i]].append(list_.change_to_list(de[i][0]))
    end_time = datetime.now() + timedelta(seconds=10)
    while datetime.now() < end_time:
        r,live = v.read()
        i  = cv2.resize(live,(200,200))
        fll = fc.face_locations(i)
        if len(fll)>0:
            E = fc.face_encodings(i,fll)
            for k in range(len(fll)):
                [x1,y1,x2,y2] = fll[k]
                cv2.rectangle(i,(y2,x1),(y1,x2),(0,0,255),2)
            for k in range(len(fll)):
                dic_e = {}
                for f in q:
                    dic_e[f] = fc.compare_faces(dic[f],E[k])
                dic_t = {}
                for g in dic_e:
                    dic_t[g] = dic_e[g].count(True)
                m = max(dic_t.values())
                
                for h in dic_t:
                    if dic_t[h] == m :
                        return(h)
    return(None)
