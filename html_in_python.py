import pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__)

df = pd.DataFrame({"name" : ["bofa", "cigna"], "id" : [1121, 1122]}, index = [0, 1])

@app.route('/')
def index():
	return """
	<html>
		<body>
			<h1>Query Companies</h1>
			<h2>Choose the vendor</h2>

			<form action="/netwise/">
				<input type="submit" value="Netwise" />
			</form>

			<form action="/zoominfo/">
				<input type="submit" value="Zoom-Info">
			</form>
		</body>
	"""

@app.route('/netwise/', methods = ["GET", "POST"])
def netwise():
	errors = ""
	if request.method == "POST":
		cm_name = None
		try:
			cm_name = str(request.form["company name"])
		except:
			errors += "<p>{!r} is not a number.</p>\n".format(request.form["company name"])
		if cm_name is not None:
			result = df[df.name == cm_name].to_html()
			return """
				<html>
					<body>
						<p>The company name is {result}</p>
						<p><a href="/netwise/">Click to search other Company</p>
					</body>
				</html>

				""".format(result = result)

	return """
		<html>
			<body>	
				{errors}
				<p>Enter your Company Name:</p>
				<form method="post" action=".">
					<p><input name="company name" /></p>
					<p><input type="submit" value="Search" /></p>
				</form>
			</body>
		</html>	
		""".format(errors = errors)



if __name__ == '__main__':
	app.run(debug=True)

