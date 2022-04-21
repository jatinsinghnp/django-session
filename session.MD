                    # Session
The session framework lets you store and retrieve arbitrary data on a per-site-visitor basis.
It stores data on the server side and abstracts the sending and receiving of cookies. Cookies contain a
session ID not the data itself.
By default, Django stores sessions in your database.
As it stores sessions in database so it is mandatory to run makemigrations and migrate to use session.
It will create required tables.
The Django sessions framework is entirely, and solely, cookie-based.
django.contrib.sessions.middleware.SessionMiddleware
django.contrib.sessions

             #Session
database-backed sessions - If you want to use a database-backed session, you need to add
'django.contrib.sessions' to your INSTALLED_APPS setting.
Once you have configured your installation, run manage.py migrate to install the single database
table that stores session data.
file-based sessions - To use file-based sessions, set the SESSION ENGINE setting to
"django.contrib.sessions.backends.file".
You might also want to set the SESSION_FILE_PATH setting (which defaults to output from
tempfile.gettempdir(), most likely /tmp) to control where Django stores session files. Be sure to
check that your Web server has permissions to read and write to this location.
cookie-based sessions - To use cookies-based sessions, set the SESSION_ENGINE setting to
"django.contrib.sessions.backends.signed_cookies". The session data will be stored using Django's
tools for cryptographic signing and the SECRET_KEY setting.

                    Session
cached sessions For better performance, you may want to use a cache-based session backend. To
store session data using Django's cache system, you'll first need to make sure you’ve configured
your cache.


                Using sessions in views
When Session Middleware is activated, each HttpRequest object, the first argument to any Django
view function will have a session attribute, which is a dictionary-like object.
You can read it and write to request.session at any point in your view. You can edit it multiple times.
# Set Item
request.session['key'] = 'value'
# Get Item
returned_value = request.session['key']
# Delete Item
del request.session['key']
This raises KeyError if the given key isn't already in the session.
# Contains
'key' in request.session

           Session Methods
keys() method returns a view object that displays a list of all the keys in the dictionary.
Syntax:- dict.keys()
items() method returns the list with all dictionary keys with values.
Syntax:- dict.items()
clear() function is used to erase all the elements of list. After this operation, list becomes empty.
Syntax:- dict.clear()
setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a
value to the dictionary.

      Session Methods
- It deletes the current session data from the session and deletes the session cookie. This is
flush() -
used if you want to ensure that the previous session data can't be accessed again from the user's
browser (for example, the django.contrib.auth.logout() function calls it).
