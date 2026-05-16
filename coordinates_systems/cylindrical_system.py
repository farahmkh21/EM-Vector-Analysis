import matplotlib
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt

def get_coordinate_input(label):
    """دالة رسمية لتنظيف المدخلات من الفراغات وفصل المديات بدقة"""
    raw_val = input(f"  Enter {label}: ").strip()
    if ',' in raw_val:
        parts = [p.strip() for p in raw_val.split(',')]
        return [float(parts[0]), float(parts[1])]
    else:
        val = float(raw_val)
        return [val, val]

def render_cylindrical_system():
    print("\n" + "═"*45)
    print("      CYLINDRICAL COORDINATE SYSTEM")
    print("═"*45)
    
    # استقبال المتغيرات الثلاثة (Rho, Phi, Z)
    limit_rho = get_coordinate_input("p (Rho)")
    limit_phi = get_coordinate_input("phi (deg)")
    limit_z = get_coordinate_input("z")
    
    # فحص الحالات هندسياً لمعرفة المديات المتغيرة
    diff_rho = limit_rho[0] != limit_rho[1]
    diff_phi = limit_phi[0] != limit_phi[1]
    diff_z = limit_z[0] != limit_z[1]

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off() # مساحة بيضاء صافية واحترافية للمشاريع

    # حساب حدود مشهد الرسم للتناسب البصري المانع للقص
    max_dim = max(limit_rho[1], abs(limit_z[1]), 10)
    display_limit = max_dim + (max_dim * 0.3)
    ax.set_xlim([-display_limit, display_limit])
    ax.set_ylim([-display_limit, display_limit])
    ax.set_zlim([-display_limit, display_limit])

    # رسم المحاور الأساسية الثلاثة (X, Y, Z)
    ax.plot([-display_limit, display_limit], [0, 0], [0, 0], 'black', lw=1.2, alpha=0.4)
    ax.plot([0, 0], [-display_limit, display_limit], [0, 0], 'black', lw=1.2, alpha=0.4)
    ax.plot([0, 0], [0, 0], [-display_limit, display_limit], 'black', lw=1.5, alpha=0.6)
    ax.text(display_limit, 0, 0, "  X", fontsize=12, fontweight='bold')
    ax.text(0, display_limit, 0, "  Y", fontsize=12, fontweight='bold')
    ax.text(0, 0, display_limit, "  Z", fontsize=12, fontweight='bold')

    # --- منطق رسم المنحنيات والأقراص والأسطوانات بشكل شبكي مضمون ---
    
    # الحالة 1: أسطوانة كاملة أو قشرة جانبيّة (تغير الزاوية والارتفاع)
    if diff_phi and diff_z:
        phi_mesh = np.radians(np.linspace(limit_phi[0], limit_phi[1], 50))
        z_mesh = np.linspace(limit_z[0], limit_z[1], 25)
        P, Z = np.meshgrid(phi_mesh, z_mesh)
        X_surf = limit_rho[1] * np.cos(P)
        Y_surf = limit_rho[1] * np.sin(P)
        ax.plot_wireframe(X_surf, Y_surf, Z, color='deepskyblue', alpha=0.4, lw=0.8)
        for zv in [limit_z[0], limit_z[1]]:
            ax.plot(limit_rho[1] * np.cos(phi_mesh), limit_rho[1] * np.sin(phi_mesh), zv, color='dodgerblue', lw=1.5)

    # الحالة 2: قرص دائري مسطح / شريحة أفقية (تغير نصف القطر والزاوية) - طلبتك بالذات!
    elif diff_rho and diff_phi:
        rho_vals = np.linspace(limit_rho[0], limit_rho[1], 15)
        phi_vals = np.radians(np.linspace(limit_phi[0], limit_phi[1], 50))
        
        # رسم الحلقات الدائرية المكونة للقرص بالتوالي لمنع اختفائها بأسلوب مصفوفاتي
        for r in rho_vals:
            ax.plot(r * np.cos(phi_vals), r * np.sin(phi_vals), limit_z[1], color='orange', alpha=0.5, lw=1.0)
        # رسم أشعة نصف القطر الممتدة لتشكيل شبكة قرص ممتازة
        for p in phi_vals[::5]:
            ax.plot([limit_rho[0] * np.cos(p), limit_rho[1] * np.cos(p)],
                    [limit_rho[0] * np.sin(p), limit_rho[1] * np.sin(p)],
                    [limit_z[1], limit_z[1]], color='orange', alpha=0.5, lw=1.0)

    # الحالة 3: جدار مستوي عمودي مايل (تغير نصف القطر والارتفاع)
    elif diff_rho and diff_z:
        rho_mesh = np.linspace(limit_rho[0], limit_rho[1], 20)
        z_mesh = np.linspace(limit_z[0], limit_z[1], 20)
        R, Z = np.meshgrid(rho_mesh, z_mesh)
        fixed_phi = np.radians(limit_phi[1])
        X_surf = R * np.cos(fixed_phi)
        Y_surf = R * np.sin(fixed_phi)
        ax.plot_wireframe(X_surf, Y_surf, Z, color='magenta', alpha=0.4, lw=0.8)

    # --- حساب النقطة النهائية والمتجه الأساسي ---
    px = limit_rho[1] * np.cos(np.radians(limit_phi[1]))
    py = limit_rho[1] * np.sin(np.radians(limit_phi[1]))
    pz = limit_z[1]

    # خطوط إسقاط هندسية مساعدة لمنع الخداع البصري للعين
    ax.plot([0, px], [0, py], [0, 0], 'green', ls='--', lw=1.2) # خط نصف القطر المسقط على الأرض
    ax.plot([px, px], [py, py], [0, pz], 'red', ls=':', lw=1.5)    # خط الارتفاع العمودي Z

    # رسم السهم (Vector) الأساسي بلون أزرق واضح
    ax.quiver(0, 0, 0, px, py, pz, color='blue', lw=2.5, arrow_length_ratio=0.08, zorder=5)
    
    # رسم النقطة المرجعية المستهدفة باللون الأحمر
    ax.scatter(px, py, pz, color='red', s=150, edgecolors='black', zorder=10)
    ax.text(px, py, pz, f"  P({limit_rho[1]}, {limit_phi[1]}°, {limit_z[1]})", fontsize=10, fontweight='bold')

    # ضبط الكاميرا الفراغية على زاوية هندسية معيارية واضحة الرؤية للأبعاد
    ax.view_init(elev=20, azim=45)

    plt.title("Cylindrical Coordinate System Geometry", pad=20, fontsize=12)
    plt.savefig('cylindrical_output.png', bbox_inches='tight', dpi=150)
    print(f"\n✅ Render Complete. Image saved as: 'cylindrical_output.png'")

if __name__ == "__main__":
    render_cylindrical_system()