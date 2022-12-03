from flask import render_template, request
from flask import Flask
import pickle

app = Flask(__name__)

modelo = pickle.load(open('modelo.pkl','rb'))
normalizacion = pickle.load(open('normalizacion.pkl','rb'))

@app.route("/") 
def index():
	return render_template('index.html')

@app.route("/resultado", methods=['POST']) 
def resultado():
	ango = int(request.form["agno"])
	comuna = request.form["comuna"]
	predict = []
	fechas = []
	diccionario = {
		'1':2794,
		'2':1593,
		'3':2548,
		'4':1824,
		'5':834,
		'6':1569,
		'7':1763,
		'8':1969,
		'9':1224,
		'10':597,
		'11':103,
		'12':245,
		'13':1971,
		'14':70,
		'15':353,
		'16':782,
		'50':65,
		'60':750,
		'70':330,
		'80':655,
		'90':97,
		'99':422
	}
	agnoIni = 2012 if ango <= 2022 else 2019
	for fecha in range(agnoIni,ango+1):
		fechas.append(fecha)
		x_norm = normalizacion.transform([[fecha,comuna]])
		predict.append(round(modelo.predict(x_norm)[0],0))
	print(fechas)
	print(predict)
	return render_template('resultado.html', resultado=predict,xVariable=fechas,lista=diccionario[comuna],comuna=comuna,agno=ango)
app.run(debug=True)