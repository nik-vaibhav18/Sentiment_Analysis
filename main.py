from flask import Flask,request
from flask import Response
import pandas
from utils.utils import createDirectoryforUser

app=Flask(__name__)

@app.route('/train', methods=['GET', 'POST'])
def train():
    try:
        if request.get_json() is not None:
            data=request.json['data']
        if request.get_json('userId') is not None:
            userId=str(request.get_json('userId'))
        if request.get_json('projectId') is not None:
            projectId=str(request.get_json('projectId'))

            createDirectoryforUser(userId,projectId)
        
        path=trainingDataFolder+'/'+userId+'/'+projectId
        







if __name__ == '__main__':    
    app.run(debug=True)