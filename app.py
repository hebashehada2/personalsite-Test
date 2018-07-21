# from flask import Flask
# app=Flask(__name__)
# @app.route('/hello')
# def index():
# 	return '8000'

# @app.route('/goodbye')
# def goodbye ():
# 	return'good bye!'

# @app.route('/')	
# def sia():
# 	return  'siaaa'


# if __name__=='__main__':	
# 	app.run(port =8585 ,debug = True)


# from flask import Flask
# import random
# app=Flask(__name__)

# @app.route('/qoute')
# def qoute():
# 	qoute=['i am strong','i am cute' , 'i am lovely ','i am drop dead gorgeous']
# 	a=(random.choice(qoute))
# 	return a


# if __name__=='__main__':	
# 	app.run(port =5000,debug = True)





# @app.route('/website')
# def website():
# 	return render_template('about_me1.html')


# if __name__=='__main__':	
# 	app.run(port =5000,debug = True)



from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def load_page():
    return render_template('tast_camp.html')
 
if __name__ == '__main__':
	app.run(debug=True)