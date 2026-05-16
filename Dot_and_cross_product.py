
import matplotlib
matplotlib.use('Agg') 

import numpy as np
import matplotlib.pyplot as plt

def smart_input(prompt):
    try:
        val = input(prompt).strip()
        return float(val) if val else 0.0
    except ValueError:
        return 0.0

def launch_universal_simulator():
    print("\n" + "═"*60)
    print("   UNIVERSAL VECTOR CALCULATOR (SAVING VIA AGG BACKEND)")
    print("═"*60)

    choice = input("  Choose operation (1 for Dot / 2 for Cross): ").strip()
    
    try:
        n = int(input("  How many vectors to simulate? "))
        if n < 2:
            print("[-] You need at least 2 vectors simulation!")
            return
    except: 
        return

    vectors = []
    for i in range(n):
        name = chr(65 + i)
        print(f"\n  [+] Vector {name}:")
        vectors.append(np.array([smart_input(f"    {name}_x: "), 
                                 smart_input(f"    {name}_y: "), 
                                 smart_input(f"    {name}_z: ")]))

    fig = plt.figure(figsize=(15, 9))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off() 
    ax.set_facecolor('white')

    colors = ['#E74C3C', '#3498DB', '#F1C40F', '#9B59B6', '#1ABC9C', '#E67E22']
    
    analysis_log = (
        "MATHEMATICAL ANALYSIS\n"
        "═════════════════════\n"
        "Input Vectors:\n"
    )
    for i, v in enumerate(vectors):
        analysis_log += f"  {chr(65+i)} = [{v[0]:.1f}, {v[1]:.1f}, {v[2]:.1f}]\n"
    analysis_log += "\nStep-by-Step Calculation:\n"

    all_vectors_to_scale = list(vectors)

    def draw_beautiful_arrow(ax, v, color, label, linestyle='-'):
        if np.all(v == 0): return
        length = np.linalg.norm(v)
        arrow_ratio = max(0.10, min(0.2, 1.0 / length)) if length > 0 else 0.15
        
        ax.quiver(0, 0, 0, v[0], v[1], v[2], 
                  color=color, 
                  linewidth=1.5,             # أسهم نحيفة بناءً على طلبك السابق
                  arrow_length_ratio=arrow_ratio, 
                  pivot='tail',              
                  linestyle=linestyle, 
                  label=label)

    for i, v in enumerate(vectors):
        draw_beautiful_arrow(ax, v, colors[i % len(colors)], f'Vector {chr(65+i)}')

    if choice == '1':
        title = f"Multi-Vector Dot Product Mode ({n} Vectors)"
        output_filename = "vector_dot_product.png"
        current_res = vectors[0]
        steps_text = ""
        
        for i in range(1, n):
            next_vec = vectors[i]
            if isinstance(current_res, np.ndarray):
                dot_val = np.dot(current_res, next_vec)
                steps_text += f"  Step {i}: {chr(64+i)} • {chr(65+i)} = {dot_val:.2f} (Scalar)\n"
                current_res = dot_val
            else:
                prev_val = current_res
                current_res = prev_val * next_vec
                steps_text += f"  Step {i}: {prev_val:.2f} * {chr(65+i)} = [{current_res[0]:.1f}, {current_res[1]:.1f}, {current_res[2]:.1f}]\n"
                all_vectors_to_scale.append(current_res)
        
        analysis_log += steps_text
        if isinstance(current_res, np.ndarray):
            analysis_log += f"\nFinal Result Vector:\n  [{current_res[0]:.2f}, {current_res[1]:.2f}, {current_res[2]:.2f}]"
            draw_beautiful_arrow(ax, current_res, '#2ECC71', 'Final Result', linestyle='--')
        else:
            analysis_log += f"\nFinal Result Scalar:\n  {current_res:.2f}"

    else:
        title = f"Multi-Vector Cross Product Mode ({n} Vectors)"
        output_filename = "vector_cross_product.png"
        current_vec = vectors[0]
        steps_text = ""
        
        for i in range(1, n):
            next_vec = vectors[i]
            res_cross = np.cross(current_vec, next_vec)
            steps_text += f"  Step {i}: Ans × {chr(65+i)} = [{res_cross[0]:.1f}, {res_cross[1]:.1f}, {res_cross[2]:.1f}]\n"
            current_vec = res_cross
            all_vectors_to_scale.append(current_vec)
            
        analysis_log += steps_text
        analysis_log += f"\nFinal Result Vector:\n  [{current_vec[0]:.2f}, {current_vec[1]:.2f}, {current_vec[2]:.2f}]"
        
        draw_beautiful_arrow(ax, current_vec, '#2ECC71', 'Final Result (C)')

    limit = np.max(np.abs(all_vectors_to_scale)) + 2
    ax.plot([-limit, limit], [0, 0], [0, 0], color='gray', lw=0.8, alpha=0.2) 
    ax.plot([0, 0], [-limit, limit], [0, 0], color='gray', lw=0.8, alpha=0.2) 
    
    z_limit = np.max(np.abs([v[2] for v in all_vectors_to_scale])) + 2
    ax.plot([0, 0], [0, 0], [-z_limit, z_limit], color='gray', lw=0.8, alpha=0.2) 
    
    ax.text(limit, 0, 0, " X", fontweight='bold', fontsize=11)
    ax.text(0, limit, 0, " Y", fontweight='bold', fontsize=11)
    ax.text(0, 0, z_limit, " Z", fontweight='bold', fontsize=11)

    plt.figtext(0.02, 0.15, analysis_log, fontsize=10, fontfamily='monospace', 
                bbox=dict(facecolor='#F8F9F9', edgecolor='lightgray', boxstyle='round,pad=1'))

    plt.suptitle(title, fontsize=15, fontweight='bold')
    plt.legend(loc='upper right')
    plt.subplots_adjust(left=0.38)
    
    # 🛠️ التعديل الجوهري للـ Agg: استبدال plt.show بـ plt.savefig لتجنب التحذير وحفظ الصورة بنجاح
    plt.savefig(output_filename, dpi=150) # جودة عالية 150 DPI
    plt.close() # إغلاق الـ figure لتفريغ الذاكرة
    
    print(f"\n[✔] Done! Using 'Agg' backend.")
    print(f"[📷] Image successfully saved as: '{output_filename}' in your current folder.")

if __name__ == "__main__":
    launch_universal_simulator()