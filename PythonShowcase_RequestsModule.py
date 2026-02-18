### Python Showcase Requests Modules ###
print("Beginning of the Python Requests Modules Showcase\n\n\n")


Requests_def = "Requests: The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc)."
import requests
Requests_x = requests.get('https://w3schools.com/python/demopage.htm')
print(f"\n{Requests_def}")
print("    import requests")
print("    Requests_x = requests.get('https://w3schools.com/python/demopage.htm')")
print(f"        print(Requests_x.text) = {Requests_x.text}")




RequestsDelete_def = "Requests Delete: The delete() method sends a DELETE request to the specified url. DELETE requests are made for deleting the specified resource (file, record etc)."
RequestsDelete_x = requests.delete('https://w3schools.com/python/demopage.php')
print(f"\n{RequestsDelete_def}")
print("url		Required. The url of the request\n"
      "allow_redirects		Optional. A Boolean to enable/disable redirection.Default True (allowing redirects)\n"
      "auth		Optional. A tuple to enable a certain HTTP authentication.Default None\n"
      "cert		Optional. A String or Tuple specifying a cert file or key.Default None\n"
      "cookies		Optional. A dictionary of cookies to send to the specified url.Default None\n"
      "headers		Optional. A dictionary of HTTP headers to send to the specified url.Default None\n"
      "proxies		Optional. A dictionary of the protocol to the proxy url.Default None\n"
      "stream		Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True). Default False\n"
      "timeout		Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response. Default None which means the request will continue until the connection is closed\n"
      "verify       Optional. A Boolean or a String indication to verify the servers TLS certificate or not. Default True")
print("    RequestsDelete_x = requests.delete('https://w3schools.com/python/demopage.php')")
print(f"        print(RequestsDelete_x.text) = {RequestsDelete_x.text}One record deleted.")




RequestsGet_def = "Requests Get: The get() method sends a GET request to the specified url."
RequestsGet_x = requests.get('https://w3schools.com')
print(f"\n{RequestsGet_def}")
print("    RequestsGet_x = requests.get('https://w3schools.com')")
print("url		Required. The url of the request\n"
      "params		Optional. A dictionary, list of tuples or bytes to send as a query string.Default None\n"
      "allow_redirects		Optional. A Boolean to enable/disable redirection.Default True (allowing redirects)\n"
      "auth		Optional. A tuple to enable a certain HTTP authentication.Default None\n"
      "cert		Optional. A String or Tuple specifying a cert file or key.Default None\n"
      "cookies		Optional. A dictionary of cookies to send to the specified url.Default None\n"
      "headers		Optional. A dictionary of HTTP headers to send to the specified url.Default None\n"
      "proxies		Optional. A dictionary of the protocol to the proxy url.Default None\n"
      "stream		Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).Default False\n"
      "timeout		Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.Default None which means the request will continue until the connection is closed\n"
      "verify	    Optional. A Boolean or a String indication to verify the servers TLS certificate or not.Default True")
print(f"        print(RequestsGet_x.status_code) = {RequestsGet_x.status_code}")




Requests_Head = "Requests Head: The head() method sends a HEAD request to the specified url. HEAD requests are done when you do not need the content of the file, but only the status_code or HTTP headers."
RequestsHead_x = requests.head('https://www.w3schools.com/python/demopage.php')
print(f"\n{Requests_Head}")
print("    RequestsHead_x = requests.head('https://www.w3schools.com/python/demopage.php')")
print("    url		Required. The url of the request\n"
      "allow_redirects	 Optional. A Boolean to enable/disable redirection. Default False (not allowing redirects)\n"
      "auth		Optional. A tuple to enable a certain HTTP authentication.Default None\n"
      "cert		Optional. A String or Tuple specifying a cert file or key.Default None\n"
      "cookies		Optional. A dictionary of cookies to send to the specified url.Default None\n"
      "headers		Optional. A dictionary of HTTP headers to send to the specified url.Default None\n"
      "proxies		Optional. A dictionary of the protocol to the proxy url.Default None\n"
      "stream		Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).Default False\n"
      "timeout		Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response. Default None which means the request will continue until the connection is closed\n"
      "verify		Optional. A Boolean or a String indication to verify the servers TLS certificate or not.Default True")
print(f"        print(RequestsHead_x.headers) = {RequestsHead_x.headers}")





Requests_Post_def = "Requests Post: The post() method sends a POST request to the specified url. The post() method is used when you want to send some data to the server."
RequestsPost_url = 'https://www.w3schools.com/python/demopage.php'
RequestsPost_myobj = {'somekey': 'somevalue'}
RequestsPost_x = requests.post(RequestsPost_url, json = RequestsPost_myobj)
print(f"\n{Requests_Post_def}")
print("    RequestsPost_url = 'https://www.w3schools.com/python/demopage.php'")
print("    RequestsPost_myobj = {'somekey': 'somevalue'}")
print("    RequestsPost_x = requests.post(RequestsPost_url, json = RequestsPost_myobj)")
print(f"        print(RequestsPost_x.text) = {RequestsPost_x.text}")
print("url		Required. The url of the request\n"
      "data		Optional. A dictionary, list of tuples, bytes or a file object to send to the specified url\n"
      "json		Optional. A JSON object to send to the specified url\n"
      "files		Optional. A dictionary of files to send to the specified url\n"
      "allow_redirects		Optional. A Boolean to enable/disable redirection.Default True (allowing redirects)\n"
      "auth		Optional. A tuple to enable a certain HTTP authentication.Default None\n"
      "cert		Optional. A String or Tuple specifying a cert file or key.Default None\n"
      "cookies		Optional. A dictionary of cookies to send to the specified url.Default None\n"
      "headers		Optional. A dictionary of HTTP headers to send to the specified url.Default None\n"
      "proxies		Optional. A dictionary of the protocol to the proxy url.Default None\n"
      "stream		Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).Default False\n"
      "timeout		Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.Default None which means the request will continue until the connection is closed\n"
      "verify	    Optional. A Boolean or a String indication to verify the servers TLS certificate or not.Default True")




print("\n\n\nEnd of the Python Requests Modules Showcase")

