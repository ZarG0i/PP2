import json
import os

SETTINGS="settings.json"
SCORES="leaderboard.json"


def load_settings():

    if not os.path.exists(SETTINGS):
        return {
            "difficulty":"medium",
            "sound":True
        }

    with open(SETTINGS,"r") as f:
        return json.load(f)


def save_settings(settings):

    with open(SETTINGS,"w") as f:
        json.dump(settings,f)


def get_scores():

    if not os.path.exists(SCORES):
        return []

    with open(SCORES,"r") as f:
        return json.load(f)


def save_score(name,score,distance):

    scores=get_scores()

    scores.append({
        "name":name,
        "score":score,
        "distance":int(distance)
    })

    scores=sorted(
        scores,
        key=lambda x:x["score"],
        reverse=True
    )[:10]

    with open(SCORES,"w") as f:
        json.dump(scores,f)