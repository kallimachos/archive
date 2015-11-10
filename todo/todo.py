import sqlite3
from bottle import route, run, debug, template, request, static_file, error

@route('/')
@route('/todo')
# demonstrates two routes for the same function
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    return(template('make_table', rows=result))

@route('/new', method='GET')
# demonstrates input using GET
def new_item():
    if request.GET.get('save','').strip():
        new = request.GET.get('task', '').strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid
        conn.commit()
        c.close()
        return('<p>The new task was inserted into the database, the ID is %s</p><p><a href="/todo">Home</a></p>' % new_id)
    else: return(template('new_task.tpl'))

@route('/edit/<no:int>', method='GET')
# demonstrates validating input (in this case checking the input is an integer)
def edit_item(no):
    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status = request.GET.get('status','').strip()
        if status == 'open':
            status = 1
        else:
            status = 0
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()
        return('<p>The item number %s was successfully updated</p><p><a href="/todo">Home</a></p>' % no)
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()
        return(template('edit_task', old=cur_data, no=no))

@route('/item:<item:re:[0-9]+>')
# demonstrates a regular expression in a route
def show_item(item):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (item))
    result = c.fetchall()
    c.close()
    if not result:
        return 'This item number does not exist!'
    else:
        return('<p>Task: %s </p><p><a href="/todo">Home</a></p>' %result[0])

@route('/json<json:re:[0-9]+>')
# demonstrates returning a json object; all it requires is returning a Python dictionary, which bottle converts to a json object
def show_json(json):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json))
    result = c.fetchall()
    c.close()
    if not result:
        return {'task':'This item number does not exist!'}
    else:
        return {'Task': result[0]}

@route('/help')
# demonstrates returning a static file instead of a python function
def help():
    return static_file('help.html', root='./static/')

@error(403)
# demonstrates catching an error using an error route
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
# demonstrates catching an error using an error route
def mistake404(code):
    return 'Sorry, this page does not exist!'

# debug and reloader must be removed when the application is moved from development to production
debug(True)
run(reloader=True)