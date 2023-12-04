import pandas as pd
pd.set_option('display.max_columns', None)

leagues = [ "FIFA World Cup",
    "Serie A",
    "Ligue 1",
    "La Liga",
    "Premier League",
    "Bundesliga",
    "Eredivisie",
    "Austrian Football Bundesliga",
    "Belgian Pro League",
    "Campeonato Brasileiro Série A",
    "Liga MX",
    "Primeira Liga",
    "Major League Soccer",
    "UEFA Champions League"]

leagues2 = [
    "Serie A",
    "Ligue 1",
    "La Liga",
    "Premier League",
    "Bundesliga",
    "FIFA World Cup",
    "UEFA Champions League"
]

import soccerdata as sd

fbref = sd.FBref(leagues=leagues2, seasons=2022)
read_leagues = fbref.read_leagues()
read_leagues_clean = read_leagues[["country"]]
read_leagues_clean.to_csv("leagues.csv")

read_teams = fbref.read_team_season_stats(stat_type="misc")
read_teams = read_teams[[]]
read_teams.to_csv("teams.csv")

read_matches = fbref.read_team_match_stats(stat_type="shooting")
read_matches = read_matches[["date", "opponent", "round", "venue", "GF", "GA"]]
read_matches.to_csv("matches.csv")

read_players = fbref.read_player_season_stats(stat_type="standard")
read_players = read_players[["nation", "pos"]]
read_players.to_csv("players.csv")

read_appearances = fbref.read_player_match_stats(stat_type="summary")
selected_columns = [("min", ""), ("Performance", "Gls"), ("Performance", "Ast"), ("Performance", "PK"), ("Performance", "PKatt"), ("Performance", "CrdY"), ("Performance", "CrdR"), ("Expected", "xG"), ("Expected", "npxG"), ("Expected", "xAG")]
read_appearances = read_appearances[selected_columns]
read_appearances.to_csv("appearances.csv")

read_shots = fbref.read_shot_events()
read_shots.to_csv("shots.csv")
