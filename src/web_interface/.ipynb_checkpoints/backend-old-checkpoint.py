import pandas as pd
from fastapi import FastAPI
import uvicorn
from fastapi.responses import FileResponse, HTMLResponse

data = pd.read_csv("../../data/final_corpus.csv")

app = FastAPI()

# Functions for generating HTML
def create_row(data):
    '''Given a pandas dataframe will create a new HTML row out of each row in the dataframe'''
    S = []
    
    i = 1
    for _, row in data.iterrows(): 
        if i % 2 == 0:
            S.append("<tr class='even'>") # New Table Row
        else:
            S.append("<tr class='odd'>")
        i += 1
        for col in data.columns:
            S.append("<td class='table_field'>" + str(row[col]) + "</td>") # New Field In Row
    
        S.append("</tr>") # Table Row Closing Tag
    return "".join(S) # Return HTML

def create_header(data):
    '''Given a pandas dataframe will create a HTML header row'''
    S = []
    S.append('<tr class=\'even\'>') # New Table Row

    for col in data.columns:
        S.append('<th>' + col.upper() + '</th>') # New Field in Row

    S.append('</tr>') # Table Row Closing Tag
    return "".join(S) # Return HTML

def put_in_table(data):
    '''Puts given dataframe into HTML table format'''
    return "<table>" + create_header(data) + create_row(data) + "</table>"


@app.get("/")
def start():
    return FileResponse("src/web_interface/group7.html")

@app.get("/{filename}")
def get_file(filename):
    return FileResponse("src/web_interface/" + filename)

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
        results = results[["Subject", "Predicate", "Object", "Overview"]]
        return HTMLResponse(put_in_table(results))

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9999, debug=True)