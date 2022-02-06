import requests
import json

# url =   "https://mail.qq.com/cgi-bin/readtemplate"
# data = {
#     "target":"",
#     "account":"1106893786",
#     "qqmailkey":"193a157e3c2b93b2852e7e86c69ea060a8c750f166164a96eec243a57ff773ac",
#     "check":"false",
#     "ft":"loginpage",
#     "t":"loginpage_new_jump",
#     "vt":"passport",
#     "vm":"wpt"
# }
url =   "https://mail.qq.com/cgi-bin/login"
data = {
    "target":"",
    "ds":"a8724ce31fbb925636e2b3b65a663821",
    "ft":"loginpage",
    "vt":"passport",
    "vm":"wpt"
}


res = requests.post(url,data)
# response_url = res['dara']['url'][0]
# request_url = response_url
# print(type(res))
print(res)
# print(res.cookies)
