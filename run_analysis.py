"""
Main script to run the complete analysis.
"""

import os
from prime_utils import generate_n_primes
from nth_prime_approx import compute_errors
from gap_analysis import analyse_mod_patterns, analyse_higher_order, compute_gaps
from visualization import (plot_gap_distribution, plot_residue_pie,
                           plot_higher_order_gaps, higher_order_gaps)

# ===== Configuration =====
N = 100_000          # number of primes to generate
SAVE_FIGURES = True  # save plots to disk
# =========================

def main():
    print(f"Generating the first {N} primes...")
    primes = generate_n_primes(N)
    print(f"Done. Largest prime = {primes[-1]}")

    # 1. nth prime approximations
    compute_errors(primes)

    # 2. Prime gaps
    gaps = compute_gaps(primes)
    print(f"\nFirst 20 gaps: {gaps[:20]}")

    # 3. Modular patterns
    analyse_mod_patterns(primes)

    # 4. Higher-order gaps
    analyse_higher_order(primes, max_order=5)

    # 5. Visualizations (optional)
    if SAVE_FIGURES:
        os.makedirs("data", exist_ok=True)

        plot_gap_distribution(gaps, bins=50,
                              title=f"Distribution of prime gaps (first {N} primes)",
                              save_path="data/gap_distribution.png")

        plot_residue_pie(gaps, modulus=6,
                         title=f"Gap residues mod 6 (first {N} primes)",
                         save_path="data/residue_mod6.png")
        plot_residue_pie(gaps, modulus=30,
                         title=f"Gap residues mod 30 (first {N} primes)",
                         save_path="data/residue_mod30.png")

        orders = [2, 3, 4, 5]
        higher_gaps = [higher_order_gaps(primes, order) for order in orders]
        plot_higher_order_gaps(higher_gaps, orders,
                               save_path="data/higher_order_gaps.png")

        print("\nPlots saved in the 'data/' directory.")

if __name__ == "__main__":
    main()
