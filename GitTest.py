from flask import Flask
app = Flask(__name__)

@app.route('/user/<int:post_num>')
# here I set the url to include a positive integer which will be manipulated later in the code
def show_num(post_num):
    return 'The user number multiplied by 100 is %d' % (post_num*100)

#set port to 8003
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002)

#added port 8002 as a requirement