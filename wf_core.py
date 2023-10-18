import os
from wf_datagen import manualWebScrape
from wf_visualization import visualization

manualWebScrape("data_processed/funds.csv")

fundsFiles = os.listdir(path='.\\data_original\\funds')
visualization(fundsFiles)