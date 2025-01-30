import hashlib
import csv

urls = 1

def genShort():
    global urls

    key = hashlib.md5(str(urls).encode()).hexdigest()[:10]

    urls += 1
    return "https://shopi.fy/" + str(key)

def mapToLong(short, long):
    key = (short.split("/"))[-1]

    # TODO: error check commas
    # TODO: overwrite
    f = open("urls.csv", "a")
    writer = csv.writer(f)
    writer.writerow([key, long])
    f.close()

def getLong(short):
    key = (short.split("/"))[-1]

    f = open("urls.csv", "r")
    reader = csv.reader(f)

    out = None

    for lines in reader:
        if lines[0] == key:
            out = lines[1]
            break

    f.close()
    return out





s = genShort()
mapToLong(s, "http://localhost")
assert(getLong(s) == "http://localhost")

t = genShort()
mapToLong(t, "http://shopify.com")
assert(getLong(t) == "http://shopify.com")