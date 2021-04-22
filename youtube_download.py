import pytube

def download_video(url, resolution):
    tag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(tag)
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
    else:
        itag = 18
    return itag


def input_links():
    print("Enter the links of the videos (terminate by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop" and link !="Stop":
        link = input()
        links.append(link)

    links.pop()

    return links