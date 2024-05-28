# Function to generate the SQL command for inserting a single Match object
def insert_single_match_sql(match_obj):
    return f"""
    BEGIN TRANSACTION;
    INSERT INTO Matches (matchID, team1, team2, winner, finalScore) VALUES (
        '{match_obj.matchID}', '{match_obj.team1}', '{match_obj.team2}', '{match_obj.winner}', '{match_obj.finalScore}');
    COMMIT;
    """

# Function to generate the SQL command for inserting a single Round object
def insert_single_round_sql(round_obj):
    return f"""
    INSERT INTO Rounds (matchID, roundNum, startTick, freezeTimeEndTick, endTick, endOfficialTick, 
                        tScore, ctScore, endTScore, endCTScore, tTeam, ctTeam, winningSide, 
                        winningTeam, losingTeam, roundEndReason, ctFreezeTimeEndEqVal, 
                        ctRoundStartEqVal, ctRoundSpendMoney, ctBuyType, tFreezeTimeEndEqVal, 
                        tRoundStartEqVal, tRoundSpendMoney, tBuyType, mapName) VALUES (
        '{round_obj.matchID}', {round_obj.roundNum}, {round_obj.startTick}, {round_obj.freezeTimeEndTick}, 
        {round_obj.endTick}, {round_obj.endOfficialTick}, {round_obj.tScore}, {round_obj.ctScore}, 
        {round_obj.endTScore}, {round_obj.endCTScore}, '{round_obj.tTeam}', '{round_obj.ctTeam}', 
        '{round_obj.winningSide}', '{round_obj.winningTeam}', '{round_obj.losingTeam}', 
        '{round_obj.roundEndReason}', {round_obj.ctFreezeTimeEndEqVal}, {round_obj.ctRoundStartEqVal}, 
        {round_obj.ctRoundSpendMoney}, '{round_obj.ctBuyType}', {round_obj.tFreezeTimeEndEqVal}, 
        {round_obj.tRoundStartEqVal}, {round_obj.tRoundSpendMoney}, '{round_obj.tBuyType}', 
        '{round_obj.mapName}');
    """

# Function to generate the SQL command for inserting a single Kill object
def insert_single_kill_sql(kill_obj):
    return f"""
    INSERT INTO Kills (tick, seconds, clockTime, attackerSteamID, attackerName, attackerTeam, attackerSide, attackerX, attackerY, attackerZ, attackerViewX, attackerViewY, victimSteamID, victimName, victimTeam, victimSide, victimX, victimY, victimZ, victimViewX, victimViewY, assisterSteamID, assisterName, assisterTeam, assisterSide, isSuicide, isTeamkill, isWallbang, penetratedObjects, isFirstKill, isHeadshot, victimBlinded, attackerBlinded, flashThrowerSteamID, flashThrowerName, flashThrowerTeam, flashThrowerSide, noScope, thruSmoke, distance, isTrade, playerTradedName, playerTradedTeam, playerTradedSteamID, playerTradedSide, weapon, weaponClass, roundNum, matchID, mapName) VALUES (
        {kill_obj.tick}, {kill_obj.seconds}, '{kill_obj.clockTime}', '{kill_obj.attackerSteamID}', '{kill_obj.attackerName}', 
        '{kill_obj.attackerTeam}', '{kill_obj.attackerSide}', {kill_obj.attackerX}, {kill_obj.attackerY}, {kill_obj.attackerZ}, 
        {kill_obj.attackerViewX}, {kill_obj.attackerViewY}, '{kill_obj.victimSteamID}', '{kill_obj.victimName}', '{kill_obj.victimTeam}', 
        '{kill_obj.victimSide}', {kill_obj.victimX}, {kill_obj.victimY}, {kill_obj.victimZ}, {kill_obj.victimViewX}, {kill_obj.victimViewY}, 
        '{kill_obj.assisterSteamID}', '{kill_obj.assisterName}', '{kill_obj.assisterTeam}', '{kill_obj.assisterSide}', 
        {kill_obj.isSuicide}, {kill_obj.isTeamkill}, {kill_obj.isWallbang}, {kill_obj.penetratedObjects}, {kill_obj.isFirstKill}, 
        {kill_obj.isHeadshot}, {kill_obj.victimBlinded}, {kill_obj.attackerBlinded}, '{kill_obj.flashThrowerSteamID}', 
        '{kill_obj.flashThrowerName}', '{kill_obj.flashThrowerTeam}', '{kill_obj.flashThrowerSide}', {kill_obj.noScope}, 
        {kill_obj.thruSmoke}, {kill_obj.distance}, {kill_obj.isTrade}, '{kill_obj.playerTradedName}', '{kill_obj.playerTradedTeam}', 
        '{kill_obj.playerTradedSteamID}', '{kill_obj.playerTradedSide}', '{kill_obj.weapon}', '{kill_obj.weaponClass}', 
        {kill_obj.roundNum}, '{kill_obj.matchID}', '{kill_obj.mapName}');
    """

