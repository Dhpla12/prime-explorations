"""
Prime gap analysis.
"""

from collections import Counter

def compute_gaps(primes):
    """Return list of gaps g_n = p_{n+1} - p_n."""
    return [primes[i+1] - primes[i] for i in range(len(primes)-1)]

def gap_residues(gaps, modulus):
    """Counter of gaps modulo modulus."""
    return Counter(g % modulus for g in gaps)

def print_residue_frequencies(gaps, modulus, expected=None):
    """Print frequency table of residues modulo modulus."""
    total = len(gaps)
    counter = gap_residues(gaps, modulus)
    residues = sorted(counter.keys())

    print(f"\nGap residues modulo {modulus} (total gaps = {total}):")
    print("-"*60)
    print(f"{'Residue':<10} {'Count':<12} {'Frequency':<12} "
          f"{'Expected':<12} {'Deviation':<12}")
    for r in residues:
        count = counter[r]
        freq = count / total * 100
        if expected:
            exp = expected.get(r, 0) * 100
            dev = freq - exp
            print(f"{r:<10} {count:<12} {freq:>6.2f}%      {exp:>6.2f}%      {dev:>+6.2f}%")
        else:
            print(f"{r:<10} {count:<12} {freq:>6.2f}%")

def higher_order_gaps(primes, order):
    """
    Compute k-th order gaps recursively.
    """
    gaps = compute_gaps(primes)
    for _ in range(2, order+1):
        gaps = [gaps[i+1] - gaps[i] for i in range(len(gaps)-1)]
    return gaps

def analyse_mod_patterns(primes):
    """Perform modular analysis for mod 6 and mod 30."""
    gaps = compute_gaps(primes)
    # Expected frequencies under random model for mod 6
    expected_mod6 = {0: 0.5, 2: 0.25, 4: 0.25}
    print_residue_frequencies(gaps, 6, expected_mod6)
    print_residue_frequencies(gaps, 30)

def analyse_higher_order(primes, max_order=5):
    """Print frequency of multiples of 6 in higher-order gaps."""
    print("\n" + "="*70)
    print("Higher-order gaps (multiples of 6 frequency)")
    print("="*70)
    for order in range(1, max_order+1):
        if len(primes) <= order:
            print(f"Not enough primes for order {order}")
            continue
        gaps = higher_order_gaps(primes, order)
        mod6 = [g % 6 for g in gaps]
        count_mod0 = mod6.count(0)
        total = len(gaps)
        perc = count_mod0 / total * 100
        print(f"Order {order}: {count_mod0:8d} / {total:8d} gaps are 0 mod 6  ({perc:.2f}%)")
    print("="*70 + "\n")
