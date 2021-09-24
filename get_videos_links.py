import requests_html as rqhtml

session = rqhtml.HTMLSession()
def get_videos_links_of_youtube_playlist(link):
    r = session.get(link)
    r.html.render(timeout=200)
    a_tags = r.html.find("a#video-title")
    links = ["https://www.youtube.com"+a_tag.attrs.get("href") for a_tag in a_tags]
    return links