import matplotlib
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt

def get_coordinate_input(label):
    raw_val = input(f"  Enter {label}: ").strip()
    return float(raw_val)

def generate_transformation_report_img(path_name, inputs, laws, results):
    """Generates an academic high-quality PNG image of the laws and results"""
    fig, ax = plt.subplots(figsize=(10, 8.5), facecolor='white')
    ax.axis('off')
    
    # Header
    plt.text(0.5, 0.96, "Vector Transformation Engineering Report", fontsize=15, fontweight='bold', ha='center', color='#0f172a')
    plt.text(0.5, 0.91, f"Path: {path_name}", fontsize=12, style='italic', ha='center', color='#475569')
    ax.plot([0.05, 0.95], [0.88, 0.88], color='#0f172a', lw=1.5)
    
    # Inputs Block
    plt.text(0.05, 0.81, "1. Given Coordinate & Vector Components:", fontsize=12, fontweight='bold', color='#1e3a8a')
    in_text = "\n".join([f"   • {k}: {v}" for k, v in inputs.items()])
    plt.text(0.08, 0.71, in_text, fontsize=11, fontname='monospace', color='#1e40af',
             bbox=dict(facecolor='#f0fdf4', edgecolor='#bbf7d0', boxstyle='round,pad=0.6'))
    
    # Laws & Substitution Block
    plt.text(0.05, 0.62, "2. Transformation Equations & Substitution Steps:", fontsize=12, fontweight='bold', color='#0f172a')
    law_text = "\n\n".join([f"   ▶ {k}\n      Sub: {v}" for k, v in laws.items()])
    plt.text(0.08, 0.35, law_text, fontsize=10.5, fontname='monospace', color='#334155')
    
    ax.plot([0.05, 0.95], [0.28, 0.28], color='#cbd5e1', ls='--', lw=1)
    
    # Final Results Block
    plt.text(0.05, 0.20, "3. Final Transformed Vector Components:", fontsize=12, fontweight='bold', color='#15803d')
    res_text = f"   🎯 Resulting Vector:  A = {results}"
    plt.text(0.08, 0.10, res_text, fontsize=13, fontweight='bold', fontname='sans-serif', color='#166534',
             bbox=dict(facecolor='#f0fdf4', edgecolor='#16a34a', boxstyle='square,pad=0.8'))
    
    plt.savefig('laws_and_results.png', bbox_inches='tight', dpi=200)
    print(f"\n✅ Graphic Report saved successfully as: 'laws_and_results.png'")

