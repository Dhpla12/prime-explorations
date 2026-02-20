"""
Plotting functions.
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_gap_distribution(gaps, bins=50, title="Distribution of Prime Gaps",
                          save_path=None):
    plt.figure(figsize=(10, 6))
    plt.hist(gaps, bins=bins, edgecolor='black', alpha=0.7)
    plt.xlabel("Gap size")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.grid(alpha=0.3)
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()

def plot_residue_pie(gaps, modulus, title=None, save_path=None):
    residues = [g % modulus for g in gaps]
    unique, counts = np.unique(residues, return_counts=True)
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=unique, autopct='%1.1f%%', startangle=90)
    if title is None:
        title = f"Gap residues modulo {modulus}"
    plt.title(title)
    plt.axis('equal')
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()

def plot_higher_order_gaps(higher_gaps_list, orders, save_path=None):
    n_orders = len(orders)
    fig, axes = plt.subplots(1, n_orders, figsize=(5*n_orders, 4))
    if n_orders == 1:
        axes = [axes]
    for ax, gaps, order in zip(axes, higher_gaps_list, orders):
        ax.hist(gaps, bins=50, edgecolor='black', alpha=0.7)
        ax.set_title(f"Order {order} gaps")
        ax.set_xlabel("Gap size")
        ax.set_ylabel("Frequency")
        ax.grid(alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()
