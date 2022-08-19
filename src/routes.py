from flask import request, render_template, render_template_string
from flask import current_app as app


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        value = result['name']
        template = '''
        <p> Hello World</p>
        {}
        '''.format(value)
        return render_template_string(template)
