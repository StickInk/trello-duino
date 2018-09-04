import requests

url = "https://api.trello.com/1/boards/Pz4VqRgs"

querystring = {"actions":"all","boardStars":"none","cards":"visible","checklists":"none","fields":"name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames","lists":"open","members":"none","memberships":"none","membersInvited":"none","membersInvited_fields":"all","key":"8ed3b71cfd765ef3d7fd17bd4ca64181","token":"0990ac99337589987515bfc207197621a60d861609595593e67b5f663a48f60f"}

response = requests.request("GET", url, params=querystring)

print(response.text)