from flask import Flask
app = Flask(__name__)

@app.route('/user/<int:post_num>')
# here I set the url to include a positive integer which will be manipulated later in the code
def show_num(post_num):
    return 'The user number multiplied by 100 is %d' % (post_num*100)

#set port to 8003
if __name__ == "__main__":
    app.run(port=8003)

#this is an upload change I am making