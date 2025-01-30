# Generate a short URL

# Map it to a long URL

# Short URL -> Long URL
import hashlib


my_urls = {}
urls = 1

def genShort():
    global urls

    key = hashlib.md5(str(urls).encode()).hexdigest()[:10]

    my_urls[str(key)] = None

    urls += 1
    return "https://shopi.fy/" + str(key)

def mapToLong(short, long):
    key = (short.split("/"))[-1]

    my_urls[key] = long

def getLong(short):
    key = (short.split("/"))[-1]

    if key in list(my_urls):
        return my_urls[key]
    else:
        return None


s = genShort()
mapToLong(s, "http://localhost")
assert(getLong(s) == "http://localhost")

t = genShort()
mapToLong(t, "http://shopify.com")
assert(getLong(t) == "http://shopify.com")