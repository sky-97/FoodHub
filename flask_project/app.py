from flask import Flask,request,render_template,url_for
import model

app = Flask(__name__)
model.init_db()

@app.route("/home",methods=["POST","GET"])
def home():
	if request.method == 'POST':
		return render_template('food.html',todos=[[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]])
	else:
		return render_template('home.html')

@app.route("/food",methods=["GET","POST"])
def food():
	if request.method == 'POST':
		search = request.form['search']
		todos = model.get_details(search)
		print(todos)
		return render_template('food.html', todos = todos)
	else:
		return render_template('food.html',todos=[[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]])

	# else:
	# todos = model.show()
	# return render_template('food.html',todos=todos)

if __name__ == "__main__":
	app.run(debug=True)
