from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'Cast in the name of God, ye not guilty'

@app.route('/')
def counter_main():
    session['counter'] = 0
    session['truecount'] = 0
    return redirect('/counter')

@app.route('/counter')
def counter():
    session['counter'] += 1
    session['truecount'] += 1
    return render_template('index.html', counter = session['counter'], truecount = session['truecount'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/plus_two')
def plus_two():
    session['counter'] += 1
    return redirect('/counter')

@app.route('/soft_reset')
def soft_reset():
    session['counter'] = -1
    return redirect('/counter')

@app.route('/varcount', methods=['POST'])
def varcount():
    session['counter'] += (int(request.form['num']) - 1)
    return redirect('/counter')



if __name__ == "__main__":
    app.run(debug = True)