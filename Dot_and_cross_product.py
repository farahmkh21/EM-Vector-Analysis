import matplotlib
matplotlib.use('WebAgg') 

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
    print("   UNIVERSAL VECTOR CALCULATOR (DOT & CROSS)")
    print("═"*60)

    # اختيار نوع العملية
    choice = input("  Choose operation (1 for Dot / 2 for Cross): ").strip()
    
    try:
        n = int(input("  How many vectors to simulate? "))
    except: return

    vectors = []
    for i in range(n):
        name = chr(65 + i)
        print(f"\n  [+] Vector {name}:")
        vectors.append(np.array([smart_input(f"    {name}_x: "), 
                                 smart_input(f"    {name}_y: "), 
                                 smart_input(f"    {name}_z: ")]))

    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off() 
    ax.set_facecolor('white')

    # تحديد مقياس المحاور
    limit = np.max(np.abs(vectors)) + 2 if n > 0 else 5

    # رسم المحاور (ممتدة سالب وموجب - تسمية موجبة فقط)
    ax.plot([-limit, limit], [0, 0], [0, 0], color='gray', lw=1.2, alpha=0.4) 
    ax.plot([0, 0], [-limit, limit], [0, 0], color='gray', lw=1.2, alpha=0.4) 
    ax.plot([0, 0], [0, 0], [-limit, limit], color='gray', lw=1.2, alpha=0.4) 
    
    ax.text(limit, 0, 0, " X", fontweight='bold', fontsize=12)
    ax.text(0, limit, 0, " Y", fontweight='bold', fontsize=12)
    ax.text(0, 0, limit, " Z", fontweight='bold', fontsize=12)

    # رسم المتجهات
    colors = ['#E74C3C', '#3498DB', '#2ECC71', '#F1C40F', '#9B59B6']
    analysis_log = "  ANALYSIS LOG\n" + "═"*15 + "\n"

    for i, v in enumerate(vectors):
        ax.quiver(0, 0, 0, v[0], v[1], v[2], 
                  color=colors[i % len(colors)], 
                  lw=4, arrow_length_ratio=0.12, 
                  label=f'Vector {chr(65+i)}')
        analysis_log += f"  {chr(65+i)}: {v}\n"

    # حساب الناتج بناءً على الاختيار
    analysis_log += "═"*15 + "\n"
    if choice == '1':
        title = "Dot Product Mode"
        if n >= 2:
            res = np.dot(vectors[0], vectors[1])
            analysis_log += f"  A • B = {res:.2f}"
    else:
        title = "Cross Product Mode"
        if n >= 2:
            res = np.cross(vectors[0], vectors[1])
            analysis_log += f"  A × B = \n  {res}"

    # لوحة المعلومات
    plt.figtext(0.02, 0.45, analysis_log, fontsize=11, fontfamily='monospace', 
                bbox=dict(facecolor='white', edgecolor='lightgray', boxstyle='round,pad=1'))

    plt.suptitle(title, fontsize=16, fontweight='bold')
    plt.legend(loc='upper right')
    
    print(f"\n[✔] Done! Check your browser for the {title}.")
    plt.show()

if __name__ == "__main__":
    launch_universal_simulator()