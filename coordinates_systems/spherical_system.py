import matplotlib
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt

def get_coordinate_input(label):
    """دالة رسمية لتنظيف وتفكيك المدخلات من الفراغات بدقة"""
    raw_val = input(f"  Enter {label}: ").strip()
    if ',' in raw_val:
        parts = [p.strip() for p in raw_val.split(',')]
        return [float(parts[0]), float(parts[1])]
    else:
        val = float(raw_val)
        return [val, val]

def render_spherical_system():
    print("\n" + "═"*45)
    print("      SPHERICAL COORDINATE SYSTEM")
    print("═"*45)
    
    # استقبال المتغيرات الكروية الثلاثة: r (نصف القطر)، theta (زاوية الارتفاع)، phi (الزاوية الأفقية)
    limit_r = get_coordinate_input("r (Radius)")
    limit_theta = get_coordinate_input("theta (deg, 0-180)")
    limit_phi = get_coordinate_input("phi (deg, 0-360)")
    
    # فحص التغير لكل متغير لتحديد الأبعاد الهندسية المطلوبة
    diff_r = limit_r[0] != limit_r[1]
    diff_theta = limit_theta[0] != limit_theta[1]
    diff_phi = limit_phi[0] != limit_phi[1]
    
    variable_count = sum([diff_r, diff_theta, diff_phi])

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off() # مساحة بيضاء صافية واحترافية بدون الصندوق الرمادي

    # تحديد التناسب لحجم مشهد الرسم لضمان عدم قص المنحنيات
    max_dim = max(limit_r[1], 10)
    display_limit = max_dim + (max_dim * 0.3)
    ax.set_xlim([-display_limit, display_limit])
    ax.set_ylim([-display_limit, display_limit])
    ax.set_zlim([-display_limit, display_limit])

    # رسم المحاور الإحداثية المعيارية الأساسية (X, Y, Z)
    ax.plot([-display_limit, display_limit], [0, 0], [0, 0], 'black', lw=1.2, alpha=0.4)
    ax.plot([0, 0], [-display_limit, display_limit], [0, 0], 'black', lw=1.2, alpha=0.4)
    ax.plot([0, 0], [0, 0], [-display_limit, display_limit], 'black', lw=1.5, alpha=0.6)
    ax.text(display_limit, 0, 0, "  X", fontsize=12, fontweight='bold')
    ax.text(0, display_limit, 0, "  Y", fontsize=12, fontweight='bold')
    ax.text(0, 0, display_limit, "  Z", fontsize=12, fontweight='bold')

    # --- منطق رسم الحالات الهندسية الكروية (مضمون بصرية 100%) ---
    
    # الحالة 1: قشرة كروية أو مجسم كروي (تغير الزاويتين ثيتا وفاي معاً)
    if (diff_theta and diff_phi) or variable_count == 3:
        th_vals = np.radians(np.linspace(limit_theta[0], limit_theta[1], 30))
        ph_vals = np.radians(np.linspace(limit_phi[0], limit_phi[1], 50))
        TH, PH = np.meshgrid(th_vals, ph_vals)
        
        # معادلات التحويل الرسمية من كروي إلى كارتيزي ثلاثي الأبعاد
        X_surf = limit_r[1] * np.sin(TH) * np.cos(PH)
        Y_surf = limit_r[1] * np.sin(TH) * np.sin(PH)
        Z_surf = limit_r[1] * np.cos(TH)
        
        # رسم الهيكل الشبكي الكثيف للكرة لفرض ظهورها الشفاف والأنيق
        ax.view_init(elev=20, azim=45)
        ax.plot_wireframe(X_surf, Y_surf, Z_surf, color='mediumpurple', alpha=0.4, lw=0.8)

    # الحالة 2: سطح مخروطي (تغير نصف القطر والزاوية الأفقية فاي عند زاوية ثيتا ثابتة)
    elif diff_r and diff_phi:
        r_vals = np.linspace(limit_r[0], limit_r[1], 20)
        ph_vals = np.radians(np.linspace(limit_phi[0], limit_phi[1], 50))
        R, PH = np.meshgrid(r_vals, ph_vals)
        fixed_th = np.radians(limit_theta[1])
        
        X_surf = R * np.sin(fixed_th) * np.cos(PH)
        Y_surf = R * np.sin(fixed_th) * np.sin(PH)
        Z_surf = R * np.cos(fixed_th)
        ax.plot_wireframe(X_surf, Y_surf, Z_surf, color='coral', alpha=0.4, lw=0.8)

    # الحالة 3: شريحة مسطحة مائلة عمودياً (تغير نصف القطر وثيتا عند زاوية فاي ثابتة)
    elif diff_r and diff_theta:
        r_vals = np.linspace(limit_r[0], limit_r[1], 20)
        th_vals = np.radians(np.linspace(limit_theta[0], limit_theta[1], 30))
        R, TH = np.meshgrid(r_vals, th_vals)
        fixed_ph = np.radians(limit_phi[1])
        
        X_surf = R * np.sin(TH) * np.cos(fixed_ph)
        Y_surf = R * np.sin(TH) * np.sin(fixed_ph)
        Z_surf = R * np.cos(TH)
        ax.plot_wireframe(X_surf, Y_surf, Z_surf, color='seagreen', alpha=0.4, lw=0.8)

    # الحالة 4: خط مستقيم مائل بالفراغ (إذا تغير فقط نصف القطر والزوايا ثابتة)
    elif variable_count == 1 and diff_r:
        th_fixed = np.radians(limit_theta[1])
        ph_fixed = np.radians(limit_phi[1])
        x_line = [limit_r[0] * np.sin(th_fixed) * np.cos(ph_fixed), limit_r[1] * np.sin(th_fixed) * np.cos(ph_fixed)]
        y_line = [limit_r[0] * np.sin(th_fixed) * np.sin(ph_fixed), limit_r[1] * np.sin(th_fixed) * np.sin(ph_fixed)]
        z_line = [limit_r[0] * np.cos(th_fixed), limit_r[1] * np.cos(th_fixed)]
        ax.plot(x_line, y_line, z_line, color='darkviolet', lw=3, alpha=0.8)

    # --- حساب النقطة النهائية الحقيقية للفراغ ثلاثي الأبعاد ---
    final_r = limit_r[1]
    final_th = np.radians(limit_theta[1])
    final_ph = np.radians(limit_phi[1])
    
    px = final_r * np.sin(final_th) * np.cos(final_ph)
    py = final_r * np.sin(final_th) * np.sin(final_ph)
    pz = final_r * np.cos(final_th)

    # خطوط إسقاط دقيقة للتوضيح البصري ومنع الخداع للأبعاد
    ax.plot([0, px], [0, py], [0, 0], 'green', ls='--', lw=1.2) # الإسقاط على مستوى الأرض XY
    ax.plot([px, px], [py, py], [0, pz], 'red', ls=':', lw=1.5)    # خط الارتفاع العمودي نحو النقطة

    # رسم المتجه (Vector) من نقطة الأصل للنقطة المستهدفة
    ax.quiver(0, 0, 0, px, py, pz, color='blue', lw=2.5, arrow_length_ratio=0.08, zorder=5)
    
    # رسم النقطة المرجعية الدائرية الحمراء
    ax.scatter(px, py, pz, color='red', s=150, edgecolors='black', zorder=10)
    ax.text(px, py, pz, f"  P({limit_r[1]}, {limit_theta[1]}°, {limit_phi[1]}°)", fontsize=10, fontweight='bold')

    # زاوية رؤية معيارية تبرز انحناء الكرة والعمق بكل وضوح
    ax.view_init(elev=20, azim=45)

    plt.title("Spherical Coordinate System Geometry", pad=20, fontsize=12)
    plt.savefig('spherical_output.png', bbox_inches='tight', dpi=150)
    print(f"\n✅ Render Complete. Image saved as: 'spherical_output.png'")

if __name__ == "__main__":
    render_spherical_system()