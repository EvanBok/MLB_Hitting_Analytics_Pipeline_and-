import requests
import pandas as pd
from datetime import date
import os

team_abbrev = {
    "Arizona Diamondbacks": "ARI",
    "Atlanta Braves": "ATL",
    "Baltimore Orioles": "BAL",
    "Boston Red Sox": "BOS",
    "Chicago Cubs": "CHC",
    "Chicago White Sox": "CWS",
    "Cincinnati Reds": "CIN",
    "Cleveland Guardians": "CLE",
    "Colorado Rockies": "COL",
    "Detroit Tigers": "DET",
    "Houston Astros": "HOU",
    "Kansas City Royals": "KC",
    "Los Angeles Angels": "LAA",
    "Los Angeles Dodgers": "LAD",
    "Miami Marlins": "MIA",
    "Milwaukee Brewers": "MIL",
    "Minnesota Twins": "MIN",
    "New York Mets": "NYM",
    "New York Yankees": "NYY",
    "Oakland Athletics": "OAK",
    "Philadelphia Phillies": "PHI",
    "Pittsburgh Pirates": "PIT",
    "San Diego Padres": "SD",
    "San Francisco Giants": "SF",
    "Seattle Mariners": "SEA",
    "St. Louis Cardinals": "STL",
    "Tampa Bay Rays": "TB",
    "Texas Rangers": "TEX",
    "Toronto Blue Jays": "TOR",
    "Washington Nationals": "WSH",
    "Athletics": "ATH"
}

def get_all_hitter_stats():
    url = "https://statsapi.mlb.com/api/v1/stats"
    params = {
        "stats": "season",
        "group": "hitting",
        "season": date.today().year,
        "limit": 300,
        "offset": 0,
        "playerPool": "ALL"
    }
    response = requests.get(url, params=params)
    data = response.json()
    rows = []
    for player in data["stats"][0]["splits"]:
        stat = player["stat"]
        rows.append({
            "player": player["player"]["fullName"],
            "team": player["team"]["name"],
            "team_abbrev": team_abbrev.get(player["team"]["name"], player["team"]["name"]),
            "avg": stat.get("avg"),
            "hits": stat.get("hits"),
            "homeRuns": stat.get("homeRuns"),
            "rbi": stat.get("rbi"),
            "stolenBases": stat.get("stolenBases"),
            "obp": stat.get("obp"),
            "slg": stat.get("slg"),
            "ops": stat.get("ops"),
            "atBats": stat.get("atBats"),
            "plateAppearances": stat.get("plateAppearances"),
            "strikeOuts": stat.get("strikeOuts"),
            "baseOnBalls": stat.get("baseOnBalls"),
            "gamesplayed": stat.get("gamesPlayed"),
            "PlayerID": player["player"]["id"],
             "scrape_date": date.today()
        })
    return rows

all_hitters = get_all_hitter_stats()
hitters_df = pd.DataFrame(all_hitters)
hitters_df.to_csv("/Users/evanbok/mlb-dashboard/mlb_all_hitters.csv", mode="w", index=False)
print(f"Done! Saved {len(hitters_df)} hitters")

#API used: https://statsapi.mlb.com/api/v1/stats?stats=season&group=hitting&season=2026&limit=10&playerPool=ALL
#run key: runhitters