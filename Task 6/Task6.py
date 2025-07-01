from flask import Flask, request, render_template, redirect, url_for
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)