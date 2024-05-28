class Round:
    def __init__(self, matchID, mapName, roundNum, startTick, freezeTimeEndTick, endTick, endOfficialTick, tScore, ctScore, endTScore, endCTScore, tTeam, ctTeam, winningSide, winningTeam, losingTeam, roundEndReason, ctFreezeTimeEndEqVal, ctRoundStartEqVal, ctRoundSpendMoney, ctBuyType, tFreezeTimeEndEqVal, tRoundStartEqVal, tRoundSpendMoney, tBuyType):
        self.matchID = matchID
        self.mapName = mapName
        self.roundNum = roundNum
        self.startTick = startTick
        self.freezeTimeEndTick = freezeTimeEndTick
        self.endTick = endTick
        self.endOfficialTick = endOfficialTick
        self.tScore = tScore
        self.ctScore = ctScore
        self.endTScore = endTScore
        self.endCTScore = endCTScore
        self.tTeam = tTeam
        self.ctTeam = ctTeam
        self.winningSide = winningSide
        self.winningTeam = winningTeam
        self.losingTeam = losingTeam
        self.roundEndReason = roundEndReason
        self.ctFreezeTimeEndEqVal = ctFreezeTimeEndEqVal
        self.ctRoundStartEqVal = ctRoundStartEqVal
        self.ctRoundSpendMoney = ctRoundSpendMoney
        self.ctBuyType = ctBuyType
        self.tFreezeTimeEndEqVal = tFreezeTimeEndEqVal
        self.tRoundStartEqVal = tRoundStartEqVal
        self.tRoundSpendMoney = tRoundSpendMoney
        self.tBuyType = tBuyType
        self.primary = (matchID, roundNum)
        self.foreign = matchID

    def __repr__(self):
        return (f"Round(matchID={self.matchID}, roundNum={self.roundNum}, startTick={self.startTick}, "
                f"freezeTimeEndTick={self.freezeTimeEndTick}, endTick={self.endTick}, "
                f"endOfficialTick={self.endOfficialTick}, tScore={self.tScore}, ctScore={self.ctScore}, "
                f"endTScore={self.endTScore}, endCTScore={self.endCTScore}, tTeam={self.tTeam}, "
                f"ctTeam={self.ctTeam}, winningSide={self.winningSide}, winningTeam={self.winningTeam}, "
                f"losingTeam={self.losingTeam}, roundEndReason={self.roundEndReason}, "
                f"ctFreezeTimeEndEqVal={self.ctFreezeTimeEndEqVal}, ctRoundStartEqVal={self.ctRoundStartEqVal}, "
                f"ctRoundSpendMoney={self.ctRoundSpendMoney}, ctBuyType={self.ctBuyType}, "
                f"tFreezeTimeEndEqVal={self.tFreezeTimeEndEqVal}, tRoundStartEqVal={self.tRoundStartEqVal}, "
                f"tRoundSpendMoney={self.tRoundSpendMoney}, tBuyType={self.tBuyType}, mapName={self.mapName})")


