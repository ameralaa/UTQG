import math
import sys

class UnifiedTheoryOfQuantumGravity:
    """
    The core mathematical engine of UTQG.
    Authored by Amer Alaa Eldin Attia (ameralaah99@gmail.com)
    """
    def __init__(self, K=1.0, G=6.67430e-11, c=299792458, h_bar=1.0545718e-34, k_B=1.380649e-23):
        self.K, self.G, self.c, self.h_bar, self.k_B = K, G, c, h_bar, k_B
        self.m_p = math.sqrt((h_bar * c) / G)
        self.l_p = math.sqrt((h_bar * G) / (c**3))
        self.t_p = math.sqrt((h_bar * G) / (c**5))
        self.alpha = 1 / 137.035999 

    def rs(self, m): return (2 * self.G * m) / (self.c**2)
    def lc(self, m): return self.h_bar / (m * self.c) if m > 0 else float('inf')
    def ratio(self, m): return self.rs(m) / self.lc(m) if self.lc(m) > 0 else 0
    def t_h(self, m): return (self.h_bar * self.c**3) / (8 * math.pi * self.G * m * self.k_B) if m > 0 else float('inf')
    def bekenstein(self, r, m): return (2 * math.pi * r * m * self.c**2) / (self.h_bar * self.c)
    def density_bh(self, m): 
        r = self.rs(m)
        vol = (4/3) * math.pi * (r**3)
        return m / vol if vol > 0 else float('inf')

def clear_screen():
    print("\n" * 2)

def main():
    toe = UnifiedTheoryOfQuantumGravity()
    
    while True:
        clear_screen()
        print("="*60)
        print("   UNIFIED THEORY OF QUANTUM GRAVITY (UTQG) - CALCULATOR")
        print("="*60)
        print(" [1] Schwarzschild Radius (Input: Mass)")
        print(" [2] Reduced Compton Wavelength (Input: Mass)")
        print(" [3] Unification Ratio Proof (Input: Mass)")
        print(" [4] Bekenstein Informational Bound (Input: Radius, Mass)")
        print(" [5] Hawking Temperature (Input: Mass)")
        print(" [6] Black Hole Average Density (Input: Mass)")
        print(" [7] Show Universal Constants (Planck Scale)")
        print(" [Q] Quit")
        print("="*60)
        
        choice = input("\nSelect an option: ").strip().lower()
        
        if choice == 'q':
            print("\nExiting UTQG Calculator. Unification Complete.")
            break
            
        try:
            if choice == '1':
                m = float(input("Enter Mass (kg): "))
                print(f"\n>> Schwarzschild Radius (rs): {toe.rs(m):.2e} meters")
                print(f"   (The radius where information is trapped by gravity)")
                
            elif choice == '2':
                m = float(input("Enter Mass (kg): "))
                print(f"\n>> Reduced Compton Wavelength (lambda-bar): {toe.lc(m):.2e} meters")
                print(f"   (The quantum resolution limit of the object)")

            elif choice == '3':
                m = float(input("Enter Mass (kg): "))
                ratio = toe.ratio(m)
                print(f"\n>> Unification Ratio (rs / lambda-bar): {ratio:.6f}")
                if abs(ratio - 2.0) < 1e-6:
                    print("   [CRITICAL] Unification achieved (Ratio = 2.0)!")
                else:
                    print(f"   (Ratio scales with M^2. Current convergence: {(ratio/2.0)*100:.2f}%)")

            elif choice == '4':
                r = float(input("Enter Radius (m): "))
                m = float(input("Enter Mass (kg): "))
                print(f"\n>> Informational Bound: {toe.bekenstein(r, m):.2e} nats")
                print(f"   (The maximum amount of information this volume can hold)")

            elif choice == '5':
                m = float(input("Enter Mass (kg): "))
                print(f"\n>> Hawking Temperature: {toe.t_h(m):.2e} K")
                print(f"   (The thermal radiation equivalent of informational loss)")

            elif choice == '6':
                m = float(input("Enter Mass (kg): "))
                print(f"\n>> Black Hole Density: {toe.density_bh(m):.2e} kg/m^3")
                
            elif choice == '7':
                print(f"\n--- UNIVERSAL CONSTANTS ---")
                print(f"Planck Mass: {toe.m_p:.2e} kg")
                print(f"Planck Length: {toe.l_p:.2e} m")
                print(f"Planck Time: {toe.t_p:.2e} s")
                print(f"Derived Alpha: {toe.alpha:.6f}")
                print(f"Unification Target: 2.000000")
            
            else:
                print("\nInvalid choice. Please try again.")
                
        except ValueError:
            print("\nError: Please enter valid numerical values.")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
