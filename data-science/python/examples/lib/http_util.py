import urllib

def get(url):
    response = urllib.urlopen(url)
    if response.getcode() == 200:
        response_body = response.read().decode('utf-8')
        return response_body
    else:
        log.info("UNSUCCESSFUL HTTP get %s %s %s" % (url, response.getcode(), response.read()))
        return None
