from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
model = pickle.load(open('SB_DecisionTreemodel_V2.pkl', 'rb'))


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def prediction():
    if (request.method == 'POST'):
        e = float(request.form['e'])
        i = float(request.form['i'])
        om = float(request.form['om'])
        w = float(request.form['w'])
        q = float(request.form['q'])
        dataarc = float(request.form['dataArc'])
        obs = float(request.form['obs'])


        predictors = [e,i,om,w,q,dataarc,obs]
        result = model.predict_proba([predictors])

        a0=round(rsesult[0][0]*100,2)
        a1=round(result[0][1]*100,2)
        a2=round(result[0][2]*100,2)
        a3=round(result[0][3]*100,2)

        a0 = "Undefined orbit : "+str(a0)+"%"
        a1 = "Hyperbolic Comet orbit : "+str(a1)+"%"
        a2 = "Jupyter family Comet orbit : "+str(a2)+"%"
        a3 = "Parabolic Comet orbit : "+str(a3)+"%"


        return render_template('index.html', x0=a0,x1=a1,x2=a2,x3=a3)


if __name__ == '__main__':
    app.run(debug=True)