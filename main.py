import youtube_download
import convert
import os
import pytube
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

print("(1) Download a video\n(2) Download a playlist\n(3) Download a MP3s\n(4) Download a playlist and save as MP3s")
choice = input()

if choice == "1" or choice == "2":
    print("Please choose a quality low(360p) // medium (720p) // high (1080p)")
    quality = input()
    if choice == "1":
        links = youtube_download.input_links()
        for link in links:
            youtube_download.download_video(link, quality)
            print("Done")
    if choice == "2":
        print("Enter the link to the playlist")
        link = input()
        youtube_download.download_playlist(link, quality)
        print("Done")
elif choice == "3":
    links = youtube_download.input_links()
    for link in links:
        filename = youtube_download.download_video(link, 'low')
        convert.convert_to_mp3(filename)
        os.remove(filename)
        print("Done")
elif choice == "4":
    print("Enter the link to the playlist")
    link = input()
    playlist = pytube.Playlist(link)
    for url in playlist.video_urls:
        filename = youtube_download.download_video(url, 'low')
        convert.convert_to_mp3(filename)
        os.remove(filename)
    print("Done")
else:
    print("Invalid input! Terminating...")