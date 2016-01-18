# File contains processes that need to be run to train the engine.
# Methods available include 

if argv[1] == "NYT":
	PreProcessor.scrapeNYT(argv[2],argv[3])