from pytube import YouTube
from pytube.cli import on_progress
import os
import pytube.request
import requests
from get_videos_links import get_videos_links_of_youtube_playlist
from asking_questions_on_terminal import ask_q_multiple_choices_on_terminal, ask_q_num_on_terminal
pytube.request.default_range_size = 1048576


# using selenium
# from get_videos_links_using_selenium import get_videos_links_of_playlist
# def get_links(link):
#     return get_videos_links_of_playlist(link)


# using requests-html
def get_links(link):
    print("Please Wait Till We Get The Links Of Your Videos")
    links = get_videos_links_of_youtube_playlist(link)
    print("We Got Your Links Successfully")
    return links


def create_dist_folder(dir):
    # creating the dist directory
    try:
        os.mkdir(dir)
    except FileExistsError:
        print(f"'{dir}' folder already exists")
    except Exception as e:
        print(e)


def beautify_filename(filename: str):
    not_allowed_symbols = ["|", ">", "<", "@",
                           "$",  "*", "%", "#", "!", "/", "\\", "{", "}", '"',":"]
    for symbol in not_allowed_symbols:
        filename = filename.replace(symbol, "")

    return filename


def download(link, dir, **kwargs):
    try:
        # pass
        yt = YouTube(link, on_progress_callback=on_progress)
    except:
        print("Connection Error")

    d_video = yt.streams.filter(mime_type='video/mp4').get_highest_resolution()
    if kwargs.get("id_"):
        id_ = kwargs.get("id_")
        filename = str(id_) + " - " + beautify_filename(yt.title)+".mp4"
        print("downloading  >> \t", filename)
        d_video.download(dir, filename=filename)
    else:
        print("there is no filename")
        d_video.download(output_path=dir)


def download_video(link, dir):
    create_dist_folder(dir)
    download(link, dir)


def ask_q_multiple_choices_on_terminal(question, choices):
    answer_text = ""
    for id_, choice in enumerate(choices):
        if id_ == 0:
            answer_text += "(" + choice + "/"
        elif id_ == len(choices)-1:
            answer_text += choice + ")"
        else:
            answer_text += choice+"/"
    answer = input(question+" "+answer_text)
    while not(answer in choices):
        answer = input(question+" "+answer_text)
    return answer


def download_playlist(link, dir):
    create_dist_folder(dir)
    videos_links = get_links(link)
    print(f"Your Playlist Containing {len(videos_links)} videos")
    specify_group_of_videos_answer = ask_q_multiple_choices_on_terminal(
        "Do You Want To Specify Group Of Videos To Download ?", choices=["y", "n"])
    starting_video, ending_video = None,None
    if specify_group_of_videos_answer == "y":
        starting_video = ask_q_num_on_terminal(
            "Which Video Do You Want To Start With ?", len(videos_links))
        ending_video = ask_q_num_on_terminal(
            "Which Video Do You Want To End With ?", len(videos_links))

    for id_, video_link in enumerate(videos_links):
        id_ += 1
        if specify_group_of_videos_answer == "y":
            if id_ >= starting_video and id_ <= ending_video:
                # print("downloading " + str(id_))
                download(video_link, dir, id_=id_)
        else:
            # print("downloading " + str(id_))
            download(video_link, dir, id_=id_)


playlist_link = input("Enter Playlist Link\t\t")
directory = input("Enter Directory \t\t")
download_playlist(playlist_link, directory)

# https://www.youtube.com/playlist?list=PL96AE8D9C68FEB902
# /media/abdo/Main Partition/school/5th/math/differential equation
