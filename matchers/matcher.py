import pandas as pd


managers = pd.read_csv('../data/managers.csv')
england = pd.read_csv('../england-league-two.csv')

managers_team = set(list(managers['Team']))
homes_team = set(list(england['home_team']))

matches = {
  "Huddersfield":  "Huddersfield Town",
  "Middlesbrough":  "Middlesbrough FC",
  "West Ham":  "West Ham United",
  "Tottenham":  "Tottenham Hotspur",
  "Stoke": "Stoke City",
  "Sunderland":  "Sunderland AFC",
  "Leicester":  "Leicester City",
  "Hull": "Hull City",
  "Sheffield Utd":  "Sheffield United",
  "Cardiff":  "Cardiff City",
  "Wolves":  "Wolverhampton Wanderers",
  "Swansea":  "Swansea City",
  "Fulham":  "Fulham FC",
  "Brighton": "Brighton &amp; Hove Albion",
  "Chelsea":  "Chelsea FC",
  "West Brom":  "West Bromwich Albion",
  "Norwich":  "Norwich City",
  "Watford":  "Watford FC",
  "Manchester Utd":  "Manchester United",
  "Newcastle":  "Newcastle United",
  "Brentford":  "Brentford FC",
  "Leeds":  "Leeds United",
  "Arsenal":  "Arsenal FC",
  "Burnley":  "Burnley FC",
  "Southampton":  "Southampton FC",
  "Everton": "Everton FC",
  "Liverpool":  "Liverpool FC",
  "Bournemouth": "AFC Bournemouth",
  "Ipswich": "Ipswich Town",
  "Coventry": "Coventry City",
  "Barnsley": "Barnsley FC",
  "Reading": "Reading FC",
  "Rotherham": "Rotherham United",
  "Blackpool": "Blackpool FC",
  "Burton": "Burton Albion",
  "Peterborough": "Peterborough United",
  "Sheffield Wed": "Sheffield Wednesday",
  "Nottingham": "Nottingham Forest",
  "Blackburn": "Blackburn Rovers",
  "Luton": "Luton Town",
  "Preston": "Preston North End",
  "Charlton": "Charlton Athletic",
  "Bolton": "Bolton Wanderers",
  "Wigan": "Wigan Athletic",
  "Wycombe": "Wycombe Wanderers",
  "QPR": "Queens Park Rangers",
  "Birmingham": "Birmingham City",
  "Millwall": "Millwall FC",
  "Derby": "Derby County",
  "Chesterfield": "Chesterfield FC",
  "Gillingham": "Gillingham FC",
  "Crewe": "Crewe Alexandra",
  "Rochdale": "Rochdale AFC",
  "Oxford Utd": "Oxford United",
  "Doncaster": "Doncaster Rovers",
  "Oldham": "Oldham Athletic",
  "Cheltenham": "Cheltenham Town",
  "Plymouth": "Plymouth Argyle",
  "Port Vale": "Port Vale FC",
  "MK Dons": "Milton Keynes Dons",
  "Morecambe": "Morecambe FC",
  "Swindon": "Swindon Town",
  "Lincoln": "Lincoln City",
  "Portsmouth": "Portsmouth FC",
  "Southend": "Southend United",
  "Walsall": "Walsall FC",
  "Accrington": "Accrington Stanley",
  "Scunthorpe": "Scunthorpe United",
  "Fleetwood": "Fleetwood Town",
  "Northampton": "Northampton Town",
  "Tranmere": "Tranmere Rovers",
  "Cambridge Utd": "Cambridge United",
  "Shrewsbury": "Shrewsbury Town",
  "Bury": "Bury AFC",
  "Exeter": "Exeter City",
  "Colchester": "Colchester United",
  "Sutton": "Sutton United",
  "Macclesfield": "Macclesfield FC",
  "Barrow": "Barrow AFC",
  "Notts Co": "Notts County",
  "Yeovil": "Yeovil Town",
  "Harrogate": "Harrogate Town",
  "Crawley": "Crawley Town",
  "Newport": "Newport County",
  "Carlisle": "Carlisle United",
  "Barnet": "Barnet FC",
  "Forest Green": "Forest Green Rovers",
  "Grimsby": "Grimsby Town",
  "Salford": "Salford City",
  "Stevenage": "Stevenage FC",
  "Mansfield": "Mansfield Town",
  "Hartlepool": "Hartlepool United",
}


for i, row in england.iterrows():
    if row['home_team'] in matches:
        england.at[i, 'home_team'] = matches.get(row['home_team'])
    if row['away_team'] in matches:
        england.at[i, 'away_team'] = matches.get(row['away_team'])


managers_team = set(list(managers['Team']))
homes_team = set(list(england['home_team']))

for home_team in homes_team:
    if home_team not in managers_team:
        print(home_team)


england.to_csv('england-league-two_v1.1.csv', index=False)
