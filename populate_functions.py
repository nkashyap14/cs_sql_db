# populate_functions.py

from data_classes import *

def populate_match(parsed_data):
    # Extract match information from parsed_data
    match_id = parsed_data['matchID']
    #team1 always set to team that starts as T
    team1 = parsed_data['rounds']['tTeam'].iloc[0]
    #team2 always set to team that starts as CT
    team2 = parsed_data['rounds']['ctTeam'].iloc[0]
    winner = parsed_data['rounds'].tail(1)['winningTeam'].iloc[0]
    final_score = f"{max(parsed_data['rounds'].tail(1)['endCTScore'].iloc[-1], parsed_data['rounds'].tail(1)['endTScore'].iloc[-1])}:{min(parsed_data['rounds'].tail(1)['endCTScore'].iloc[-1], parsed_data['rounds'].tail(1)['endTScore'].iloc[-1])}"
    
    # Create a Match object
    match_obj = Match(matchID=match_id, team1=team1, team2=team2, winner=winner, finalScore=final_score)
    
    return match_obj

def populate_rounds(parsed_data):
    rounds_df = parsed_data['rounds']
    rounds_list = []

    for _, row in rounds_df.iterrows():
        round_obj = Round(
            matchID=parsed_data['matchID'],
            roundNum=row['roundNum'],
            startTick=row['startTick'],
            freezeTimeEndTick=row['freezeTimeEndTick'],
            endTick=row['endTick'],
            endOfficialTick=row['endOfficialTick'],
            tScore=row['tScore'],
            ctScore=row['ctScore'],
            endTScore=row['endTScore'],
            endCTScore=row['endCTScore'],
            tTeam=row['tTeam'],
            ctTeam=row['ctTeam'],
            winningSide=row['winningSide'],
            winningTeam=row['winningTeam'],
            losingTeam=row['losingTeam'],
            roundEndReason=row['roundEndReason'],
            ctFreezeTimeEndEqVal=row['ctFreezeTimeEndEqVal'],
            ctRoundStartEqVal=row['ctRoundStartEqVal'],
            ctRoundSpendMoney=row['ctRoundSpendMoney'],
            ctBuyType=row['ctBuyType'],
            tFreezeTimeEndEqVal=row['tFreezeTimeEndEqVal'],
            tRoundStartEqVal=row['tRoundStartEqVal'],
            tRoundSpendMoney=row['tRoundSpendMoney'],
            tBuyType=row['tBuyType'],
            mapName=parsed_data['mapName']
        )
        rounds_list.append(round_obj)

    return rounds_list

def populate_weapon_fires(parsed_data):
    weapon_fires_df = parsed_data['weaponFires']
    weapon_fires_df = parsed_data['weaponFires'].drop_duplicates(subset=['matchID', 'roundNum', 'tick'], keep='first')
    weapon_fires_list = []

    for _, row in weapon_fires_df.iterrows():
        weapon_fire_obj = WeaponFire(
            tick=row['tick'],
            seconds=row['seconds'],
            clockTime=row['clockTime'],
            playerSteamID=row['playerSteamID'],
            playerName=row['playerName'],
            playerTeam=row['playerTeam'],
            playerSide=row['playerSide'],
            playerX=row['playerX'],
            playerY=row['playerY'],
            playerZ=row['playerZ'],
            playerViewX=row['playerViewX'],
            playerViewY=row['playerViewY'],
            playerStrafe=row['playerStrafe'],
            weapon=row['weapon'],
            weaponClass=row['weaponClass'],
            ammoInMagazine=row['ammoInMagazine'],
            ammoInReserve=row['ammoInReserve'],
            zoomLevel=row['zoomLevel'],
            roundNum=row['roundNum'],
            matchID=parsed_data['matchID'],
            mapName=parsed_data['mapName']
        )
        weapon_fires_list.append(weapon_fire_obj)

    return weapon_fires_list

def populate_flashes(parsed_data):
    flashes_df = parsed_data['flashes']
    flashes_list = []

    for _, row in flashes_df.iterrows():
        flash_obj = Flash(
            tick=row['tick'],
            seconds=row['seconds'],
            clockTime=row['clockTime'],
            attackerSteamID=row['attackerSteamID'],
            attackerName=row['attackerName'],
            attackerTeam=row['attackerTeam'],
            attackerSide=row['attackerSide'],
            attackerX=row['attackerX'],
            attackerY=row['attackerY'],
            attackerZ=row['attackerZ'],
            attackerViewX=row['attackerViewX'],
            attackerViewY=row['attackerViewY'],
            playerSteamID=row['playerSteamID'],
            playerName=row['playerName'],
            playerTeam=row['playerTeam'],
            playerSide=row['playerSide'],
            playerX=row['playerX'],
            playerY=row['playerY'],
            playerZ=row['playerZ'],
            playerViewX=row['playerViewX'],
            playerViewY=row['playerViewY'],
            flashDuration=row['flashDuration'],
            roundNum=row['roundNum'],
            matchID=parsed_data['matchID'],
            mapName=parsed_data['mapName']
        )
        flashes_list.append(flash_obj)

    return flashes_list

