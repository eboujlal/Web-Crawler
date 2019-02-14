from urllib.parse import urlparse

# Manage subdomaines ...
def get_sub_domaine_name(url):
    try : 
        return urlparse(url).netloc
    except :
        return ''

# Manage Domaine
def get_domaine_name(url):
    try : 
        results = get_sub_domaine_name(url).split('.')
        return results[-2]+'.'+results[-1]
    except :
        return ''

