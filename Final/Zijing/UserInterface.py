from flask import Flask, jsonify, request, Response
from SearchEngine import SearchEngine
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def search():
    #print request.args.get('key')
    if len(request.args.get('key'))==0:
        html = render_template("search.html", ol=False)
    else:
	rank = None
        rtn = se.search(request.args.get('key'))
	if rtn!=None:
            rank = sort_by_value(rtn)
        html = render_template("search.html", ol=rtn, rank=rank)
    #return jsonify({'result': rtn})
    return html

def sort_by_value(d): 
    items=d.items() 
    backitems=[[v[1],v[0]] for v in items] 
    backitems.sort(reverse=True) 
    return [ backitems[i][1] for i in range(0,len(backitems))] 



if __name__ == '__main__':
    se = SearchEngine()
    se.buildTries()
    app.run(debug=True, port=8886)

