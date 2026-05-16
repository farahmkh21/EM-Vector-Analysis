"""
Electromagnetic subject: Multi-Vector Summation (Academic Style)
Author: Farah M Khaldi - Updated for Full Axes (Positive & Negative)
"""
import matplotlib
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt

def safe_float_input(prompt_text):
    user_data = input(prompt_text).strip()
    if user_data == "":
        return 0.0
    try:
        return float(user_data)
    except ValueError:
        print("   ⚠️ Invalid input! Defaulting to 0.0")
        return 0.0

def generate_dynamic_report_img(vectors_list, vecR, magR, unitR, steps_text):
    fig = plt.figure(figsize=(16, 8), facecolor='white')
    
    # ----------------------------------------------------
    # Left Side: Pure Clean 3D Vector Space (No Box Bounds)
    # ----------------------------------------------------
    ax = fig.add_subplot(121, projection='3d')
    ax.set_axis_off() # 1. COMPLETELY REMOVE THE BOX GRID
    
    # Dynamic Scaling to give vectors breathing room
    all_coords = np.array(vectors_list + [vecR])
    max_val = np.max(np.abs(all_coords))
    limit = max(max_val * 1.4, 5)
    
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_zlim([-limit, limit])
    
    # 2. Draw Clean Centerline Reference Axes only
    ax.plot([-limit, limit], [0, 0], [0, 0], color='#94a3b8', lw=1.2, alpha=0.5) # X
    ax.plot([0, 0], [-limit, limit], [0, 0], color='#94a3b8', lw=1.2, alpha=0.5) # Y
    ax.plot([0, 0], [0, 0], [-limit, limit], color='#475569', lw=1.5, alpha=0.7) # Z
    
    ax.text(limit * 1.05, 0, 0, "  +X", fontsize=11, fontweight='bold', color='#475569')
    ax.text(0, limit * 1.05, 0, "  +Y", fontsize=11, fontweight='bold', color='#475569')
    ax.text(0, 0, limit * 1.05, "  +Z", fontsize=11, fontweight='bold', color='#1e293b')
    
    # 3. Plot individual input vectors (Tail-to-Head structure)
    colors = ['#1d4ed8', '#ea580c', '#7c3aed', '#db2777', '#0d9488']
    current_tail = np.array([0.0, 0.0, 0.0])
    
    for i, vec in enumerate(vectors_list):
        if np.linalg.norm(vec) > 0:
            c = colors[i % len(colors)]
            next_head = current_tail + vec
            
            # Solid bold vector arrow for inputs
            ax.quiver(current_tail[0], current_tail[1], current_tail[2], 
                      vec[0], vec[1], vec[2], color=c, lw=2.5, arrow_length_ratio=0.12)
            
            ax.text(next_head[0], next_head[1], next_head[2], f" V{i+1}", color=c, fontsize=9, fontweight='bold')
            current_tail = next_head
            
    # 4. DRAW THE RESULTANT VECTOR 'R' AS A DASHED LINE (خط متقطع فخم)
    # Drawing a dashed line from origin to the final point
    ax.plot([0, vecR[0]], [0, vecR[1]], [0, vecR[2]], color='#16a34a', ls='-.', lw=3, label='Resultant R')
    
    # Add a custom arrow tip at the end of the dashed line to keep it a vector
    r_norm = np.linalg.norm(vecR)
    if r_norm > 0:
        ax.quiver(vecR[0]*0.9, vecR[1]*0.9, vecR[2]*0.9, 
                  vecR[0]*0.1, vecR[1]*0.1, vecR[2]*0.1, 
                  color='#16a34a', lw=3, arrow_length_ratio=0.4)
        
    # Resultant Text Label without bounding box collision
    ax.text(vecR[0] * 1.1, vecR[1] * 1.1, vecR[2] * 1.1, 
            f"Resultant R\n({vecR[0]:.1f}, {vecR[1]:.1f}, {vecR[2]:.1f})", 
            color='#15803d', fontweight='bold', fontsize=10)
    
    # Perfect Isometric Viewing Angle matching your reference
    ax.view_init(elev=30, azim=120)
    plt.title("Vector Addition Geometric Simulator", pad=20, fontsize=13, fontweight='bold', color='#0f172a')
    
    # ----------------------------------------------------
    # Right Side: Academic Text Report Side
    # ----------------------------------------------------
    ax2 = fig.add_subplot(122)
    ax2.axis('off')
    
    plt.text(0.0, 0.95, "EM Engineering Simulator - Vector Summation", fontsize=14, fontweight='bold', color='#0f172a')
    plt.text(0.0, 0.90, f"Author: Farah M. Khaldi", fontsize=11, style='italic', color='#475569')
    ax2.plot([0.0, 0.95], [0.86, 0.86], color='black', lw=1.2)
    
    # Step 1: Breakdown
    plt.text(0.0, 0.80, "1. Mathematical Breakdown:", fontsize=11, fontweight='bold', color='#1e3a8a')
    plt.text(0.03, 0.62, steps_text, fontsize=10.5, fontname='monospace', color='#1e40af',
             bbox=dict(facecolor='#f8fafc', edgecolor='#cbd5e1', boxstyle='round,pad=0.5'))
    
    # Step 2: Formulas
    plt.text(0.0, 0.52, "2. Formulas and Calculated Invariants:", fontsize=11, fontweight='bold', color='#0f172a')
    formulas_text = (
        f" ▶ Resultant Vector Identity:\n"
        f"   R = R_x*a_x + R_y*a_y + R_z*a_z\n\n"
        f" ▶ Magnitude Formula:\n"
        f"   |R| = sqrt(R_x^2 + R_y^2 + R_z^2) = {magR:.4f}\n\n"
        f" ▶ Normalized Unit Vector:\n"
        f"   a_R = R / |R|\n"
        f"   Result: a_R = [{unitR[0]:.3f}]a_x + [{unitR[1]:.3f}]a_y + [{unitR[2]:.3f}]a_z"
    )
    plt.text(0.03, 0.22, formulas_text, fontsize=10, fontname='monospace', color='#334155')
    
    ax2.plot([0.0, 0.95], [0.16, 0.16], color='#cbd5e1', ls='--', lw=1)
    
    # Final Summary Box
    final_str = f"🎯 Total R: [{vecR[0]:.2f}, {vecR[1]:.2f}, {vecR[2]:.2f}] | Mag(|R|): {magR:.2f}"
    plt.text(0.0, 0.06, final_str, fontsize=11, fontweight='bold', color='#166534',
             bbox=dict(facecolor='#f0fdf4', edgecolor='#16a34a', boxstyle='square,pad=0.6'))
    
    plt.savefig('vector_addition_report.png', bbox_inches='tight', dpi=200)
    print(f"\n[Success] Code finished execution. Report image updated: 'vector_addition_report.png'")

