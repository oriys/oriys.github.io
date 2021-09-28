from bs4 import BeautifulSoup
import requests
import os
books = list(set([
    "https://book.douban.com/subject/26835090",
    "https://book.douban.com/subject/34907497",
    "https://book.douban.com/subject/1899158",
    "https://book.douban.com/subject/27096665",
    "https://book.douban.com/subject/27087564",
    "https://book.douban.com/subject/35390390",
    "https://book.douban.com/subject/35296788",
    "https://book.douban.com/subject/35016085",
    "https://book.douban.com/subject/33404959",
    "https://book.douban.com/subject/3211779",
    "https://book.douban.com/subject/34994608",
    "https://book.douban.com/subject/34998167",
    "https://book.douban.com/subject/1012611",
    "https://book.douban.com/subject/30264678",
    "https://book.douban.com/subject/26348596",
    "https://book.douban.com/subject/30329536",
    "https://book.douban.com/subject/4913064",
    "https://book.douban.com/subject/1029791",
    "https://book.douban.com/subject/24708143",
    "https://book.douban.com/subject/26369699",
    "https://book.douban.com/subject/34998167"
    "https://book.douban.com/subject/30280001",
    "https://book.douban.com/subject/26877752",
    "https://book.douban.com/subject/35016085",
    "https://book.douban.com/subject/25900403"]))
movies = list(set(
    ["https://movie.douban.com/subject/26774749",
     "https://movie.douban.com/subject/26720121",
     "https://movie.douban.com/subject/4851891",
     "https://movie.douban.com/subject/30458820",
     "https://movie.douban.com/subject/34812928",
     "https://movie.douban.com/subject/30337388",
     "https://movie.douban.com/subject/35576386",
     "https://movie.douban.com/subject/27138615",
     "https://movie.douban.com/subject/26741632",
     "https://movie.douban.com/subject/30331432",
     "https://movie.douban.com/subject/30367642",
     "https://movie.douban.com/subject/26613692",
     "https://movie.douban.com/subject/34953711",
     "https://movie.douban.com/subject/6748086",
     "https://movie.douban.com/subject/27186493",
     "https://movie.douban.com/subject/35076714",
     "https://movie.douban.com/subject/30513783",
     "https://movie.douban.com/subject/35161255",
     "https://movie.douban.com/subject/35235594",
     "https://movie.douban.com/subject/34845781"]))

urls = books+movies


def download(img, url):
    if not os.path.isfile('/Users/ezra/oriys/static/douban/'+img):
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8'
        }
        html = requests.request("GET", url, headers=headers).text
        soup = BeautifulSoup(html, 'html.parser')
        main_img = soup.select('#mainpic > a > img')[0]
        os.system('curl '+main_img['src']+' --output ' +
                  '/Users/ezra/oriys/static/douban/'+img)


if __name__ == '__main__':
    col = 8
    print('|'*(col-0))
    print(*['|' for i in range(col)], sep=':-:')
    i = 0
    while i < len(urls):
        j = i
        tmp = []
        lines = urls[i:i+col]
        for line in lines:
            img = line.split('/')[-1]
            download(img, line)
            n = f'[![{img}](../../douban/{img})]({line})'
            tmp.append(n)
        print(*tmp, sep='|', end='|')
        print()
        i += col
