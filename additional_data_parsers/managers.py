import requests
from bs4 import BeautifulSoup

indices = {
    'Manchester City': '281', 'Liverpool FC': '31', 'Chelsea FC': '631', 'Manchester United': '985',
    'Tottenham Hotspur': '148', 'Arsenal FC': '11', 'Leicester City': '1003', 'Everton FC': '29', 'Aston Villa': '405',
    'Wolverhampton Wanderers': '543', 'West Ham United': '379', 'Newcastle United': '762', 'Leeds United': '399',
    'Southampton FC': '180', 'Crystal Palace': '873', 'Brighton &amp; Hove Albion': '1237', 'Brentford FC': '1148',
    'Norwich City': '1123', 'Burnley FC': '1132', 'Watford FC': '1010', 'AFC Bournemouth': '989', 'Fulham FC': '931',
    'Sheffield United': '350', 'West Bromwich Albion': '984', 'Stoke City': '512', 'Nottingham Forest': '703',
    'Middlesbrough FC': '641', 'Blackburn Rovers': '164', 'Millwall FC': '1028', 'Queens Park Rangers': '1039',
    'Swansea City': '2288', 'Huddersfield Town': '1110', 'Reading FC': '1032', 'Birmingham City': '337',
    'Preston North End': '466', 'Bristol City': '698', 'Cardiff City': '603', 'Derby County': '22',
    'Barnsley FC': '349', 'Hull City': '3008', 'Luton Town': '1031', 'Coventry City': '990', 'Blackpool FC': '1181',
    'Peterborough United': '1072', 'Sheffield Wednesday': '1035', 'Sunderland AFC': '289', 'Ipswich Town': '677',
    'Wigan Athletic': '1071', 'Rotherham United': '1194', 'Charlton Athletic': '358', 'Milton Keynes Dons': '991',
    'Wycombe Wanderers': '2805', 'Portsmouth FC': '1020', 'Oxford United': '988', 'Lincoln City': '1198',
    'Doncaster Rovers': '2454', 'Burton Albion': '2963', 'Bolton Wanderers': '355', 'Gillingham FC': '2814',
    'Plymouth Argyle': '2262', 'Crewe Alexandra': '1042', 'Cheltenham Town': '3371', 'Fleetwood Town': '11177',
    'Shrewsbury Town': '3054', 'Morecambe FC': '3697', 'AFC Wimbledon': '3884', 'Accrington Stanley': '3688',
    'Cambridge United': '986', 'Salford City': '34888', 'Mansfield Town': '3820', 'Swindon Town': '352',
    'Bristol Rovers': '2455', 'Colchester United': '1060', 'Tranmere Rovers': '1074', 'Northampton Town': '1302',
    'Bradford City': '1027', 'Oldham Athletic': '1078', 'Rochdale AFC': '1088', 'Carlisle United': '1220',
    'Barrow AFC': '6168', 'Stevenage FC': '3684', 'Crawley Town': '3537', 'Port Vale FC': '1211',
    'Leyton Orient': '1150', 'Walsall FC': '899', 'Scunthorpe United': '2964', 'Forest Green Rovers': '3455',
    'Exeter City': '6699', 'Hartlepool United': '2577', 'Newport County': '3716', 'Harrogate Town': '12020',
    'Sutton United': '3052',
}

lower_indices = {
    'Notts County': '1045', 'Woking FC': '2796', 'Barnet FC': '2804', 'Stockport County': '1098', 'Bromley FC': '8981',
    'Grimsby Town': '1034', 'Wealdstone FC': '4117', 'Aldershot Town': '3717', 'Eastleigh FC': '10391',
    'Southend United': '2793', 'Dover Athletic': '3936', 'Yeovil Town': '972', 'Wrexham AFC': '1112',
    'Dagenham &amp; Redbridge FC': '3696', 'Maidenhead United': '7123', 'FC Halifax Town': '1127',
    'Torquay United': '1218', 'Altrincham FC': '2962', "King's Lynn Town": '38899', 'Solihull Moors': '12335',
    'Boreham Wood FC': '3867', 'Chesterfield FC': '1219', 'Weymouth FC': '3822',
    'Welling United': '7454', 'Hemel Hempstead Town': '17980', 'Bath City': '1099', 'Dartford FC': '4074',
    'Havant &amp; Waterlooville FC': '2794', 'Concord Rangers': '29842', 'Billericay Town': '7067',
    'Dulwich Hamlet': '6169', 'Maidstone United': '7047', 'Oxford City': '22563', 'Ebbsfleet United': '2797',
    'Tonbridge Angels': '14672', 'Braintree Town': '6340', 'Chippenham Town': '21652', 'Chelmsford City': '3698',
    'Dorking Wanderers': '52299', 'Eastbourne Borough': '3713', 'Hampton &amp; Richmond Borough': '8820',
    'Hungerford Town': '29019', 'Slough Town': '11310', 'St Albans City': '3826',
    'Hereford FC': '46842', 'Gloucester City': '11407', 'Darlington FC': '37486', 'Kidderminster Harriers': '1195',
    'AFC Fylde': '22672', 'AFC Telford United': '3694', 'Boston United': '3489', 'Blyth Spartans': '4310',
    'Farsley Celtic': '3818', 'Southport FC': '9829', 'Brackley Town': '20877', 'Bradford (Park Avenue)': '7048',
    'Chorley FC': '13286', 'York City': '1252', 'Alfreton Town': '3721', 'Chester FC': '31367',
    'Curzon Ashton': '13556', 'Gateshead FC': '3456', 'Guiseley AFC': '12658', 'Kettering Town': '3825',
    'Leamington FC': '23226', 'Spennymoor Town': '45922'
}

indices.update(lower_indices)


def url(index):
    return f'https://www.transfermarkt.com/manchester-city/mitarbeiterhistorie/verein/{index}'


managers = []
for k, v in indices.items():
    print(k)
    page = requests.get(url(v), headers={'User-Agent': 'Custom'})

    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find(class_='items')
    table2 = table.find('tbody')
    table3 = table2.find_all('tr')
    for row in table3:
        try:
            d = dict()
            d['Team'] = k
            inline = row.find(class_='inline-table')
            d['Name'] = str(inline).split("title=\"")[1].split("\"/><")[0]
            d['Birthday'] = str(inline).split("</td></tr><tr><td>")[1].split("</td></tr>")[0]
            zentrierts = row.find_all(class_='zentriert')
            d['Country'] = str(zentrierts[0]).split("title=\"")[1].split("\"/><")[0]
            d['Start'] = str(zentrierts[1]).split('">')[1].split('</')[0]
            d['End'] = str(zentrierts[2]).split('">')[1].split('</')[0]
            managers.append(d)
        except Exception:
            continue

import csv

keys = managers[0].keys()

with open('../data/managers.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(managers)
