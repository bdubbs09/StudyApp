#!/usr/bin/python

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


#
#   REMEMBER TO REPLACE THE DEVELOPER KEY!
#   USE OAUTH INSTEAD OF MASTER KEY!
#
#

DEVELOPER_KEY = "AIzaSyDuX0Dw9XUlz4eZlNwqhf-rkVwNIdXifXU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []
  channels = []
  playlists = []


  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))
  return videos, channels, playlists



def youtube_request(video_suggestion):
  argparser.add_argument("--q", help="Search term", default= video_suggestion)
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

  try:
    return youtube_search(args)
  except HttpError, e:
    return "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

video_suggestion = "discrete math"
video_results, channel_results, playlist_results = youtube_request(video_suggestion)
print "\nVideos:"
for vid in video_results:
  print vid

print "\nChannels:"
for channel in channel_results:
  print channel

print "\nPlaylists:"
for playlist in playlist_results:
  print playlist