class Kill:
    def __init__(self, tick, seconds, clockTime, attackerSteamID, attackerName, attackerTeam, attackerSide, attackerX, attackerY, attackerZ, attackerViewX, attackerViewY, victimSteamID, victimName, victimTeam, victimSide, victimX, victimY, victimZ, victimViewX, victimViewY, assisterSteamID, assisterName, assisterTeam, assisterSide, isSuicide, isTeamkill, isWallbang, penetratedObjects, isFirstKill, isHeadshot, victimBlinded, attackerBlinded, flashThrowerSteamID, flashThrowerName, flashThrowerTeam, flashThrowerSide, noScope, thruSmoke, distance, isTrade, playerTradedName, playerTradedTeam, playerTradedSteamID, playerTradedSide, weapon, weaponClass, roundNum, matchID, mapName):
        self.tick = tick
        self.seconds = seconds
        self.clockTime = clockTime
        self.attackerSteamID = attackerSteamID
        self.attackerName = attackerName
        self.attackerTeam = attackerTeam
        self.attackerSide = attackerSide
        self.attackerX = attackerX
        self.attackerY = attackerY
        self.attackerZ = attackerZ
        self.attackerViewX = attackerViewX
        self.attackerViewY = attackerViewY
        self.victimSteamID = victimSteamID
        self.victimName = victimName
        self.victimTeam = victimTeam
        self.victimSide = victimSide
        self.victimX = victimX
        self.victimY = victimY
        self.victimZ = victimZ
        self.victimViewX = victimViewX
        self.victimViewY = victimViewY
        self.assisterSteamID = assisterSteamID
        self.assisterName = assisterName
        self.assisterTeam = assisterTeam
        self.assisterSide = assisterSide
        self.isSuicide = isSuicide
        self.isTeamkill = isTeamkill
        self.isWallbang = isWallbang
        self.penetratedObjects = penetratedObjects
        self.isFirstKill = isFirstKill
        self.isHeadshot = isHeadshot
        self.victimBlinded = victimBlinded
        self.attackerBlinded = attackerBlinded
        self.flashThrowerSteamID = flashThrowerSteamID
        self.flashThrowerName = flashThrowerName
        self.flashThrowerTeam = flashThrowerTeam
        self.flashThrowerSide = flashThrowerSide
        self.noScope = noScope
        self.thruSmoke = thruSmoke
        self.distance = distance
        self.isTrade = isTrade
        self.playerTradedName = playerTradedName
        self.playerTradedTeam = playerTradedTeam
        self.playerTradedSteamID = playerTradedSteamID
        self.playerTradedSide = playerTradedSide
        self.weapon = weapon
        self.weaponClass = weaponClass
        self.roundNum = roundNum
        self.matchID = matchID
        self.mapName = mapName
        self.primary = (matchID, roundNum, tick)
        self.foreign = matchID

class Damage:
    def __init__(self, tick, seconds, clockTime, attackerSteamID, attackerName, attackerTeam, attackerSide, attackerX, attackerY, attackerZ, attackerViewX, attackerViewY, attackerStrafe, victimSteamID, victimName, victimTeam, victimSide, victimX, victimY, victimZ, victimViewX, victimViewY, weapon, weaponClass, hpDamage, hpDamageTaken, armorDamage, armorDamageTaken, hitGroup, isFriendlyFire, distance, zoomLevel, roundNum, matchID, mapName):
        self.tick = tick
        self.seconds = seconds
        self.clockTime = clockTime
        self.attackerSteamID = attackerSteamID
        self.attackerName = attackerName
        self.attackerTeam = attackerTeam
        self.attackerSide = attackerSide
        self.attackerX = attackerX
        self.attackerY = attackerY
        self.attackerZ = attackerZ
        self.attackerViewX = attackerViewX
        self.attackerViewY = attackerViewY
        self.attackerStrafe = attackerStrafe
        self.victimSteamID = victimSteamID
        self.victimName = victimName
        self.victimTeam = victimTeam
        self.victimSide = victimSide
        self.victimX = victimX
        self.victimY = victimY
        self.victimZ = victimZ
        self.victimViewX = victimViewX
        self.victimViewY = victimViewY
        self.weapon = weapon
        self.weaponClass = weaponClass
        self.hpDamage = hpDamage
        self.hpDamageTaken = hpDamageTaken
        self.armorDamage = armorDamage
        self.armorDamageTaken = armorDamageTaken
        self.hitGroup = hitGroup
        self.isFriendlyFire = isFriendlyFire
        self.distance = distance
        self.zoomLevel = zoomLevel
        self.roundNum = roundNum
        self.matchID = matchID
        self.mapName = mapName
        self.primary = (matchID, roundNum, tick)
        self.foreign = matchID