def main():
    print("="*55)
    print("        DYNAMIC MULTI-VECTOR ADDITION SYSTEM")
    print("="*55)
    
    num_input = input("🔢 Enter the total number of vectors to add: ").strip()
    num_vectors = int(num_input) if num_input != "" else 1
    
    if num_vectors < 1:
        return
        
    vectors_list = []
    for i in range(num_vectors):
        print(f"\n--- Setup Vector {i+1} ---")
        v1 = safe_float_input(f"  Enter x component for Vector {i+1} = ")
        v2 = safe_float_input(f"  Enter y component for Vector {i+1} = ")
        v3 = safe_float_input(f"  Enter z component for Vector {i+1} = ")
        vectors_list.append(np.array([v1, v2, v3]))
        
    vecR = np.zeros(3)
    for vec in vectors_list:
        vecR += vec
        
    magR = np.linalg.norm(vecR)
    unitR = vecR / magR if magR != 0 else np.zeros(3)
    
    v1_steps = " + ".join([f"({v[0]})" for v in vectors_list])
    v2_steps = " + ".join([f"({v[1]})" for v in vectors_list])
    v3_steps = " + ".join([f"({v[2]})" for v in vectors_list])
    
    steps_text = (
        f" • R_x = {v1_steps} = {vecR[0]:.2f}\n"
        f" • R_y = {v2_steps} = {vecR[1]:.2f}\n"
        f" • R_z = {v3_steps} = {vecR[2]:.2f}"
    )
    
    generate_dynamic_report_img(vectors_list, vecR, magR, unitR, steps_text)

if __name__ == "__main__":
    main()