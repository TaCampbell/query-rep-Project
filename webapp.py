from flask import Flask, request, render_template
app = Flask(__name__)  

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/contact")
@app.route('/contact/<name>') 
def contact(name=None):         
	return render_template('contact.html', name=name)

	
@app.route("/left") 
def left(name=None): 
 return render_template('left.html', name=name)
	

@app.route("/right") 
def right(name=None): 
 return render_template('right.html', name=name)


@app.route("/none") 
def none(name=None): 
 return render_template('none.html', name=name)
 
if __name__ == "__main__":     
	app.run()