class Grenade:
    def __init__(self, throwTick, destroyTick, throwSeconds, throwClockTime, destroySeconds, destroyClockTime, throwerSteamID, throwerName, throwerTeam, throwerSide, throwerX, throwerY, throwerZ, grenadeType, grenadeX, grenadeY, grenadeZ, entityId, roundNum, matchID, mapName):
        self.throwTick = throwTick
        self.destroyTick = destroyTick
        self.throwSeconds = throwSeconds
        self.throwClockTime = throwClockTime
        self.destroySeconds = destroySeconds
        self.destroyClockTime = destroyClockTime
        self.throwerSteamID = throwerSteamID
        self.throwerName = throwerName
        self.throwerTeam = throwerTeam
        self.throwerSide = throwerSide
        self.throwerX = throwerX
        self.throwerY = throwerY
        self.throwerZ = throwerZ
        self.grenadeType = grenadeType
        self.grenadeX = grenadeX
        self.grenadeY = grenadeY
        self.grenadeZ = grenadeZ
        self.entityId = entityId
        self.roundNum = roundNum
        self.matchID = matchID
        self.mapName = mapName
        self.primary = (matchID, roundNum, throwTick)
        self.foreign = matchID

class BombEvent:
    def __init__(self, tick, seconds, clockTime, playerSteamID, playerName, playerTeam, playerX, playerY, playerZ, bombAction, bombSite, roundNum, matchID, mapName):
        self.tick = tick
        self.seconds = seconds
        self.clockTime = clockTime
        self.playerSteamID = playerSteamID
        self.playerName = playerName
        self.playerTeam = playerTeam
        self.playerX = playerX
        self.playerY = playerY
        self.playerZ = playerZ
        self.bombAction = bombAction
        self.bombSite = bombSite
        self.roundNum = roundNum
        self.matchID = matchID
        self.mapName = mapName
        self.foreign = matchID
        self.primary = (matchID, roundNum, tick)

class WeaponFire:
    def __init__(self, tick, seconds, clockTime, playerSteamID, playerName, playerTeam, playerSide, playerX, playerY, playerZ, playerViewX, playerViewY, playerStrafe, weapon, weaponClass, ammoInMagazine, ammoInReserve, zoomLevel, roundNum, matchID, mapName):
        self.tick = tick
        self.seconds = seconds
        self.clockTime = clockTime
        self.playerSteamID = playerSteamID
        self.playerName = playerName
        self.playerTeam = playerTeam
        self.playerSide = playerSide
        self.playerX = playerX
        self.playerY = playerY
        self.playerZ = playerZ
        self.playerViewX = playerViewX
        self.playerViewY = playerViewY
        self.playerStrafe = playerStrafe
        self.weapon = weapon
        self.weaponClass = weaponClass
        self.ammoInMagazine = ammoInMagazine
        self.ammoInReserve = ammoInReserve
        self.zoomLevel = zoomLevel
        self.roundNum = roundNum
        self.matchID = matchID
        self.mapName = mapName
        self.primary = (matchID, roundNum, tick)
        self.foreign = matchID

class Frame:
    def __init__(self, roundNum, tick, seconds, ctTeamName, ctEqVal, ctAlivePlayers, ctUtility, tTeamName, tEqVal, tAlivePlayers, tUtility, matchID):
        self.roundNum = roundNum
        self.tick = tick
        self.seconds = seconds
        self.ctTeamName = ctTeamName
        self.ctEqVal = ctEqVal
        self.ctAlivePlayers = ctAlivePlayers
        self.ctUtility = ctUtility
        self.tTeamName = tTeamName
        self.tEqVal = tEqVal
        self.tAlivePlayers = tAlivePlayers
        self.tUtility = tUtility
        self.foreign = matchID
        self.primary = (roundNum, tick)

