from pathlib import Path

#def unique_path(directory, name_pattern):
#    counter = 0
#    while True:
#        counter += 1
#        path = directory / name_pattern.format(counter)
#        if not path.exists():
#            return path

#path = unique_path(Path.home().joinpath('Processed'), 'test{:03d}.txt')
#print(path)
processed_path = Path.home().joinpath('IntraGalacticMediaService', 'Processed')
waitingtoprocess_path = Path.home().joinpath('IntraGalacticMediaService', 'WaitingToProcess')
processed_path.mkdir(parents=True, exist_ok=True )
waitingtoprocess_path.mkdir(parents=True, exist_ok=True)