# Function to generate the SQL command for inserting a single Grenade object
def insert_single_grenade_sql(grenade_obj):
    return f"""
    INSERT INTO Grenades (throwTick, destroyTick, throwSeconds, throwClockTime, destroySeconds, destroyClockTime, throwerSteamID, throwerName, throwerTeam, throwerSide, throwerX, throwerY, throwerZ, grenadeType, grenadeX, grenadeY, grenadeZ, entityId, roundNum, matchID, mapName) VALUES (
        {grenade_obj.throwTick}, {grenade_obj.destroyTick}, {grenade_obj.throwSeconds}, '{grenade_obj.throwClockTime}', {grenade_obj.destroySeconds}, 
        '{grenade_obj.destroyClockTime}', '{grenade_obj.throwerSteamID}', '{grenade_obj.throwerName}', '{grenade_obj.throwerTeam}', 
        '{grenade_obj.throwerSide}', {grenade_obj.throwerX}, {grenade_obj.throwerY}, {grenade_obj.throwerZ}, '{grenade_obj.grenadeType}', 
        {grenade_obj.grenadeX}, {grenade_obj.grenadeY}, {grenade_obj.grenadeZ}, {grenade_obj.entityId}, {grenade_obj.roundNum}, 
        '{grenade_obj.matchID}', '{grenade_obj.mapName}');
    """

# Function to generate the SQL command for inserting a single Flash object
def insert_single_flash_sql(flash_obj):
    return f"""
    INSERT INTO Flashes (tick, seconds, clockTime, attackerSteamID, attackerName, attackerTeam, attackerSide, attackerX, attackerY, attackerZ, attackerViewX, attackerViewY, playerSteamID, playerName, playerTeam, playerSide, playerX, playerY, playerZ, playerViewX, playerViewY, flashDuration, roundNum, matchID, mapName) VALUES (
        {flash_obj.tick}, {flash_obj.seconds}, '{flash_obj.clockTime}', '{flash_obj.attackerSteamID}', '{flash_obj.attackerName}', '{flash_obj.attackerTeam}', 
        '{flash_obj.attackerSide}', {flash_obj.attackerX}, {flash_obj.attackerY}, {flash_obj.attackerZ}, {flash_obj.attackerViewX}, 
        {flash_obj.attackerViewY}, '{flash_obj.playerSteamID}', '{flash_obj.playerName}', '{flash_obj.playerTeam}', '{flash_obj.playerSide}', 
        {flash_obj.playerX}, {flash_obj.playerY}, {flash_obj.playerZ}, {flash_obj.playerViewX}, {flash_obj.playerViewY}, {flash_obj.flashDuration}, 
        {flash_obj.roundNum}, '{flash_obj.matchID}', '{flash_obj.mapName}');
    """

