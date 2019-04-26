def movie_urls(links_urls):
    url_list = []
    for i in links_urls:
        url_split = i.split('?')
        for e in url_split:
            if e.startswith('https'):
                url_list.append(e)
            else:
                pass
    return url_list