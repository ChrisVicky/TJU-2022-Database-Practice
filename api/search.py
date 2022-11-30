from flask import Blueprint, Flask, make_response, render_template, request, url_for, redirect
from api.service import SearchService
searchpage = Blueprint('searchpage', __name__)

##
# @brief Search Posts titles
@searchpage.route('/', methods=('GET', 'POST'))
def searchPage():
    if request.method=='POST':
        content = request.form['content']
        errorcode, posts = SearchService.getSearchResult(content, 12)
        if errorcode:
            return render_template('500.html', msg=posts)
        return render_template('results.html', posts=posts, content=content)
    return render_template('search.html')



