import matplotlib.pyplot as plt
import numpy as np
import math

"""
Tully-Fisher Simulation Engine for UTQG
Authored by Amer Alaa Eldin Attia (ameralaah99@gmail.com)
"""

# Constants
G = 6.67430e-11
c = 299792458
SOLAR_MASS = 1.989e30
KPC = 3.086e19 # 1 kiloparsec in meters

def calculate_utqg_velocity(mass, r):
    L_h = 1.37e26 # Hubble Radius
    r_s = (2 * G * mass) / (c**2)
    r_0 = math.sqrt(r_s * L_h) # Dynamic Horizon
    v_newton = math.sqrt((G * mass) / r)
    # Radius-dependent boost
    boost = math.sqrt(1.0 + (r / r_0))
    return v_newton * boost

def generate_tully_fisher_plot():
    masses = np.logspace(9, 12, 50) * SOLAR_MASS
    v_max_vals = []
    
    for m in masses:
        # Calculate v at a characteristic outer radius (e.g., 50 kpc)
        v = calculate_utqg_velocity(m, 50 * KPC)
        v_max_vals.append(v / 1000) # km/s

    plt.figure(figsize=(10, 6), facecolor='#0d1117')
    ax = plt.gca()
    ax.set_facecolor('#0d1117')
    
    # Tully-Fisher is typically L (or M) vs V^4
    v_4 = [v**4 for v in v_max_vals]
    plt.loglog(masses/SOLAR_MASS, v_4, color='#79c0ff', linewidth=3, label='UTQG Prediction')
    
    plt.title('Universal Tully-Fisher Relation: Mass vs V_max^4', color='white', fontsize=14)
    plt.xlabel('Baryonic Mass (Solar Masses)', color='white')
    plt.ylabel('V_max^4 ((km/s)^4)', color='white')
    plt.grid(True, which="both", ls="-", alpha=0.1, color='white')
    plt.legend()
    plt.setp(ax.get_xticklabels(), color='white')
    plt.setp(ax.get_yticklabels(), color='white')
    
    plt.savefig('Theory_Visuals/toe_tully_fisher.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_rotation_curves():
    radii_kpc = np.linspace(1, 100, 200)
    galaxy_masses = [1e10 * SOLAR_MASS, 1e11 * SOLAR_MASS, 1e12 * SOLAR_MASS]
    labels = ['Dwarf Galaxy (10^10 M_s)', 'Spiral Galaxy (10^11 M_s)', 'Massive Galaxy (10^12 M_s)']
    colors = ['#ff7b72', '#79c0ff', '#d299ff']

    plt.figure(figsize=(10, 6), facecolor='#0d1117')
    ax = plt.gca()
    ax.set_facecolor('#0d1117')

    for m, label, color in zip(galaxy_masses, labels, colors):
        v_vals = [calculate_utqg_velocity(m, r_kpc * KPC) / 1000 for r_kpc in radii_kpc]
        plt.plot(radii_kpc, v_vals, label=label, color=color, linewidth=2)

    plt.title('UTQG Galactic Rotation Curves: The Flatness Proof', color='white', fontsize=14)
    plt.xlabel('Radius (kpc)', color='white')
    plt.ylabel('Orbital Velocity (km/s)', color='white')
    plt.ylim(0, 1000)
    plt.grid(True, which="both", ls="-", alpha=0.1, color='white')
    plt.legend()
    plt.setp(ax.get_xticklabels(), color='white')
    plt.setp(ax.get_yticklabels(), color='white')

    plt.savefig('Theory_Visuals/toe_rotation_curves.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_tully_fisher_plot()
    generate_rotation_curves()
    print("Tully-Fisher and Rotation Curve plots generated successfully.")