def populate_grenades(parsed_data):
    grenades_df = parsed_data['grenades']
    grenades_df = parsed_data['grenades'].drop_duplicates(subset=['matchID', 'roundNum', 'throwTick'], keep='first')
    grenades_list = []

    for _, row in grenades_df.iterrows():
        grenade_obj = Grenade(
            throwTick=row['throwTick'],
            destroyTick=row['destroyTick'],
            throwSeconds=row['throwSeconds'],
            throwClockTime=row['throwClockTime'],
            destroySeconds=row['destroySeconds'],
            destroyClockTime=row['destroyClockTime'],
            throwerSteamID=row['throwerSteamID'],
            throwerName=row['throwerName'],
            throwerTeam=row['throwerTeam'],
            throwerSide=row['throwerSide'],
            throwerX=row['throwerX'],
            throwerY=row['throwerY'],
            throwerZ=row['throwerZ'],
            grenadeType=row['grenadeType'],
            grenadeX=row['grenadeX'],
            grenadeY=row['grenadeY'],
            grenadeZ=row['grenadeZ'],
            entityId=row['entityId'],
            roundNum=row['roundNum'],
            matchID=parsed_data['matchID'],
            mapName=parsed_data['mapName']
        )
        grenades_list.append(grenade_obj)

    return grenades_list

def populate_damages(parsed_data):
    damages_df = parsed_data['damages']
    damages_df = parsed_data['damages'].drop_duplicates(subset=['matchID', 'roundNum', 'tick', 'attackerSteamID', 'victimSteamID'], keep='first')
    damages_list = []

    for _, row in damages_df.iterrows():
        damage_obj = Damage(
            tick=row['tick'],
            seconds=row['seconds'],
            clockTime=row['clockTime'],
            attackerSteamID=row['attackerSteamID'],
            attackerName=row['attackerName'],
            attackerTeam=row['attackerTeam'],
            attackerSide=row['attackerSide'],
            attackerX=row['attackerX'],
            attackerY=row['attackerY'],
            attackerZ=row['attackerZ'],
            attackerViewX=row['attackerViewX'],
            attackerViewY=row['attackerViewY'],
            attackerStrafe=row['attackerStrafe'],
            victimSteamID=row['victimSteamID'],
            victimName=row['victimName'],
            victimTeam=row['victimTeam'],
            victimSide=row['victimSide'],
            victimX=row['victimX'],
            victimY=row['victimY'],
            victimZ=row['victimZ'],
            victimViewX=row['victimViewX'],
            victimViewY=row['victimViewY'],
            weapon=row['weapon'],
            weaponClass=row['weaponClass'],
            hpDamage=row['hpDamage'],
            hpDamageTaken=row['hpDamageTaken'],
            armorDamage=row['armorDamage'],
            armorDamageTaken=row['armorDamageTaken'],
            hitGroup=row['hitGroup'],
            isFriendlyFire=row['isFriendlyFire'],
            distance=row['distance'],
            zoomLevel=row['zoomLevel'],
            roundNum=row['roundNum'],
            matchID=parsed_data['matchID'],
            mapName=parsed_data['mapName']
        )
        damages_list.append(damage_obj)

    return damages_list

def populate_kills(parsed_data):
    kills_df = parsed_data['kills']
    kills_list = []

    for _, row in kills_df.iterrows():
        kill_obj = Kill(
            tick=row['tick'],
            seconds=row['seconds'],
            clockTime=row['clockTime'],
            attackerSteamID=row['attackerSteamID'],
            attackerName=row['attackerName'],
            attackerTeam=row['attackerTeam'],
            attackerSide=row['attackerSide'],
            attackerX=row['attackerX'],
            attackerY=row['attackerY'],
            attackerZ=row['attackerZ'],
            attackerViewX=row['attackerViewX'],
            attackerViewY=row['attackerViewY'],
            victimSteamID=row['victimSteamID'],
            victimName=row['victimName'],
            victimTeam=row['victimTeam'],
            victimSide=row['victimSide'],
            victimX=row['victimX'],
            victimY=row['victimY'],
            victimZ=row['victimZ'],
            victimViewX=row['victimViewX'],
            victimViewY=row['victimViewY'],
            assisterSteamID=row['assisterSteamID'],
            assisterName=row['assisterName'],
            assisterTeam=row['assisterTeam'],
            assisterSide=row['assisterSide'],
            isSuicide=row['isSuicide'],
            isTeamkill=row['isTeamkill'],
            isWallbang=row['isWallbang'],
            penetratedObjects=row['penetratedObjects'],
            isFirstKill=row['isFirstKill'],
            isHeadshot=row['isHeadshot'],
            victimBlinded=row['victimBlinded'],
            attackerBlinded=row['attackerBlinded'],
            flashThrowerSteamID=row.get('flashThrowerSteamID'),
            flashThrowerName=row.get('flashThrowerName'),
            flashThrowerTeam=row.get('flashThrowerTeam'),
            flashThrowerSide=row.get('flashThrowerSide'),
            noScope=row['noScope'],
            thruSmoke=row['thruSmoke'],
            distance=row['distance'],
            isTrade=row['isTrade'],
            playerTradedName=row['playerTradedName'],
            playerTradedTeam=row['playerTradedTeam'],
            playerTradedSteamID=row['playerTradedSteamID'],
            playerTradedSide=row['playerTradedSide'],
            weapon=row['weapon'],
            weaponClass=row['weaponClass'],
            roundNum=row['roundNum'],
            matchID=parsed_data['matchID'],
            mapName=parsed_data['mapName']
        )
        kills_list.append(kill_obj)

    return kills_list

