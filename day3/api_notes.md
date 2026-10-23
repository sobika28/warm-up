HTTP
- hyper text transfer protocol
- its communication protocol used to transfer information between client and server

client:
- sends the request
server:
- receives the request and process it

url(Uniform Resource Locato):
eg: https://abc.example.com/items/10?category=books
https: Protocol
api.example.com: Domain name
/items/10: Resource path
category=books: Query parameter

http methods:
get : retrieves the data from server
post: sends data to create a resource
put: replace or updates a resource
delete:deletes a resource

http status code:
2xx :The request was successful. (Eg: 200 OK)
4xx :There is a problem with the request or access. (Eg:404 Not Found)
5xx :The server encountered a problem. (Eg: 500 Internal Server Error)

headers:
provides extra information abt request or response

JSONbodies:
- it contains data in structured format
eq:{"name":"alice","age" :20}

API keys:
an api key is credential used by some apis to identify or authorize a user application
it should be kept secret

Rate limit:
A rate limit restricts how many requests an application can make during a particular period. If the limit is exceeded, the API may return status code 429 Too Many Requests