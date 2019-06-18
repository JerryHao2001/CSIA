# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 13:56:00 2019

@author: 11658
"""

# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
     
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

if __name__ == '__main__':
    app.run()