def populate_player_frames(parsed_data):
    player_frames_df = parsed_data['playerFrames']
    player_frames_list = []

    for _, row in player_frames_df.iterrows():
        player_frame_obj = PlayerFrame(
            roundNum=row['roundNum'],
            tick=row['tick'],
            seconds=row['seconds'],
            side=row['side'],
            teamName=row['teamName'],
            steamID=row['steamID'],
            name=row['name'],
            team=row['team'],
            x=row['x'],
            y=row['y'],
            z=row['z'],
            eyeX=row['eyeX'],
            eyeY=row['eyeY'],
            eyeZ=row['eyeZ'],
            velocityX=row['velocityX'],
            velocityY=row['velocityY'],
            velocityZ=row['velocityZ'],
            viewX=row['viewX'],
            viewY=row['viewY'],
            hp=row['hp'],
            armor=row['armor'],
            activeWeapon=row['activeWeapon'],
            flashGrenades=row['flashGrenades'],
            smokeGrenades=row['smokeGrenades'],
            heGrenades=row['heGrenades'],
            fireGrenades=row['fireGrenades'],
            totalUtility=row['totalUtility'],
            lastPlaceName=row['lastPlaceName'],
            isAlive=row['isAlive'],
            isBot=row['isBot'],
            isBlinded=row['isBlinded'],
            isAirborne=row['isAirborne'],
            isDucking=row['isDucking'],
            isDuckingInProgress=row['isDuckingInProgress'],
            isUnDuckingInProgress=row['isUnDuckingInProgress'],
            isDefusing=row['isDefusing'],
            isPlanting=row['isPlanting'],
            isReloading=row['isReloading'],
            isInBombZone=row['isInBombZone'],
            isInBuyZone=row['isInBuyZone'],
            isStanding=row['isStanding'],
            isScoped=row['isScoped'],
            isWalking=row['isWalking'],
            isUnknown=row['isUnknown'],
            spotters=row['spotters'],
            equipmentValue=row['equipmentValue'],
            equipmentValueFreezetimeEnd=row['equipmentValueFreezetimeEnd'],
            equipmentValueRoundStart=row['equipmentValueRoundStart'],
            cash=row['cash'],
            cashSpendThisRound=row['cashSpendThisRound'],
            cashSpendTotal=row['cashSpendTotal'],
            hasHelmet=row['hasHelmet'],
            hasDefuse=row['hasDefuse'],
            hasBomb=row['hasBomb'],
            ping=row['ping'],
            zoomLevel=row['zoomLevel'],
            matchID=parsed_data['matchID'],
            mapName=parsed_data['mapName']
        )
        player_frames_list.append(player_frame_obj)

    return player_frames_list

def populate_frames(parsed_data, matchID):
    frames_df = parsed_data['frames']
    frames_list = []

    for _, row in frames_df.iterrows():
        frame_obj = Frame(
            roundNum=row['roundNum'],
            tick=row['tick'],
            seconds=row['seconds'],
            ctTeamName=row['ctTeamName'],
            ctEqVal=row['ctEqVal'],
            ctAlivePlayers=row['ctAlivePlayers'],
            ctUtility=row['ctUtility'],
            tTeamName=row['tTeamName'],
            tEqVal=row['tEqVal'],
            tAlivePlayers=row['tAlivePlayers'],
            matchID=matchID,
            tUtility=row['tUtility']
        )
        frames_list.append(frame_obj)

    return frames_list


def populate_bomb_events(parsed_data):
    bomb_events_df = parsed_data['bombEvents']
    bomb_events_list = []

    for _, row in bomb_events_df.iterrows():
        bomb_event_obj = BombEvent(
            tick=row['tick'],
            seconds=row['seconds'],
            clockTime=row['clockTime'],
            playerSteamID=row['playerSteamID'],
            playerName=row['playerName'],
            playerTeam=row['playerTeam'],
            playerX=row['playerX'],
            playerY=row['playerY'],
            playerZ=row['playerZ'],
            bombAction=row['bombAction'],
            bombSite=row['bombSite'],
            roundNum=row['roundNum'],
            matchID=parsed_data['matchID'],
            mapName=parsed_data['mapName']
        )
        bomb_events_list.append(bomb_event_obj)

    return bomb_events_list