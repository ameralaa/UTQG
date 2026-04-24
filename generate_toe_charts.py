import matplotlib.pyplot as plt
import numpy as np
import math

"""
The core mathematical engine of UTQG.
Authored by Amer Alaa Eldin Attia (ameralaah99@gmail.com)
"""
# Use the same constants as the test suite
G = 6.67430e-11
c = 299792458
h_bar = 1.0545718e-34
k_B = 1.380649e-23

def calculate_schwarzschild_radius(mass):
    return (2 * G * mass) / (c**2)

def calculate_compton_wavelength(mass):
    return h_bar / (mass * c)

def calculate_planck_mass():
    return math.sqrt((h_bar * c) / G)

def generate_unification_chart():
    m_p = calculate_planck_mass()
    masses = np.logspace(np.log10(m_p) - 5, np.log10(m_p) + 5, 500)
    
    rs_vals = [calculate_schwarzschild_radius(m) for m in masses]
    lc_vals = [calculate_compton_wavelength(m) for m in masses]
    
    plt.figure(figsize=(10, 6), facecolor='#0d1117')
    ax = plt.gca()
    ax.set_facecolor('#0d1117')
    
    plt.loglog(masses, rs_vals, label='Schwarzschild Radius (r_s)', color='#ff7b72', linewidth=2)
    plt.loglog(masses, lc_vals, label='Compton Wavelength (λ_c)', color='#79c0ff', linewidth=2)
    
    # Intersection Point
    plt.scatter([m_p], [calculate_schwarzschild_radius(m_p)], color='#d299ff', s=100, zorder=5, label='Unification Point (Ratio = 2.0)')
    plt.annotate('2.0 Ratio', xy=(m_p, calculate_schwarzschild_radius(m_p)), xytext=(m_p*10, calculate_schwarzschild_radius(m_p)),
                 color='#d299ff', arrowprops=dict(arrowstyle='->', color='#d299ff'))

    plt.title('The Unification Proof: r_s / λ_c Convergence', color='white', fontsize=14)
    plt.xlabel('Mass (kg)', color='white')
    plt.ylabel('Length (m)', color='white')
    plt.grid(True, which="both", ls="-", alpha=0.1, color='white')
    
    legend = plt.legend()
    plt.setp(legend.get_texts(), color='white')
    
    for spine in ax.spines.values():
        spine.set_color('#30363d')
    ax.tick_params(colors='white', which='both')
    
    plt.tight_layout()
    plt.savefig('toe_unification_chart.png', dpi=300)
    print("Generated toe_unification_chart.png")

def generate_entropy_bound_chart():
    # Comparing different physical objects in S-A plane
    objects = {
        'Planck Mass': (calculate_planck_mass(), 1e-70), # Placeholder area
        'Proton': (1.67e-27, 1e-30),
        'Sun': (1.989e30, 6e18),
        'M87*': (1.3e40, 1e26),
        'Universe': (1e53, 1e53)
    }
    
    masses = [v[0] for v in objects.values()]
    labels = list(objects.keys())
    
    plt.figure(figsize=(10, 6), facecolor='#0d1117')
    ax = plt.gca()
    ax.set_facecolor('#0d1117')
    
    # Hypothetical informational complexity vs mass
    h_vals = [m * c**2 / (k_B * 300) for m in masses] # Landauer-inspired complexity
    
    plt.bar(labels, h_vals, color=['#7ee787', '#aff5b4', '#d299ff', '#ff7b72', '#79c0ff'], alpha=0.8)
    plt.yscale('log')
    plt.title('Informational Complexity Across Physical Scales', color='white', fontsize=14)
    plt.ylabel('H (nats)', color='white')
    
    for spine in ax.spines.values():
        spine.set_color('#30363d')
    ax.tick_params(colors='white')
    
    plt.tight_layout()
    plt.savefig('toe_complexity_bars.png', dpi=300)
    print("Generated toe_complexity_bars.png")

if __name__ == "__main__":
    generate_unification_chart()
    generate_entropy_bound_chart()
