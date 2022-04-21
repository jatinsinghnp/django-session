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

               Session Methods

  get_session_cookie_age() - It returns the age of session cookies, in seconds. Defaults to
  SESSION_COOKIE_AGE.
  set expiry(value) It sets the expiration time for the session. You can pass a number of different
  values:
  If value is an integer, the session will expire after that many seconds of inactivity. For example,
  calling request.session.set_expiry(300) would make the session expire in 5 minutes.
  If value is a datetime or timedelta object, the session will expire at that specific date/time. Note that
  datetime and timedelta values are only serializable if you are using the PickleSerializer.
  If value is 0, the user's session cookie will expire when the user's Web browser is closed.
  If value is None, the session reverts to using the global session expiry policy.
  Reading a session is not considered activity for expiration purposes. Session expiration is computed
  from the last time the session was modified.
  Session Methods

get_expiry_age() - It returns the number of seconds until this session expires. For sessions with no
custom expiration (or those set to expire at browser close), this will equal
SESSION_COOKIE_AGE.
This function accepts two optional keyword arguments:
modification: last modification of the session, as a datetime object. Defaults to the current time.
expiry: expiry information for the session, as a datetime object, an int (in seconds), or Nne. Defaults
to the value stored in the session by set expiry(), if there is one, or None.
get_expiry_date() - It returns the date this session will expire. For sessions with no custom expiration
(or those set to expire at browser close), this will equal the date SESSION_COOKIE_AGE seconds
from now.
This function accepts the same keyword arguments as get_expiry_age().

Session Methods
get expire_at_browser_close() - It returns either True or False, depending on whether the user's

session cookie will expire when the user's Web browser is closed.
clear_expired() – It removes expired sessions from the session store. This class method is called by
clearsessions.

Session Methods
set test cookie() – It sets a test cookie to determine whether the user's browser supports cookies.
Due to the way cookies work, you won't be able to test this until the user's next page request.

test_cookie_worked() – It returns either True or False, depending on whether the user's browser
accepted the test cookie. Due to the way cookies work, you'll have to call set_test_cookie() on a
previous, separate page request.

delete_test_cookie() – It deletes the test cookie. Use this to clean up after yourself.

        #Session Settings
SESSION CACHE ALIAS - If you're using cache-based session storage, this selects the cache to
use. Default: 'default'
SESSION_COOKIE_AGE - The age of session cookies, in seconds. Default: 1209600 (2 weeks, in
seconds)
SESSION COOKIE DOMAIN - The domain to use for session cookies. Set this to a string such as
"example.com" for cross-domain cookies, or use None for a standard domain còokie.
Be cautious when updating this setting on a production site. If you update this setting to enable cross-
domain cookies on a site that previously used standard domain cookies, existing user cookies will be
set to the old domain. This may result in them being unable to log in as long as these cookies persist.
Default: None