# Function to generate the SQL command for inserting a single WeaponFire object
def insert_single_weapon_fire_sql(weapon_fire_obj):
    return f"""
    INSERT INTO WeaponFires (tick, seconds, clockTime, playerSteamID, playerName, playerTeam, playerSide, playerX, playerY, playerZ, playerViewX, playerViewY, playerStrafe, weapon, weaponClass, ammoInMagazine, ammoInReserve, zoomLevel, roundNum, matchID, mapName) VALUES (
        {weapon_fire_obj.tick}, {weapon_fire_obj.seconds}, '{weapon_fire_obj.clockTime}', '{weapon_fire_obj.playerSteamID}', '{weapon_fire_obj.playerName}', 
        '{weapon_fire_obj.playerTeam}', '{weapon_fire_obj.playerSide}', {weapon_fire_obj.playerX}, {weapon_fire_obj.playerY}, {weapon_fire_obj.playerZ}, 
        {weapon_fire_obj.playerViewX}, {weapon_fire_obj.playerViewY}, {weapon_fire_obj.playerStrafe}, '{weapon_fire_obj.weapon}', 
        '{weapon_fire_obj.weaponClass}', {weapon_fire_obj.ammoInMagazine}, {weapon_fire_obj.ammoInReserve}, {weapon_fire_obj.zoomLevel}, 
        {weapon_fire_obj.roundNum}, '{weapon_fire_obj.matchID}', '{weapon_fire_obj.mapName}');
    """

# Function to generate the SQL command for inserting a single BombEvent object
def insert_single_bomb_event_sql(bomb_event_obj):
    return f"""
    INSERT INTO BombEvents (tick, seconds, clockTime, playerSteamID, playerName, playerTeam, playerX, playerY, playerZ, bombAction, bombSite, roundNum, matchID, mapName) VALUES (
        {bomb_event_obj.tick}, {bomb_event_obj.seconds}, '{bomb_event_obj.clockTime}', '{bomb_event_obj.playerSteamID}', '{bomb_event_obj.playerName}', 
        '{bomb_event_obj.playerTeam}', {bomb_event_obj.playerX}, {bomb_event_obj.playerY}, {bomb_event_obj.playerZ}, '{bomb_event_obj.bombAction}', 
        '{bomb_event_obj.bombSite}', {bomb_event_obj.roundNum}, '{bomb_event_obj.matchID}', '{bomb_event_obj.mapName}');
    """

# Function to generate the SQL command for inserting a single Frame object
def insert_single_frame_sql(frame_obj):
    return f"""
    INSERT INTO Frames (roundNum, tick, seconds, ctTeamName, ctEqVal, ctAlivePlayers, ctUtility, tTeamName, tEqVal, tAlivePlayers, tUtility) VALUES (
        {frame_obj.roundNum}, {frame_obj.tick}, {frame_obj.seconds}, '{frame_obj.ctTeamName}', {frame_obj.ctEqVal}, {frame_obj.ctAlivePlayers}, 
        {frame_obj.ctUtility}, '{frame_obj.tTeamName}', {frame_obj.tEqVal}, {frame_obj.tAlivePlayers}, {frame_obj.tUtility});
    """

