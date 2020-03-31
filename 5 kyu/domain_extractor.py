'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

import re


def domain_name(url):
    if url:
        # Remove any characters before domain name
        before_domain_name = re.compile(r"https?://(www\.)?")
        url = before_domain_name.sub('', url).strip().strip('/')

        if url[0:4] == 'www.':
            url = url.strip('www.')

        # Remove '.com' and any characters that come after
        after_dot_com = re.compile((re.escape('.')+'.*'))
        url = after_dot_com.sub('', url)

    return url
