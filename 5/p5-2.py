numbers = "0123456789"
lines = []

def getMappedValue(destRangeStart, sourceRangeStart, rangeLength, target):
    if target >= sourceRangeStart and target <= sourceRangeStart + rangeLength:
        diff = target - sourceRangeStart
        return destRangeStart + diff
    return -1

def getMappedValues(ingredientMap, target):
    candidates = [getMappedValue(destRangeStart, sourceRangeStart, rangeLength, target) for destRangeStart, sourceRangeStart, rangeLength in ingredientMap]
    candidates = list(filter(lambda x: x != -1, candidates))
    result = target if not candidates else candidates[0]
    return result


def getLowestLocation(
    seedsArray,
    seedSoilMap,
    soilFertilizerMap,
    fertilizerWaterMap,
    waterLightMap,
    lightTemperatureMap,
    temperatureHumidityMap,
    humidityLocationMap):
        seedsMemo = {}
        res = float('inf')
        for i in range(0, len(seedsArray), 2):
            startSeed, endSeed = seedsArray[i], seedsArray[i+1]
            for seed in range(startSeed, startSeed + endSeed):
                if seed in seedsMemo:
                    location = seedsMemo[seed]
                else:
                    soil = getMappedValues(seedSoilMap, seed)
                    fertilizer = getMappedValues(soilFertilizerMap, soil)
                    water = getMappedValues(fertilizerWaterMap, fertilizer)
                    light = getMappedValues(waterLightMap, water)
                    temperature = getMappedValues(lightTemperatureMap, light)
                    humidity = getMappedValues(temperatureHumidityMap, temperature)
                    location = getMappedValues(humidityLocationMap, humidity)
                    seedsMemo[seed] = location
                res = min(res, location)
        return res


def convertLineToMap(line):
    return [int(n) for n in line.strip().split(' ')]


with open('input.txt', 'r') as f:
    lines = f.readlines()

_, seeds = lines[0].split(':')
seeds = [int(seed) for seed in seeds.strip().split(' ')]

# build maps
seedSoilIdx = 3
seedSoilArray = []

while lines[seedSoilIdx][0] in numbers:
    seedSoilArray.append(lines[seedSoilIdx].strip())
    seedSoilIdx += 1
seedSoilMap = [convertLineToMap(line) for line in seedSoilArray]

soilFertilizerIdx = seedSoilIdx + 2
soilFertilizerArray = []

while lines[soilFertilizerIdx][0] in numbers:
    soilFertilizerArray.append(lines[soilFertilizerIdx].strip())
    soilFertilizerIdx += 1
soilFertilizerMap = [convertLineToMap(line) for line in soilFertilizerArray]

fertilizerWaterIdx = soilFertilizerIdx + 2
fertilizerWaterArray = []

while lines[fertilizerWaterIdx][0] in numbers:
    fertilizerWaterArray.append(lines[fertilizerWaterIdx].strip())
    fertilizerWaterIdx += 1
fertilizerWaterMap = [convertLineToMap(line) for line in fertilizerWaterArray]

waterLightIdx = fertilizerWaterIdx + 2
waterLightArray = []

while lines[waterLightIdx][0] in numbers:
    waterLightArray.append(lines[waterLightIdx].strip())
    waterLightIdx += 1
waterLightMap = [convertLineToMap(line) for line in waterLightArray]

lightTemperatureIdx = waterLightIdx + 2
lightTemperatureArray = []

while lines[lightTemperatureIdx][0] in numbers:
    lightTemperatureArray.append(lines[lightTemperatureIdx].strip())
    lightTemperatureIdx += 1
lightTemperatureMap = [convertLineToMap(line) for line in lightTemperatureArray]

temperatureHumidityIdx = lightTemperatureIdx + 2
temperatureHumidityArray = []

while lines[temperatureHumidityIdx][0] in numbers:
    temperatureHumidityArray.append(lines[temperatureHumidityIdx].strip())
    temperatureHumidityIdx += 1
temperatureHumidityMap = [convertLineToMap(line) for line in temperatureHumidityArray]

humidityLocationIdx = temperatureHumidityIdx + 2
humidityLocationArray = []

while humidityLocationIdx < len(lines) and lines[humidityLocationIdx][0] in numbers:
    humidityLocationArray.append(lines[humidityLocationIdx].strip())
    humidityLocationIdx += 1
humidityLocationMap = [convertLineToMap(line) for line in humidityLocationArray]


print(getLowestLocation(seeds,
        seedSoilMap,
        soilFertilizerMap,
        fertilizerWaterMap,
        waterLightMap,
        lightTemperatureMap,
        temperatureHumidityMap,
        humidityLocationMap))

