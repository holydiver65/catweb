from flask import Flask, render_template

import os



#from PIL import Image
#insert image path below
#img = Image.open("/home/amang/vscode/ hard drive webapp/static/pics/felixsox1.PNG" )
#print(img.width,img.height)
#img.show()
#img = img.resize((int(img.width/3),int(img.height/3)))
#print(img.width,img.height)

#img.save("new_img.JPG")
#img.show()

app = Flask(__name__)

picsFolder = os.path.join('static', 'pics')



app.config['UPLOAD_FOLDER'] = picsFolder


@app.route('/')
def index():
    #pic1 =os.path.join (app.config['UPLOAD_FOLDER'],'pic1.PNG')

    #imagelist = os.listdir('static/pics')
    #imagelist =['pics/' + image for image in imagelist]
    
    return render_template('index.html')
    



                            

    

@app.route("/history of cats")

def cats():
    return render_template("history.html")

@app.route("/cat pics")
def new():
    pic1 =os.path.join (app.config['UPLOAD_FOLDER'],'pic1.PNG')

    imagelist = os.listdir('static/pics')
    imagelist =['pics/' + image for image in imagelist]
    return render_template("new.html", imagelist =imagelist)
    
    

if __name__ == '__main__':
    app.run()






