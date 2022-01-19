import re

def step7(newid):
    len_id = len(newid)
    if len_id == 3:
        return newid
    
    newid += newid[len_id-1]
    newid=step7(newid)
    
    return newid

def solution(new_id):
    
    #1단계
    newid = new_id.lower()
    #2단계
    newid = re.sub(r'[^0-9a-zA-Z-_.]','',newid)
    #3단계
    newid = re.sub(r'[.]+', '.',newid)
    #4단계
    newid = newid.strip(".")
    #5단계
    if newid == "":
        newid = "a"
    #6단계
    if len(newid) >= 16 :
        newid = newid[:15]
        newid = newid.strip(".")
    #7단계
    if len(newid) <=2:
        newid = step7(newid)
    
    print(newid)
    answer = newid
    return answer
