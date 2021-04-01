import requests

_API_PATH = 'https://nginx-helsinki-searchapi-master.ch.amazee.io/contacts'

def _collect( query ):

    ## todo: limit could provide more information on boundaries

    page = 1
    content = []

    while True:

        query['page'] = page

        r = requests.get( _API_PATH , params = query )
        data = r.json()
        content += data['hydra:member']

        page += 1

        if len( content ) >= data['hydra:totalItems']:
            break

    return content

def _clean_output( results, lang = 'en' ):

    for item in results:

        for key, value in item.copy().items():

            print( key )

            if key.startswith('@'):
                del item[key]

            ## todo: clean json more
            if isinstance( value, list ):
                item[key] = _clean_output( value, lang = lang )

            if isinstance( value, dict ):

                ## todo: some manually constructed special cases
                if key in ['title']:
                    value = value['name']

                if lang in value:
                    item[key] = value[lang]

    return results


def search( search, lang = 'en' ):
    search_results = _collect( {'search': search } )
    return _clean_output( search_results )[0]

def by_organisation( organisations = [], lang = 'en' ):

    ## todo: we should be able to collect them all in one query

    ret = []

    for org in organisations:

        query = { 'organizations.id[]' : org }
        ret += _collect( query )

    return _clean_output( ret )