# Function to generate the SQL command for inserting a single PlayerFrame object
def insert_single_player_frame_sql(player_frame_obj):
    return f"""
    INSERT INTO PlayerFrames (matchID, roundNum, tick, seconds, side, teamName, steamID, name, team, x, y, z, eyeX, eyeY, eyeZ, velocityX, velocityY, velocityZ, viewX, viewY, hp, armor, activeWeapon, flashGrenades, smokeGrenades, heGrenades, fireGrenades, totalUtility, lastPlaceName, isAlive, isBot, isBlinded, isAirborne, isDucking, isDuckingInProgress, isUnDuckingInProgress, isDefusing, isPlanting, isReloading, isInBombZone, isInBuyZone, isStanding, isScoped, isWalking, isUnknown, spotters, equipmentValue, equipmentValueFreezetimeEnd, equipmentValueRoundStart, cash, cashSpendThisRound, cashSpendTotal, hasHelmet, hasDefuse, hasBomb, ping, zoomLevel, mapName) VALUES (
        '{player_frame_obj.matchID}', {player_frame_obj.roundNum}, {player_frame_obj.tick}, {player_frame_obj.seconds}, '{player_frame_obj.side}', 
        '{player_frame_obj.teamName}', '{player_frame_obj.steamID}', '{player_frame_obj.name}', '{player_frame_obj.team}', {player_frame_obj.x}, 
        {player_frame_obj.y}, {player_frame_obj.z}, {player_frame_obj.eyeX}, {player_frame_obj.eyeY}, {player_frame_obj.eyeZ}, 
        {player_frame_obj.velocityX}, {player_frame_obj.velocityY}, {player_frame_obj.velocityZ}, {player_frame_obj.viewX}, {player_frame_obj.viewY}, 
        {player_frame_obj.hp}, {player_frame_obj.armor}, '{player_frame_obj.activeWeapon}', {player_frame_obj.flashGrenades}, {player_frame_obj.smokeGrenades}, 
        {player_frame_obj.heGrenades}, {player_frame_obj.fireGrenades}, {player_frame_obj.totalUtility}, '{player_frame_obj.lastPlaceName}', 
        {player_frame_obj.isAlive}, {player_frame_obj.isBot}, {player_frame_obj.isBlinded}, {player_frame_obj.isAirborne}, {player_frame_obj.isDucking}, 
        {player_frame_obj.isDuckingInProgress}, {player_frame_obj.isUnDuckingInProgress}, {player_frame_obj.isDefusing}, {player_frame_obj.isPlanting}, 
        {player_frame_obj.isReloading}, {player_frame_obj.isInBombZone}, {player_frame_obj.isInBuyZone}, {player_frame_obj.isStanding}, {player_frame_obj.isScoped}, 
        {player_frame_obj.isWalking}, {player_frame_obj.isUnknown}, '{player_frame_obj.spotters}', {player_frame_obj.equipmentValue}, 
        {player_frame_obj.equipmentValueFreezetimeEnd}, {player_frame_obj.equipmentValueRoundStart}, {player_frame_obj.cash}, {player_frame_obj.cashSpendThisRound}, 
        {player_frame_obj.cashSpendTotal}, {player_frame_obj.hasHelmet}, {player_frame_obj.hasDefuse}, {player_frame_obj.hasBomb}, {player_frame_obj.ping}, 
        {player_frame_obj.zoomLevel}, '{player_frame_obj.mapName}');
    """


def insert_single_damage_sql(damage_obj):
    return f"""
    INSERT INTO Damages (tick, seconds, clockTime, attackerSteamID, attackerName, attackerTeam, attackerSide, attackerX, attackerY, attackerZ, attackerViewX, attackerViewY, attackerStrafe, victimSteamID, victimName, victimTeam, victimSide, victimX, victimY, victimZ, victimViewX, victimViewY, weapon, weaponClass, hpDamage, hpDamageTaken, armorDamage, armorDamageTaken, hitGroup, isFriendlyFire, distance, zoomLevel, roundNum, matchID, mapName) VALUES (
        {damage_obj.tick}, {damage_obj.seconds}, '{damage_obj.clockTime}', '{damage_obj.attackerSteamID}', '{damage_obj.attackerName}', 
        '{damage_obj.attackerTeam}', '{damage_obj.attackerSide}', {damage_obj.attackerX}, {damage_obj.attackerY}, {damage_obj.attackerZ}, 
        {damage_obj.attackerViewX}, {damage_obj.attackerViewY}, {damage_obj.attackerStrafe}, '{damage_obj.victimSteamID}', 
        '{damage_obj.victimName}', '{damage_obj.victimTeam}', '{damage_obj.victimSide}', {damage_obj.victimX}, {damage_obj.victimY}, 
        {damage_obj.victimZ}, {damage_obj.victimViewX}, {damage_obj.victimViewY}, '{damage_obj.weapon}', '{damage_obj.weaponClass}', 
        {damage_obj.hpDamage}, {damage_obj.hpDamageTaken}, {damage_obj.armorDamage}, {damage_obj.armorDamageTaken}, '{damage_obj.hitGroup}', 
        {damage_obj.isFriendlyFire}, {damage_obj.distance}, {damage_obj.zoomLevel}, {damage_obj.roundNum}, '{damage_obj.matchID}', 
        '{damage_obj.mapName}');
    """