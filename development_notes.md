# Note about normalisation

NB : For a good normalising, we need a good knowledge of the domain and the different uses of the data
Early normalisation can be counter-productive.

Obvious data split :
- Tournament
  - Location = Venue of tournament
  - Tournament = Name of tounament (including sponsor if relevant)
  - Series = Name of ATP tennis series (Grand Slam, Masters, International or International Gold)
  - Tier = Tier (tournament ranking) of WTA tennis series.
  - Court = Type of court (outdoors or indoors)
  - Surface = Type of surface (clay, hard, carpet or grass)
  - Best of = Maximum number of sets playable in match
- Match
  - Date = Date of match (note: prior to 2003 the date shown for all matches played in a single tournament is the start date)
  - Round = Round of match
  - Winner = Match winner
  - Loser = Match loser
  - WRank = ATP Entry ranking of the match winner as of the start of the tournament
  - LRank = ATP Entry ranking of the match loser as of the start of the tournament
  - WPts = ATP Entry points of the match winner as of the start of the tournament
  - LPts = ATP Entry points of the match loser as of the start of the tournament
  - W1 = Number of games won in 1st set by match winner
  - L1 = Number of games won in 1st set by match loser
  - W2 = Number of games won in 2nd set by match winner
  - L2 = Number of games won in 2nd set by match loser
  - W3 = Number of games won in 3rd set by match winner
  - L3 = Number of games won in 3rd set by match loser
  - W4 = Number of games won in 4th set by match winner
  - L4 = Number of games won in 4th set by match loser
  - W5 = Number of games won in 5th set by match winner
  - L5 = Number of games won in 5th set by match loser
  - Comment = Comment on the match (Completed, won through retirement of loser, or via Walkover)
  - B365W = Bet365 odds of match winner
  - B365L = Bet365 odds of match loser
  - B&WW = Bet&Win odds of match winner
  - B&WL = Bet&Win odds of match loser
  - CBW = Centrebet odds of match winner
  - CBL = Centrebet odds of match loser
  - EXW = Expekt odds of match winner
  - EXL = Expekt odds of match loser
  - LBW = Ladbrokes odds of match winner
  - LBL = Ladbrokes odds of match loser
  - GBW = Gamebookers odds of match winner
  - GBL = Gamebookers odds of match loser
  - IWW = Interwetten odds of match winner
  - IWL = Interwetten odds of match loser
  - PSW = Pinnacles Sports odds of match winner
  - PSL = Pinnacles Sports odds of match loser
  - SBW = Sportingbet odds of match winner
  - SBL = Sportingbet odds of match loser
  - SJW = Stan James odds of match winner
  - SJL = Stan James odds of match loser
  - UBW = Unibet odds of match winner
  - UBL = Unibet odds of match loser
  - MaxW= Maximum odds of match winner (as shown by Oddsportal.com)
  - MaxL= Maximum odds of match loser (as shown by Oddsportal.com)
  - AvgW= Average odds of match winner (as shown by Oddsportal.com)
  - AvgL= Average odds of match loser (as shown by Oddsportal.com)

Potential data split :
- Player : can be interesting as it is probable that players might have information attached to them atsome point
- Set : make things more complex without benifit. I would propose to store the set result in a json field / array fields
- Separation of match and match's odds (1 to 1 relationship)

Possible redundancy removal :
- ATP / WTA : seems to be a redundant id as it seems to be the order in which tournement happen each year.
- Wsets = redundant with the detail of sets
- Lsets = redundant with the detail of sets


If we also take into account women's result, we would have to take into account the "Best of" that is different for different categories.
By replacing "Best of" by a "men best of" and a "women best of" fields within tournement table.

Also, this normalisation, would potentialy need to change by looking at all the data:
Does all the tournement's fields stable between saisons ? (e.g. a tournemnt might change the 'best of' number / surface / location ).
In that situation, we will need to we store a different tournament and ned to decide if we want to split tournemant in 2 to keep the relationship between slightly different tournemnt

For this first version, I will keep the normalisation simple by removing the redundant fields and splitting in 2 tables (tournements/matches).


# Potential data error
there's probably a small mistake in the tennis-data 2011 file :
line 1598,Wimbledon Malisse X.	vs Melzer J.: best of should be 5 not 3


# What to do next
* Add unit tests for the data load function
* add system test for the api
* Make data loading faster using bulk inserts
* Integrate a django admin overall like Grapelli or jet
* docker compose deployemnt
