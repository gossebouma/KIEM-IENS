
Note that train_integrated.py and paths_lstm_classifier are slightly modified versions of the LexNET-2 code that worked for me:

train_integrated.py:
- gpu command line flags uitgezet 
- get_vocabulary robuust gemaakt tegen utf8 encoding errors
- load_paths etc idem

paths_lstm_classifier:
- import dynet ipv _dynet 
- changed 1 explicit reference to _dynet
- changed model = Model() to model = ParameterCollection() (as in tutorial examples)
- changed trainer.update_epochs() to trainer.update() (acc to documentation)

