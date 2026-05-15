"""
Electromagnetic subject: Multi-Vector Summation (Academic Style)
Author: Farah M Khaldi - Updated for Full Axes (Positive & Negative)
"""
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

def launch_academic_simulator_v2():
    print("\n" + "═"*60)
    print("   FARAH KHALDI - VECTOR PRESENTATION TOOL (FULL AXES)")
    print("═"*60)

    raw_n = input("  How many vectors to simulate? (Default 0): ").strip()
    n = int(raw_n) if raw_n.isdigit() else 0

    if n == 0:
        print("  [!] No vectors to display.")
        return

    vectors = []
    for i in range(n):
        print(f"\n  [+] Vector {chr(65+i)} Configuration:")
        x = smart_input(f"    x-comp: ")
        y = smart_input(f"    y-comp: ")
        z = smart_input(f"    z-comp: ")
        vectors.append(np.array([x, y, z]))

    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    
    # --- تنظيف الرسمة (إخفاء المكعب والشبكة) ---
    ax.set_axis_off() 
    ax.set_facecolor('white')

    # --- تحديد حجم المحاور بناءً على تراكم المتجهات ---
    all_coords = np.cumsum(vectors, axis=0)
    # بناخد أقصى قيمة (مطلق) عشان المحاور تكون متساوية في الجهتين
    axis_len = max(np.max(np.abs(all_coords)), np.max(np.abs(vectors)), 5) + 2
    
    # --- رسم المحاور المركزية (موجب وسالب) ---
    # محور X (من السالب للموجب)
    ax.plot([-axis_len, axis_len], [0, 0], [0, 0], color='black', lw=1.2, alpha=0.6)
    ax.text(axis_len, 0, 0, " +X", fontsize=12, fontweight='bold')
    
    # محور Y
    ax.plot([0, 0], [-axis_len, axis_len], [0, 0], color='black', lw=1.2, alpha=0.6)
    ax.text(0, axis_len, 0, " +Y", fontsize=12, fontweight='bold')
    
    # محور Z
    ax.plot([0, 0], [0, 0], [-axis_len, axis_len], color='black', lw=1.2, alpha=0.6)
    ax.text(0, 0, axis_len, " +Z", fontsize=12, fontweight='bold')

    # --- رسم المتجهات (Head-to-Tail) ---
    curr = np.array([0.0, 0.0, 0.0])
    colors = plt.cm.Set1(np.linspace(0, 1, n))
    
    analysis_text = "  SYSTEM RESULTS\n" + "─"*20 + "\n"

    for i, v in enumerate(vectors):
        # رسم المتجه (بدءاً من نهاية اللي قبله) بسماكة ممتازة
        ax.quiver(curr[0], curr[1], curr[2], v[0], v[1], v[2], 
                  color=colors[i], lw=4, arrow_length_ratio=0.12)
        
        # إضافة اسم المتجه
        ax.text(curr[0]+v[0], curr[1]+v[1], curr[2]+v[2], f"  {chr(65+i)}", 
                color=colors[i], fontweight='bold')
        
        mag = np.linalg.norm(v)
        analysis_text += f"  {chr(65+i)}: Mag = {mag:.2f}\n"
        curr += v

    # --- رسم المحصلة النهائية (Resultant) ---
    if n > 1:
        # المحصلة بتبدأ من الصفر (0,0,0) لنهاية آخر متجه
        ax.quiver(0, 0, 0, curr[0], curr[1], curr[2], 
                  color='blue', lw=2.5, linestyle='--', arrow_length_ratio=0.1, label='Resultant')
        ax.text(curr[0], curr[1], curr[2], "  (R)", color='blue', fontweight='bold')

    # لوحة المعلومات
    analysis_text += "─"*20 + f"\n  Total R: {curr}\n  Mag(R): {np.linalg.norm(curr):.2f}"
    plt.figtext(0.02, 0.4, analysis_text, fontsize=10, fontfamily='monospace', 
                bbox=dict(facecolor='white', edgecolor='lightgray', boxstyle='round,pad=1'))

    plt.suptitle(f"EM Engineering Simulator - {n} Vector Summation\nAuthor: Farah M. Khaldi", fontsize=15)
    
    ax.view_init(elev=20, azim=45)
    
    print("\n[✔] Full Axes Mode Active. Results displayed in side panel.")
    plt.show()

if __name__ == "__main__":
    launch_academic_simulator_v2()