import json
import time
import sympy as sp

def write_dict_file(harmonic_dict, filepath):
    '''
    Writes a harmonic dictionary into a .json file
    
    Args:
        filepath (str): filepath to save the .json file to
        harmonic_dict (dict): dictionary to be saved
    
    Return:
        None
    '''
    
    data_serializable = {key: str(expr) for key, expr in harmonic_dict.items()}
    with open(filepath, "w") as file:
        json.dump(
            data_serializable,
            file,
            indent=4,
            ensure_ascii=False
        )

def filter_series(terms_list, N, wt_dict):
    
    '''
    Modifies an ordered set of terms by deleting h.o.t. (i.e O(term) > O(∆E^N) and j > N)
    
    Args:
        terms_list (list): ordered terms from expanded series
        N (int): highest ordered harmonic terms to keep (e.g. up to 4th order... N = 4)
        wt_dict (dict): dictionary where the keys are the sympy representations of each concentration coefficient
                        (e.g. C_11, C_3, etc.) and the values are the weights (∆E^k) of the different harmonics (e.g. C_11 = 1, C_3 = 3)
    
    Return:
        res (list): list of filtered terms
    '''
    
    res = []
    for term in terms_list:
        
        #Dictionary with base numbers as keys and exponents as values (e.g. C_11^2 * C_24^3 * a^2 ==> keys: C_11, C_24, a; values: 2, 3, 2)
        powers_dict = term.as_powers_dict()
        exp_key = sp.exp(1) #key --> sympy representation of exponential base e
        harmonic = -1
        
        if exp_key in powers_dict:

            #Harmonic Number of Exponential
            harmonic = int(abs(powers_dict[exp_key] / (sp.I * t * w))) #determines the harmonic number j of each term

            if harmonic > N:
                continue #removes terms with exponentials greater than n (j > n)
        
        #Calculates the Total ∆E^k of each Term
        pow = 0
        for key in powers_dict:
            temp_key = str(key) #converts Sympy representation of variable to explicit string
            if temp_key in wt_dict:
                wt = wt_dict[temp_key] #∆E^k weight (e.g C_24 ==> wt = 4)
                exp = powers_dict[key] #Raised Exponent of Term (e.g. C_24^3 ==> exp = 3)
                pow += wt * exp #∆E^(k_1*exp_1) * #∆E^(k_2*exp_2) * .... #∆E^(k_i*exp_i)  ==>  k power = (k_1*exp_1) + (k_2*exp_2) + ... (k_i*exp_i)              
        if pow <= N:
            res.append(term) #Adds terms only if the summed exponents (k) is less than / equal to 'N'  
    
    return res

def sort_harmonics(filtered_terms):
        
    '''
    Sorts the different terms into respective harmonic bins via a dictionary [keys are const, 1, 2, 3, ...; values are series of terms]
    
    Args:
        filtered_terms (list): list containing the terms that have been filtered
    
    Return:
        res_dict (dict): dictionary containing the sorted terms with exponentials still attatched
    
    '''
    
    res_dict = {"const":[]}
    for term in filtered_terms:
        
        #Dictionary with base numbers as keys and exponents as values (e.g. C_11^2 * C_24^3 * a^2 ==> keys: C_11, C_24, a; values: 2, 3, 2)
        powers_dict = term.as_powers_dict()
        exp_key = sp.exp(1) #key --> sympy representation of exponential base e
        
        if exp_key in powers_dict:

            harmonic = int(abs(sp.simplify(powers_dict[exp_key] / (sp.I * t * w)))) #determines the harmonic number j of each term

            if harmonic in res_dict:
                val = res_dict[harmonic]
                res_dict[harmonic] = val + [term] #adds term to existing harmonic series
            else:
                res_dict[harmonic] = [term] #creates first term in new harmoinc series
        else:
            res_dict["const"] += [term] #adds to const bin if no harmonic contribution detected
                
    return res_dict
        

#Generating the Expansion
w, t, a, f, E, C_11, C_13,C_15, C_22, C_24,C_26, C_33,C_35, C_44,C_46,C_5,C_6, c_b = sp.symbols(r'w t a f E C_11 C_13 C_15 C_22 C_24 C_26 C_33 C_35 C_44 C_46 C_5 C_6 c_b',real=True)
sp.init_printing(use_unicode=True)

#Sympy Fraction
one_half = sp.Rational(1, 2)

E_eq = (
    one_half * (C_11 + C_13 + C_15) / c_b * (sp.exp(sp.I * w * t) + sp.exp(-sp.I * w * t)) +
    one_half * (C_22 + C_24 + C_26) / c_b * (sp.exp(2 * sp.I * w * t) + sp.exp(-2 * sp.I * w * t)) +
    one_half * (C_33 + C_35) / c_b  * (sp.exp(3 * sp.I * w * t) + sp.exp(-3 * sp.I * w * t)) +
    one_half * (C_44 + C_46) / c_b * (sp.exp(4 * sp.I * w * t) + sp.exp(-4 * sp.I * w * t)) +
    one_half * (C_5) / c_b * (sp.exp(5 * sp.I * w * t) + sp.exp(-5 * sp.I * w * t)) +
    one_half * (C_6) / c_b * (sp.exp(6 * sp.I * w * t) + sp.exp(-6 * sp.I * w * t)) 
)

inner = a*E_eq
series = (1 + E_eq) * (1 + inner + (inner)**2 + (inner)**3 + (inner)**4 + (inner)**5 + (inner)**6)

print("Beginning Expansion.")
t0 = time.time()
series_expanded = sp.expand(series)
t1 = time.time()
print(f"Expansion Completed: {round((t1-t0)/60,5)} minutes.")

print(f"Generating Terms.")
series_expanded_terms = series_expanded.as_ordered_terms()
t2 = time.time()
print(f"Generation Completed: {round((t2-t1)/60,5)} minutes.")

#Filter out Higher Order Terms
wt_dict = {
    'C_11':1,
    'C_13':3,
    'C_15':5,
    'C_22':2,
    'C_24':4,
    'C_26':6,
    'C_33':3,
    'C_35':5,
    'C_44':4,
    'C_46':6,
    'C_5':5,
    'C_6':6
}

# Removes higher order terms (>6)
print("Filtering Terms.")
filtered_terms = filter_series(series_expanded_terms,6,wt_dict)
t3 = time.time()
print(f"Filtering Completed: {round((t3-t2)/60,5)} minutes.")

#Sorts the Terms (Consts and Exponentials) into Different Harmonics (Exponentials still in terms)
harmonic_dict = sort_harmonics(filtered_terms)

#Writes Dictionary
filepath = "sixth_order_filtered_terms.json"
print("Writing dictionary to file.")
t4 = time.time()
write_dict_file(harmonic_dict,filepath)
t5 = time.time()
print(f"Dictionary Saved: {round((t5-t4)/60,5)} minutes.")
print()
print("Script complete! -------------")