def main_transformation_system():
    print("\n" + "═"*55)
    print("     THE COMPLETE 6-PATH VECTOR TRANSFORMER")
    print("═"*45)
    print("  Select Conversion Path:")
    print("  1. Cartesian to Cylindrical")
    print("  2. Cylindrical to Cartesian")
    print("  3. Cartesian to Spherical")
    print("  4. Spherical to Cartesian")
    print("  5. Cylindrical to Spherical")
    print("  6. Spherical to Cylindrical")
    choice = input("  Your Choice (1-6): ").strip()
    
    inputs, laws, final_str = {}, {}, ""
    path_titles = [
        "Cartesian to Cylindrical", "Cylindrical to Cartesian",
        "Cartesian to Spherical", "Spherical to Cartesian",
        "Cylindrical to Spherical", "Spherical to Cylindrical"
    ]
    
    if choice not in [str(i) for i in range(1, 7)]:
        print("❌ Invalid Choice!")
        return

    # --- 1. Cartesian to Cylindrical ---
    if choice == '1':
        print("\n[Input] Enter Cartesian Position:")
        x, y, z = get_coordinate_input("x"), get_coordinate_input("y"), get_coordinate_input("z")
        print("\n[Input] Enter Vector Components:")
        Ax, Ay, Az = get_coordinate_input("Ax"), get_coordinate_input("Ay"), get_coordinate_input("Az")
        
        rho = np.sqrt(x**2 + y**2)
        phi_rad = np.arctan2(y, x)
        phi_deg = np.degrees(phi_rad) % 360
        
        A_rho = Ax * np.cos(phi_rad) + Ay * np.sin(phi_rad)
        A_phi = -Ax * np.sin(phi_rad) + Ay * np.cos(phi_rad)
        
        inputs = {"Position": f"x={x}, y={y}, z={z}", "Vector": f"Ax={Ax}, Ay={Ay}, Az={Az}"}
        laws = {
            "Computed: rho = sqrt(x²+y²), phi = atan2(y,x)": f"rho={rho:.3f}, phi={phi_deg:.2f}°",
            "A_rho = Ax*cos(phi) + Ay*sin(phi)": f"{Ax}*cos({phi_deg:.1f}°) + {Ay}*sin({phi_deg:.1f}°) = {A_rho:.4f}",
            "A_phi = -Ax*sin(phi) + Ay*cos(phi)": f"-({Ax})*sin({phi_deg:.1f}°) + {Ay}*cos({phi_deg:.1f}°) = {A_phi:.4f}",
            "Az = Az (Constant)": f"{Az} = {Az:.4f}"
        }
        final_str = f"({A_rho:.3f})a_rho + ({A_phi:.3f})a_phi + ({Az:.3f})az"

    # --- 2. Cylindrical to Cartesian ---
    elif choice == '2':
        print("\n[Input] Enter Cylindrical Position:")
        rho, phi_deg, z = get_coordinate_input("Rho"), get_coordinate_input("Phi (deg)"), get_coordinate_input("z")
        print("\n[Input] Enter Vector Components:")
        A_rho, A_phi, Az = get_coordinate_input("A_rho"), get_coordinate_input("A_phi"), get_coordinate_input("Az")
        
        phi_rad = np.radians(phi_deg)
        Ax = A_rho * np.cos(phi_rad) - A_phi * np.sin(phi_rad)
        Ay = A_rho * np.sin(phi_rad) + A_phi * np.cos(phi_rad)
        
        inputs = {"Position": f"Rho={rho}, Phi={phi_deg}°, z={z}", "Vector": f"A_rho={A_rho}, A_phi={A_phi}, Az={Az}"}
        laws = {
            "Ax = A_rho*cos(phi) - A_phi*sin(phi)": f"{A_rho}*cos({phi_deg}°) - {A_phi}*sin({phi_deg}°) = {Ax:.4f}",
            "Ay = A_rho*sin(phi) + A_phi*cos(phi)": f"{A_rho}*sin({phi_deg}°) + {A_phi}*cos({phi_deg}°) = {Ay:.4f}",
            "Az = Az (Constant)": f"{Az} = {Az:.4f}"
        }
        final_str = f"({Ax:.3f})ax + ({Ay:.3f})ay + ({Az:.3f})az"

    # --- 3. Cartesian to Spherical ---
    elif choice == '3':
        print("\n[Input] Enter Cartesian Position:")
        x, y, z = get_coordinate_input("x"), get_coordinate_input("y"), get_coordinate_input("z")
        print("\n[Input] Enter Vector Components:")
        Ax, Ay, Az = get_coordinate_input("Ax"), get_coordinate_input("Ay"), get_coordinate_input("Az")
        
        r = np.sqrt(x**2 + y**2 + z**2)
        th_rad = np.arccos(z/r) if r != 0 else 0
        ph_rad = np.arctan2(y, x)
        th_deg, ph_deg = np.degrees(th_rad), np.degrees(ph_rad) % 360
        
        Ar = Ax * np.sin(th_rad) * np.cos(ph_rad) + Ay * np.sin(th_rad) * np.sin(ph_rad) + Az * np.cos(th_rad)
        A_th = Ax * np.cos(th_rad) * np.cos(ph_rad) + Ay * np.cos(th_rad) * np.sin(ph_rad) - Az * np.sin(th_rad)
        A_ph = -Ax * np.sin(ph_rad) + Ay * np.cos(ph_rad)
        
        inputs = {"Position": f"x={x}, y={y}, z={z}", "Vector": f"Ax={Ax}, Ay={Ay}, Az={Az}"}
        laws = {
            "Computed: r, theta, phi": f"r={r:.2f}, theta={th_deg:.1f}°, phi={ph_deg:.1f}°",
            "Ar = Ax*sin(th)cos(ph) + Ay*sin(th)sin(ph) + Az*cos(th)": f"= {Ar:.4f}",
            "A_theta = Ax*cos(th)cos(ph) + Ay*cos(th)sin(ph) - Az*sin(th)": f"= {A_th:.4f}",
            "A_phi = -Ax*sin(ph) + Ay*cos(ph)": f"= {A_ph:.4f}"
        }
        final_str = f"({Ar:.3f})ar + ({A_th:.3f})a_theta + ({A_ph:.3f})a_phi"

    # --- 4. Spherical to Cartesian ---
    elif choice == '4':
        print("\n[Input] Enter Spherical Position:")
        r, th_deg, ph_deg = get_coordinate_input("r"), get_coordinate_input("theta (deg)"), get_coordinate_input("phi (deg)")
        print("\n[Input] Enter Vector Components:")
        Ar, A_th, A_ph = get_coordinate_input("Ar"), get_coordinate_input("A_theta"), get_coordinate_input("A_phi")
        
        th_rad, ph_rad = np.radians(th_deg), np.radians(ph_deg)
        Ax = Ar * np.sin(th_rad) * np.cos(ph_rad) + A_th * np.cos(th_rad) * np.cos(ph_rad) - A_ph * np.sin(ph_rad)
        Ay = Ar * np.sin(th_rad) * np.sin(ph_rad) + A_th * np.cos(th_rad) * np.sin(ph_rad) + A_ph * np.cos(ph_rad)
        Az = Ar * np.cos(th_rad) - A_th * np.sin(th_rad)
        
        inputs = {"Position": f"r={r}, th={th_deg}°, ph={ph_deg}°", "Vector": f"Ar={Ar}, A_th={A_th}, A_ph={A_ph}"}
        laws = {
            "Ax = Ar*sin(th)cos(ph) + A_th*cos(th)cos(ph) - A_ph*sin(ph)": f"= {Ax:.4f}",
            "Ay = Ar*sin(th)sin(ph) + A_th*cos(th)sin(ph) + A_ph*cos(ph)": f"= {Ay:.4f}",
            "Az = Ar*cos(th) - A_th*sin(th)": f"= {Az:.4f}"
        }
        final_str = f"({Ax:.3f})ax + ({Ay:.3f})ay + ({Az:.3f})az"

    # --- 5. Cylindrical to Spherical ---
    elif choice == '5':
        print("\n[Input] Enter Cylindrical Position:")
        rho, ph_deg, z = get_coordinate_input("Rho"), get_coordinate_input("Phi (deg)"), get_coordinate_input("z")
        print("\n[Input] Enter Vector Components:")
        A_rho, A_phi, Az = get_coordinate_input("A_rho"), get_coordinate_input("A_phi"), get_coordinate_input("Az")
        
        r_pos = np.sqrt(rho**2 + z**2)
        th_rad = np.arctan2(rho, z) if r_pos != 0 else 0
        th_deg = np.degrees(th_rad)
        
        Ar = A_rho * np.sin(th_rad) + Az * np.cos(th_rad)
        A_th = A_rho * np.cos(th_rad) - Az * np.sin(th_rad)
        A_ph = A_phi
        
        inputs = {"Position": f"Rho={rho}, Phi={ph_deg}°, z={z}", "Vector": f"A_rho={A_rho}, A_phi={A_phi}, Az={Az}"}
        laws = {
            "Computed Parameter: theta = atan2(rho, z)": f"theta = {th_deg:.2f}°",
            "Ar = A_rho*sin(theta) + Az*cos(theta)": f"{A_rho}*sin({th_deg:.1f}°) + {Az}*cos({th_deg:.1f}°) = {Ar:.4f}",
            "A_theta = A_rho*cos(theta) - Az*sin(theta)": f"{A_rho}*cos({th_deg:.1f}°) - {Az}*sin({th_deg:.1f}°) = {A_th:.4f}",
            "A_phi = A_phi (Constant)": f"{A_ph:.4f} = {A_ph:.4f}"
        }
        final_str = f"({Ar:.3f})ar + ({A_th:.3f})a_theta + ({A_ph:.3f})a_phi"

    # --- 6. Spherical to Cylindrical ---
    elif choice == '6':
        print("\n[Input] Enter Spherical Position:")
        r, th_deg, ph_deg = get_coordinate_input("r"), get_coordinate_input("theta (deg)"), get_coordinate_input("phi (deg)")
        print("\n[Input] Enter Vector Components:")
        Ar, A_th, A_ph = get_coordinate_input("Ar"), get_coordinate_input("A_theta"), get_coordinate_input("A_phi")
        
        th_rad = np.radians(th_deg)
        A_rho = Ar * np.sin(th_rad) + A_th * np.cos(th_rad)
        A_phi = A_ph
        Az = Ar * np.cos(th_rad) - A_th * np.sin(th_rad)
        
        inputs = {"Position": f"r={r}, theta={th_deg}°, phi={ph_deg}°", "Vector": f"Ar={Ar}, A_theta={A_th}, A_phi={A_ph}"}
        laws = {
            "A_rho = Ar*sin(theta) + A_theta*cos(theta)": f"{Ar}*sin({th_deg}°) + {A_th}*cos({th_deg}°) = {A_rho:.4f}",
            "A_phi = A_phi (Constant)": f"{A_phi:.4f} = {A_phi:.4f}",
            "Az = Ar*cos(theta) - A_theta*sin(theta)": f"{Ar}*cos({th_deg}°) - {A_th}*sin({th_deg}°) = {Az:.4f}"
        }
        final_str = f"({A_rho:.3f})a_rho + ({A_phi:.3f})a_phi + ({Az:.3f})az"

    # Print Report on Terminal
    print("\n" + "─"*50)
    print("   MATHEMATICAL STEP-BY-STEP SOLUTION:")
    print("─"*50)
    for law, sub in laws.items():
        print(f" 🔹 Equation: {law}")
        print(f"    Result:   {sub}\n")
    print("─"*50)
    print(f"🎯 TRANSFORMED VECTOR RESULT: {final_str}")
    print("─"*50)

    # Export Graphics
    generate_transformation_report_img(path_titles[int(choice)-1], inputs, laws, final_str)

if __name__ == "__main__":
    main_transformation_system()