helpMessage = ""

def sendHelp():
  greet = "Welcome to NewsBot! I envision sharing with you the top 5 latest news from various news souce :)"
  currentSources = "Current, we have the following sources:\n1. CNA"
  functions = "To accesss the news sources, you can use the following handlers\n1. /get_cna"

  helpMessage = greet + "\n\n" + currentSources + "\n\n" + functions

  return helpMessage
