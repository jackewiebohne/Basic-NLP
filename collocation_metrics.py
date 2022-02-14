from scipy.stats.distributions import chi2
import numpy as np


class Collocation_Metrics():
    """
    class to calculate some standard collocation metrics commonly used in 
    computational linguistics. there are a few collocation metrics that are not
    included here, however.

    params::
        self.N = total tokens
        self.C = collocate frequency in total corpus
        self.W = frequency of target token
        self.WC = frequency of co-occurrence of token and collocate


    for these formulas, see Brezina: statistics in corpus linguistics, p. 72. 
    t-score corrected by window size seems to be the least extreme in 
    susceptibility to frequency and exclusivity (see ibid., p. 74)
    """
    def __init__(self,N, C, W, WC):
        self.N = N 
        self.C = C 
        self.W = W 
        self.WC = WC 
        
    def _expected(self):
        return (self.W*self.C)/self.N
    
    def _corrected_expected(self, window_size):
        return (self.W*self.C*window_size)/self.N
    
    def MI(self):
        if self._expected():
            return np.log2(self.WC/self._expected())
        else:
            return 0
    
    def MI2(self):
        if self._expected():
            return np.log2(self.WC**2/self._expected())
        else:
            return 0
    
    def MI3(self):
        if self._expected():
            return np.log2(self.WC**3/self._expected())
        else:
            return 0
    
    def z_score(self):
        if self._expected():
            return (self.C - self._expected())/np.sqrt(self._expected())
        else:
            return 0
    
    def t_score(self):
        if self.WC:
            return (self.WC - self._expected())/np.sqrt(self.WC)
        else:
            return 0
    
    def corrected_t_score(self, window_size):
        if self.WC:
            return (self.WC - self._corrected_expected(window_size))/np.sqrt(self.WC)
        else:
            return 0


def log_likelihood_corpus_cf(total_tokens_reference_corpus, total_tokens_comparison_corpus,
 target_frequency_reference, target_frequency_comparison, significance_level=0.05, verbose=True):
    """
    Conduct log-likelihood test of word frequencies between a comparison corpus and a reference corpus.
    
    params ::
        arguments are self-explanatory
        if verbose, function prints p-value and log-likelihood and states whether or not H0 should be rejected

    for source see Brezina, Statistics in Corpus Linguistics, pp. 84-5
    returns: tuple of the raw log-likelihood and the p-value at the given significance level (using chi-square approx. 
    with 1 degree of freedom)
    """
    TR = total_tokens_reference_corpus
    TC = total_tokens_comparison_corpus
    O21 = target_frequency_reference
    O11 = target_frequency_comparison
    E11 = (TC * (O11 + O21))/(TC + TR)
    E21 = (TR * (O11 + O21))/(TC + TR)
    LL = 2 * (O11 * np.log(O11/E11) + O21 * np.log(O21/E21))
    p_val = chi2.sf(LL, 1) # 1 = degree of freedom
    if verbose:
        print('Log-likelihood: ', LL, '\np < ', p_val)
        if p_val <= significance_level:
            print('reject H0')
        else:
            print('accept H0')
    return (LL, p_val)