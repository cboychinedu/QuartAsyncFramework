#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
from quart import Blueprint
from quart import render_template 

# Creating the blueprint object 
about = Blueprint('about', __name__, template_folder='templates', static_folder='static'); 

# Creating the About page 
@about.route("/", methods=["GET"])
def AboutPage(): 
    # Rendering the about page 
    return render_template('about.html'); 