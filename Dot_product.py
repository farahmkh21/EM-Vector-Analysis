import matplotlib
# تفعيل واجهة المتصفح
matplotlib.use('WebAgg') 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def smart_input(prompt):
    try:
        val = input(prompt).strip()
        return float(val) if val else 0.0
    except ValueError:
        return 0.0

def launch_multi_dot_simulator():
    print("\n" + "="*60)
    print("   MULTI-VECTOR DOT PRODUCT SIMULATOR (WEB INTERFACE)")
    print("="*60)

    try:
        n = int(input("  How many vectors to simulate? "))
    except:
        print("  [!] Invalid number.")
        return

    vectors = []
    for i in range(n):
        name = chr(65 + i)
        print(f"\n  [+] Configuring Vector {name}:")
        x = smart_input(f"    {name}_x: ")
        y = smart_input(f"    {name}_y: ")
        z = smart_input(f"    {name}_z: ")
        vectors.append(np.array([x, y, z]))

    # تجهيز الرسمة
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off() 
    ax.set_facecolor('white')

    # حسابات التحليل للوحة المعلومات
    analysis_log = "  SYSTEM ANALYSIS\n" + "="*25 + "\n"
    colors = plt.cm.rainbow(np.linspace(0, 1, n))
    
    max_mag = 5 # حد أدنى للمحاور
    
    for i in range(n):
        v = vectors[i]
        mag = np.linalg.norm(v)
        max_mag = max(max_mag, mag)
        
        # رسم المتجه
        ax.quiver(0, 0, 0, v[0], v[1], v[2], color=colors[i], lw=3, label=f'Vector {chr(65+i)}')
        analysis_log += f"  {chr(65+i)}: Mag={mag:.2f}\n"

    # حساب الـ Dot Product (بين أول متجهين كمثال أساسي أو تراكمي)
    analysis_log += "="*25 + "\n  DOT PRODUCT RESULTS:\n"
    if n >= 2:
        for j in range(n-1):
            dot_val = np.dot(vectors[j], vectors[j+1])
            analysis_log += f"  {chr(65+j)} . {chr(65+j+1)} = {dot_val:.2f}\n"
    else:
        analysis_log += "  Need 2+ vectors for Dot\n"

    # رسم المحاور المركزية (ستايل السلايدات)
    limit = max_mag + 2
    ax.plot([-limit, limit], [0, 0], [0, 0], color='black', lw=1, alpha=0.5) 
    ax.plot([0, 0], [-limit, limit], [0, 0], color='black', lw=1, alpha=0.5) 
    ax.plot([0, 0], [0, 0], [-limit, limit], color='black', lw=1, alpha=0.5) 
    ax.text(limit, 0, 0, " X")
    ax.text(0, limit, 0, " Y")
    ax.text(0, 0, limit, " Z")

    # إظهار لوحة المعلومات
    plt.figtext(0.02, 0.4, analysis_log, fontsize=10, fontfamily='monospace', 
                bbox=dict(facecolor='#FDFEFE', edgecolor='#ABB2B9', boxstyle='round,pad=1'))

    plt.suptitle("Engineering Simulation: Multi-Vector Analysis", fontsize=16, fontweight='bold')
    plt.legend()
    
    print("\n[✔] Simulation started. Check your browser.")
    plt.show()

if __name__ == "__main__":
    launch_multi_dot_simulator()