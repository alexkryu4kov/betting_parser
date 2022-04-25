from dataclasses import dataclass


@dataclass
class MatchInfo:
    date: str
    time: str
    country: str
    league: str
    home_team: str
    away_team: str
    home_win_rate: float
    draw_rate: float
    away_win_rate: float
    home_double_chance_rate: float
    away_double_chance_rate: float
    no_draw_rate: float
    total_over_1_rate: float
    total_under_1_rate: float
    total_over_15_rate: float
    total_under_15_rate: float
    total_over_2_rate: float
    total_under_2_rate: float
    total_over_25_rate: float
    total_under_25_rate: float
    total_over_3_rate: float
    total_under_3_rate: float
    total_over_35_rate: float
    total_under_35_rate: float
    both_team_to_score_yes: float
    both_team_to_score_no: float
    link: str
    home_handicap_0: float
    away_handicap_0: float
    home_handicap_minus_15: float
    away_handicap_minus_15: float
    home_handicap_minus_1: float
    away_handicap_minus_1: float
    home_handicap_plus_15: float
    away_handicap_plus_15: float
    home_handicap_plus_1: float
    away_handicap_plus_1: float
    home_first_half_handicap_0: float
    away_first_half_handicap_0: float
    home_first_half_handicap_minus_15: float
    away_first_half_handicap_minus_15: float
    home_first_half_handicap_minus_1: float
    away_first_half_handicap_minus_1: float
    home_first_half_handicap_plus_15: float
    away_first_half_handicap_plus_15: float
    home_first_half_handicap_plus_1: float
    away_first_half_handicap_plus_1: float
    home_second_half_handicap_0: float
    away_second_half_handicap_0: float
    home_second_half_handicap_minus_15: float
    away_second_half_handicap_minus_15: float
    home_second_half_handicap_minus_1: float
    away_second_half_handicap_minus_1: float
    home_second_half_handicap_plus_15: float
    away_second_half_handicap_plus_15: float
    home_second_half_handicap_plus_1: float
    away_second_half_handicap_plus_1: float
    home_first_half_win_rate: float
    draw_first_half_rate: float
    away_first_half_win_rate: float
    home_second_half_win_rate: float
    draw_second_half_rate: float
    away_second_half_win_rate: float
    home_double_chance_first_half_rate: float
    away_double_chance_first_half_rate: float
    no_draw_first_half_rate: float
    home_double_chance_second_half_rate: float
    away_double_chance_second_half_rate: float
    no_draw_second_half_rate: float
    total_first_half_over_05_rate: float
    total_first_half_under_05_rate: float
    total_first_half_over_1_rate: float
    total_first_half_under_1_rate: float
    total_first_half_over_15_rate: float
    total_first_half_under_15_rate: float
    total_first_half_over_2_rate: float
    total_first_half_under_2_rate: float
    total_second_half_over_05_rate: float
    total_second_half_under_05_rate: float
    total_second_half_over_1_rate: float
    total_second_half_under_1_rate: float
    total_second_half_over_15_rate: float
    total_second_half_under_15_rate: float
    total_second_half_over_2_rate: float
    total_second_half_under_2_rate: float
    both_team_to_score_first_half_yes: float
    both_team_to_score_first_half_no: float
    both_team_to_score_second_half_yes: float
    both_team_to_score_second_half_no: float
    odd: float
    even: float
    odd_first: float
    odd_second: float
    even_first: float
    even_second: float
    correct_score10: float
    correct_score20: float
    correct_score21: float
    correct_score30: float
    correct_score31: float
    correct_score32: float
    correct_score40: float
    correct_score41: float
    correct_score00: float
    correct_score11: float
    correct_score22: float
    correct_score33: float
    correct_score01: float
    correct_score02: float
    correct_score12: float
    correct_score03: float
    correct_score13: float
    correct_score23: float
    correct_score04: float
    correct_score14: float
    home_home: float
    home_draw: float
    home_away: float
    draw_home: float
    draw_draw: float
    draw_away: float
    away_home: float
    away_draw: float
    away_away: float


@dataclass
class ResultMatchInfo:
    home_scored: int
    away_scored: int
    home_first_half_scored: int
    away_first_half_scored: int
    home_second_half_scored: int
    away_second_half_scored: int


@dataclass
class Info:
    match_info: MatchInfo
    result: ResultMatchInfo
