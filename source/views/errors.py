from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('505.html'), 500

