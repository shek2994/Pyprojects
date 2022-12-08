import pytube

def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag

def input_links1():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links

def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = ['https://www.youtube.com/watch?v=OW7An1moxL4"', 
    #         'https://www.youtube.com/watch?v=WXNKQ_otO_g&list=PLSNNzog5eydtwsdT__t5WtRgvpfMzpTc7&index=7"', 
    #         'https://www.youtube.com/watch?v=UbMlPIgzTxc&list=PLSNNzog5eydtwsdT__t5WtRgvpfMzpTc7&index=2"', 
    #         'https://www.youtube.com/watch?v=XrZxJsKUQR8"', 
    #         'https://www.youtube.com/watch?v=6SHnmho7zCs&t=656s"', 
    #         'https://www.youtube.com/watch?v=sER3W_ChuNQ"', 
    #         'https://www.youtube.com/watch?v=-3Uq_FZkzpc"', 
    #         'https://www.youtube.com/watch?v=fKl2JW_qrso"', 
    #         'https://www.youtube.com/watch?v=lhiH-6ygGl8&list=PLS1QulWo1RIYt4e0WnBp-ZjCNq8X0FX0J&index=37"', 
    #         'https://www.youtube.com/watch?v=FsAPt_9Bf3U"', 
    #         'https://www.youtube.com/watch?v=16FI1-d2P4E"', 
            'https://www.youtube.com/watch?v=9G0hvmPbvmk&list=PLS1QulWo1RIYt4e0WnBp-ZjCNq8X0FX0J&index=48"', 
            'https://www.youtube.com/watch?v=5bRDpzdcuf8&list=PLS1QulWo1RIYt4e0WnBp-ZjCNq8X0FX0J&index=51"', 
            'https://www.youtube.com/watch?v=dDCiiVRhWUc"', 
            'https://www.youtube.com/watch?v=BpJCAafw2qE"', 
            'https://www.youtube.com/watch?v=kN1Czs0m1SU"', 
            'https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw"', 
            'https://www.youtube.com/watch?v=bFtkHJy9kIU"', 'https://www.youtube.com/watch?v=KwUY2fZ04Bg"', 'https://www.youtube.com/watch?v=3ohzBxoFHAY"', 'https://www.youtube.com/watch?v=HGOBQPFzWKo"', 'https://www.youtube.com/watch?v=8OpMAlYyH5Y&list=PLea0WJq13cnB_ORdGzEkPlZEN20TSt6Lx&index=11"', 'https://www.youtube.com/watch?v=_I0U1sZ9RJ8"', 'https://www.youtube.com/"', 'https://www.youtube.com/watch?v=n-e1FDAtBuM"', 'https://www.youtube.com/watch?v=xAPHzRdWX0g&t=0s"', 'https://www.youtube.com/watch?v=uNmJppc-gR8"', 'https://www.youtube.com/watch?v=rC6uR9gR6w4"', 'https://www.youtube.com/watch?v=uNmJppc-gR8&list=WL&index=2&t=596s"', 'https://www.youtube.com/watch?v=zUnrLHbYmKA"', 'https://www.youtube.com/watch?v=xr_aZ4DrkHQ"', 'https://www.youtube.com/watch?v=p6Q2-m9i4Fg"', 'https://www.youtube.com/watch?v=URsSTw5nUVM"', 'https://www.youtube.com/watch?v=cLXsH6lpWMo"', 'https://www.youtube.com/watch?v=ttBjf4bMDXY"', 'https://www.youtube.com/watch?v=XXPNpdaK9WA"', 'https://www.youtube.com/watch?v=ou1ynsJxRLA"', 'https://www.youtube.com/watch?v=zfLc45RQ9Zk"', 'https://www.youtube.com/watch?v=1-awqIzgdUA"', 'https://www.youtube.com/watch?v=3tP3lT5y-QA"', 'https://www.youtube.com/watch?v=Kqea4PA-xkw"', 'https://www.youtube.com/watch?v=9b5TO7drqqE"', 'https://www.youtube.com/watch?v=lgugpeE8nz0"', 'https://www.youtube.com/watch?v=ZDa-Z5JzLYM"', 'https://www.youtube.com/watch?v=BJ-VvGyQxho"', 'https://www.youtube.com/watch?v=rq8cL2XMM5M"', 'https://www.youtube.com/watch?v=tY5Sw2YDVpI"', 'https://www.youtube.com/watch?v=z_DRMA2jpYU"', 'https://www.youtube.com/playlist?list=PLRqwX-V7Uu6Zy51Q-x9tMWIv9cueOFTFA"', 'https://www.youtube.com/channel/UC8aFE06Cti9OnQcKpl6rDvQ"', 'https://www.youtube.com/watch?v=E45v2dD3IQU"', 'https://www.youtube.com/watch?v=_5T70cAXDJ0&t=1s"', 'https://www.youtube.com/watch?v=lVsP8yjf3H4"', 'https://www.youtube.com/watch?v=F4kT_xHDHwA"', 'https://www.youtube.com/watch?v=6fPGvmBHifM"', 'https://www.youtube.com/watch?v=vZr9LEIWOsA"', 'https://www.youtube.com/watch?v=YAz0qJf05ko"', 'https://www.youtube.com/watch?v=bTj0vFs8ndI"', 'http://www.youtube.com/watch?v=EPYupizJYQI"', 'https://www.youtube.com/watch?v=7aDjYqOMu9w"', 'https://www.youtube.com/watch?v=Zn8mEZXr6nE"', 'https://www.youtube.com/watch?v=ReKzEGLlGfk"', 'https://www.youtube.com/watch?v=pTB30aXS77U"']

    # links.pop()

    return links