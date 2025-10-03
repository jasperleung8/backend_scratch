from flask import Flask
import scratchattach as sa
from threading import Thread
import backend_code

Thread(target=backend_code.run).start()

session = sa.login_by_id(".eJxVj0trwzAQhP-LzomrtS3Zzi0lJZfSQl-Qk9FjYyt2pGDLBFL637uCXHJbvtmZnf1ly4yTV2dkG3ZS8wUnPQW2Yq1aYt8msXWWtKrOKyFrTlLEOZoQBpc81zANaB8NWpkBfXIlhj46o6ILPrsLc_aBl_EOn-_LlBtoIFNTcpCAjbUgSiu15rJSpTaCawMlNBu-P-z8z26_AIx44-v91-3oXvX79-cLxYyhc37tLpRUywzKIoNCZnkuUslR-W5RXWpOt1bMngiENroz3oJPeHvGiao9veG1PdBzj6_1au5pKdegG9sA8KKoKlC2Nrk5CoOglOCSQKGlMCX7-we-lnF5:1utNCF:7HeahINQVqpyfTonWxS7-ZzztSY", username="jasperbro") 

cloud = session.connect_cloud("1212801905")
client = cloud.requests()

client.send("server started")
@client.request
def ping(): 
    print("Ping request received")
    return "pong" 

@client.request
def Comments(argument1):
    project = session.connect_project(argument1)
    if project.comments_allowed :
        Comments = project.comments(limit=20, offset=0)
        return_comment = []
        for comment in Comments :
            author = comment.author
            content = comment.content
            time = comment.datetime_created
            return_comment.append(f"{comment.author()} : {comment.content} at {comment.datetime_created}")
            replies = comment.replies(limit=4)
            for reply in replies :
                return_comment.append(f"        {reply.author()} : {reply.content} at {reply.datetime_created}")
    else :    
        return_comment = "Not allowed"
    return return_comment

@client.request
def Update():
    project = session.connect_project("1212801905")
    Comments = project.comments(limit=20, offset=0)
    return_comment = []
    return_comment.append("Click green flag, wait and reload to see change !")
    for comment in Comments :
        author = comment.author
        content = comment.content
        time = comment.datetime_created
        return_comment.append(f"{comment.author()} : {comment.content}")
        replies = comment.replies(limit=20)
        for reply in replies :
            return_comment.append(f"        {reply.author()} : {reply.content}")
    projectset = session.connect_project("1212801905")
    set = "Comments for this project :"
    for item in return_comment :
        set = f"{set}\n{item}"
    projectset.set_notes(set)
    return "Updated"

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Back4apper!"

def run()
    client.start(thread=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
