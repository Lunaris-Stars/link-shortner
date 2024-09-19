import requests



def short_link(full_link, link_name):
    api_key = "db241238dda854e210b3c34bd9436b0c8bceb"
    base_url = "https://cutt.ly/api/api.php"
    
    payload = {"key":api_key, "short":full_link, "name":link_name}
    
    request = requests.get(base_url, params=payload)
    data = request.json()
    
    print('')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        
        print('title:', title)
        print('link:', short_link)
    except:
        status = data['url']['status']
        print('error status:', status)

link = input("Enter the link: ")
name = input('Give your link a name: ')

short_link(link, name)