class PlayerFrame:
    def __init__(self, roundNum, tick, seconds, side, teamName, steamID, name, team, x, y, z, eyeX, eyeY, eyeZ, velocityX, velocityY, velocityZ, viewX, viewY, hp, armor, activeWeapon, flashGrenades, smokeGrenades, heGrenades, fireGrenades, totalUtility, lastPlaceName, isAlive, isBot, isBlinded, isAirborne, isDucking, isDuckingInProgress, isUnDuckingInProgress, isDefusing, isPlanting, isReloading, isInBombZone, isInBuyZone, isStanding, isScoped, isWalking, isUnknown, spotters, equipmentValue, equipmentValueFreezetimeEnd, equipmentValueRoundStart, cash, cashSpendThisRound, cashSpendTotal, hasHelmet, hasDefuse, hasBomb, ping, zoomLevel, matchID, mapName):
        self.roundNum = roundNum
        self.tick = tick
        self.seconds = seconds
        self.side = side
        self.teamName = teamName
        self.steamID = steamID
        self.name = name
        self.team = team
        self.x = x
        self.y = y
        self.z = z
        self.eyeX = eyeX
        self.eyeY = eyeY
        self.eyeZ = eyeZ
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.velocityZ = velocityZ
        self.viewX = viewX
        self.viewY = viewY
        self.hp = hp
        self.armor = armor
        self.activeWeapon = activeWeapon
        self.flashGrenades = flashGrenades
        self.smokeGrenades = smokeGrenades
        self.heGrenades = heGrenades
        self.fireGrenades = fireGrenades
        self.totalUtility = totalUtility
        self.lastPlaceName = lastPlaceName
        self.isAlive = isAlive
        self.isBot = isBot
        self.isBlinded = isBlinded
        self.isAirborne = isAirborne
        self.isDucking = isDucking
        self.isDuckingInProgress = isDuckingInProgress
        self.isUnDuckingInProgress = isUnDuckingInProgress
        self.isDefusing = isDefusing
        self.isPlanting = isPlanting
        self.isReloading = isReloading
        self.isInBombZone = isInBombZone
        self.isInBuyZone = isInBuyZone
        self.isStanding = isStanding
        self.isScoped = isScoped
        self.isWalking = isWalking
        self.isUnknown = isUnknown
        self.spotters = spotters
        self.equipmentValue = equipmentValue
        self.equipmentValueFreezetimeEnd = equipmentValueFreezetimeEnd
        self.equipmentValueRoundStart = equipmentValueRoundStart
        self.cash = cash
        self.cashSpendThisRound = cashSpendThisRound
        self.cashSpendTotal = cashSpendTotal
        self.hasHelmet = hasHelmet
        self.hasDefuse = hasDefuse
        self.hasBomb = hasBomb
        self.ping = ping
        self.zoomLevel = zoomLevel
        self.matchID = matchID
        self.mapName = mapName
        self.foreign = (matchID, roundNum)
        self.primary = (matchID, roundNum, tick, steamID)

class Flash:
    def __init__(self, tick, seconds, clockTime, attackerSteamID, attackerName, attackerTeam, attackerSide, attackerX, attackerY, attackerZ, attackerViewX, attackerViewY, playerSteamID, playerName, playerTeam, playerSide, playerX, playerY, playerZ, playerViewX, playerViewY, flashDuration, roundNum, matchID, mapName):
        self.tick = tick
        self.seconds = seconds
        self.clockTime = clockTime
        self.attackerSteamID = attackerSteamID
        self.attackerName = attackerName
        self.attackerTeam = attackerTeam
        self.attackerSide = attackerSide
        self.attackerX = attackerX
        self.attackerY = attackerY
        self.attackerZ = attackerZ
        self.attackerViewX = attackerViewX
        self.attackerViewY = attackerViewY
        self.playerSteamID = playerSteamID
        self.playerName = playerName
        self.playerTeam = playerTeam
        self.playerSide = playerSide
        self.playerX = playerX
        self.playerY = playerY
        self.playerZ = playerZ
        self.playerViewX = playerViewX
        self.playerViewY = playerViewY
        self.flashDuration = flashDuration
        self.roundNum = roundNum
        self.matchID = matchID
        self.mapName = mapName
        self.primary = (matchID, roundNum, tick)
        self.foreign = matchID

class Match:
    def __init__(self, matchID, team1, team2, winner, finalScore):
        self.matchID = matchID
        self.team1 = team1
        self.team2 = team2
        self.winner = winner
        self.finalScore = finalScore

        # Primary Key
        self.primary = (matchID,)