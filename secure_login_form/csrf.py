from flask import session
import secrets

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        csrf_token = request.form.get('csrf_token')
        if not csrf_token or csrf_token != session.get('csrf_token'):
            return 'CSRF Token Invalid', 403
    else:
        session['csrf_token'] = secrets.token_hex(16)
    return render_template('login.html', csrf_token=session['csrf_token'])