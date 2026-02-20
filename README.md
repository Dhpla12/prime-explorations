# Prime Explorations

Code accompanying the paper *Exploring Approximations and Patterns in Prime Numbers: A Self-Directed Computational Inquiry* by Aradhya Haldikar.

## Files

- `prime_utils.py`       – Prime generation utilities (optimised trial division, sieve)
- `nth_prime_approx.py`  – Evaluation of approximations for the n‑th prime
- `gap_analysis.py`      – Prime gap analysis (residues, higher‑order gaps)
- `visualization.py`     – Plotting functions
- `run_analysis.py`      – Main script that runs the complete analysis

## Requirements

- Python ≥ 3.7
- NumPy
- Matplotlib

Install with: `pip install -r requirements.txt`

## Usage

Run `python run_analysis.py`.  
Edit `N` in that file to change the number of primes generated (default 100,000).  
Figures are saved in the `data/` folder if `SAVE_FIGURES = True`.
