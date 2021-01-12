from pathlib import Path

processed_path = Path.home().joinpath('IntraGalacticMediaService', 'Processed')
waitingtoprocess_path = Path.home().joinpath('IntraGalacticMediaService', 'WaitingToProcess')
processed_path.mkdir(parents=True, exist_ok=True )
waitingtoprocess_path.mkdir(parents=True, exist_ok=True)
