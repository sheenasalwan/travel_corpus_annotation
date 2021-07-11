# pip install uvicorn
# pip install fastapi
# pip install aiofiles

import pandas as pd
from fastapi import FastAPI
import uvicorn
from fastapi.responses import FileResponse, HTMLResponse

data = pd.read_csv("../../data/final_corpus.csv")
annotations = pd.read_csv("../../data/final_annotations_one_token.csv")


app = FastAPI()

# Functions for generating HTML
def create_row(data):
    '''Given a pandas dataframe will create a new HTML row out of each row in the dataframe'''
    S = []
    
    for _, row in data.iterrows(): 
        S.append("<tr>") # New Table Row
        for col in data.columns:
            S.append("<td>" + str(row[col]) + "</td>") # New Field In Row
    
        S.append("</tr>") # Table Row Closing Tag
    return "".join(S) # Return HTML

def create_header(data):
    '''Given a pandas dataframe will create a HTML header row'''
    S = []
    S.append('<tr>') # New Table Row

    for col in data.columns:
        S.append('<th>' + col.upper() + '</th>') # New Field in Row

    S.append('</tr>') # Table Row Closing Tag
    return "".join(S) # Return HTML

def put_in_table(data):
    '''Puts given dataframe into HTML table format'''
    return "<table class='w3-table-all'>" + create_header(data) + create_row(data) + "</table>"

def put_in_dropdown(data):
    '''Puts given list into HTML dropdown format'''
    select_str = "<select name='annot_drop_down' id='annot_drop_down'>"

    for item in lst:
        select_str += "<option value="+item+">"+item+"</option>"

    select_str += "</select>"
    return select_str

@app.get("/")
def start():
    #return FileResponse("src/web_interface/group7.html") # for docker
    return FileResponse("group7.html")

@app.get("/{filename}")
def get_file(filename):
    #return FileResponse("src/web_interface/" + filename) # for docker
    return FileResponse(filename)

@app.get("/pos/")
def search_documents(search):
    '''Returns documents that match the search query'''
    terms = search.split(" ")

    regstr = '|'.join(terms)
    results = data[data["Overview"].str.contains(regstr, na=False)]
    n_results = 3

    if results.size == 0:
        return HTMLResponse("No documents found!")
    else:
        if results.size > n_results:
            results = results[:n_results]
        results = results[["Document ID","Subject", "Predicate", "Object", "Overview"]]
        return HTMLResponse(put_in_table(results))

@app.get("/pos_annot/")
def search_documents_for_annotations(annot_drop_down):
    '''Returns documents that match the search query annotation'''
    result = annotations.query("Annotation_Token == @annot_drop_down")
    doc_id_list = list(result['Document_ID'])

    results = data[data['Document ID'].isin(doc_id_list)]
    n_results = 3

    if results.size == 0:
        return HTMLResponse("No documents found!")
    else:
        if results.size > n_results:
            results = results[:n_results]
        results = results[["Document ID","Subject", "Predicate", "Object", "Overview"]]
        return HTMLResponse(put_in_table(results))


def get_annotations():
    '''Returns annotations'''

    results = annotations["Annotation Token"].unique()

    return HTMLResponse(put_in_dropdown(results))



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9999, debug=True)