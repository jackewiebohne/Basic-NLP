# Readme

Here are some commonly used basic NLP and computational linguistics algorithms
Most of the file names are self-explanatory.

## keygram vec
keygram vectoriser to create n-grams (with n = window-size) for a specific target word

## collocation metrics:
All of these metrics are based on: Brezina, Statistics in Corpus Linguistics, 2018, Cambridge UP
Not all of the metrics listed in the book are implemented (they might be added in the future).

The included collocation metrics are:
- MI (mutual information)
- MI2
- MI3 
- z-score
- t_score
- corrected t-score (i.e. the t-score for a window size greater than 1; window size is collocation within a window of words >= 1)
