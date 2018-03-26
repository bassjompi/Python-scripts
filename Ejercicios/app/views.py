from flask import render_template, flash, redirect
from app import app


@app.route('/login', methods=['GET', 'POST'])
def main():
    return render_template('login.html')