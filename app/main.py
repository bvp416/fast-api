"""
Implementation of a URL lookup service

In our theoretical security company, have an HTTP proxy that scans traffic
looking for malicious URLs. Before allowing HTTP connections to be made,
this proxy asks a service that maintains several databases of URLs that can
be referenced to determine if a resource being requested is known to contain malware.

In the language/framework of your choice, write a small web API service that
responds to GET requests where the caller passes in a URL and the service responds
with information about that URL. The GET requests look like this:

    GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}

The caller wants to know if it is safe to access that URL or not.
As the implementer, you get to choose the response format and structure.
These lookups are blocking users from accessing the URL until the caller
receives a response from your service.
"""

from fastapi import FastAPI

app = FastAPI()

db = [
    {
    'name' : 'youtube.com',
    'status' : 'safe'
    },
    {
    'name' : 'menlosecurity.com',
    'status' : 'unsafe'
    },
]

def return_query(query_string):
    """Queries the database and returns data on the queried object."""
    return list(filter(lambda item: item['name'] == f'{query_string}', db))[0]

@app.get('/urlinfo/1/{hostname_and_port}/{original_path_and_query_string}')
def get_resource_scan(
    hostname_and_port: str,
    original_path_and_query_string: str
    ):
    """GET call that receives request to scan specified resource object."""
    result = return_query(original_path_and_query_string)
    return result
