import pynder
import sys
import os
import traceback
import logging
from beauty_predict import want_to_like
from beauty_predict import beauty_predict
from skimage.io import imread, imsave, imshow, show, imsave
import requests
import pynder.constants as constants
import json
import secret 

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(APP_ROOT)
parent_path = os.path.dirname(parent_path)

session = pynder.Session("damien.chailley",facebook_auth_token) #kwarg

headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    "content-type": "application/json",
    "User-agent": "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)",
    "Accept": "application/json"
}

def _request(methode, url):
  print(_session.headers);
  return _session.request(methode, url)


def like(user) :
  return _request("POST","https://api.gotinder.com/like/{}".format(user.get("_id"))).json()

def dislike(user) :
  return _request("POST","https://api.gotinder.com/pass/{}".format(user.get("_id"))).json()


_session = requests.Session()

_session.headers.update(headers)
_token = facebook_auth_token;

if _token is not None:
            _session.headers.update({"X-Auth-Token": str(_token)})


try:
  print("Fetching users...")

  users_json = _request("GET","https://api.gotinder.com/v2/recs/core").json()


  for item in users_json['data']['results']:
    name = "totoche"
    name = item.get("user")['name']; #recupère le nom.   
    print(name+"\n")

    # Fetch user profile picure
    image = imread(item.get("user")['photos'][0].get('url'))
    imsave(parent_path + "/samples/image/screen.jpg", image)
    print("picture saved succesfully ! :) \n");

    resultat = want_to_like("screen.jpg")

    if(resultat) :
      print("I want to like")
      print(format(item.get("user")))
      print(like(item.get("user")))
    else : 
      print("Nope")
      print(format(item.get("user")))
      print(dislike(item.get("user")))
except Exception as e:
  logging.error(traceback.format_exc())


