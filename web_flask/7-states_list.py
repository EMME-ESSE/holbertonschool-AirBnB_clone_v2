#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """List all states"""   
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)  
    return render_template('7-states_list.html', states=sorted_states)

@app.teardown_appcontext
def close_state(exception):
    """Close database connection"""    
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
