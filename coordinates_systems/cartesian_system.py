import matplotlib
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt

def get_coordinate_input(label):
    """دالة لاستلام المدخلات سواء كانت قيمة ثابتة أو مدى"""
    val = input(f"  Enter {label}: ").strip().split(',')
    return [float(val[0]), float(val[1])] if len(val) > 1 else [float(val[0]), float(val[0])]

def render_cartesian_system():
    """الدالة الرئيسية لرسم النظام الكارتيزي بكافة حالاته الهندسية بدقة عالية"""
    print("\n" + "═"*45)
    print("      CARTESIAN COORDINATE SYSTEM")
    print("═"*45)
    
    # استلام القيم (x, y, z)
    limit_x = get_coordinate_input("x")
    limit_y = get_coordinate_input("y")
    limit_z = get_coordinate_input("z")
    
    # تحديد الحالات هندسياً
    diff_x = limit_x[0] != limit_x[1]
    diff_y = limit_y[0] != limit_y[1]
    diff_z = limit_z[0] != limit_z[1]
    variable_count = sum([diff_x, diff_y, diff_z])

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # شطب كل الإعدادات التلقائية للمكتبة للحصول على مساحة بيضاء صافية
    ax.set_axis_off() 

    # حساب أبعاد الرسمة الكلية للتناسب
    max_dim = max(abs(limit_x[1]), abs(limit_y[1]), abs(limit_z[1]), 10)
    display_limit = max_dim + (max_dim * 0.3)
    ax.set_xlim([-display_limit, display_limit])
    ax.set_ylim([-display_limit, display_limit])
    ax.set_zlim([-display_limit, display_limit])

    # رسم المحاور الأساسية النظيفة
    ax.plot([-display_limit, display_limit], [0, 0], [0, 0], 'black', lw=1.2, alpha=0.4) # المحور الأول
    ax.plot([0, 0], [-display_limit, display_limit], [0, 0], 'black', lw=1.2, alpha=0.4) # المحور الثاني
    ax.plot([0, 0], [0, 0], [-display_limit, display_limit], 'black', lw=1.2, alpha=0.4) # المحور الثالث

    # تسمية المحاور بخط واضح وكبير عند النهايات
    ax.text(display_limit, 0, 0, "  X", fontsize=13, fontweight='bold')
    ax.text(0, display_limit, 0, "  Y", fontsize=13, fontweight='bold')
    ax.text(0, 0, display_limit, "  Z", fontsize=13, fontweight='bold')

    # الهدف النهائي (رأس السهم والنقطة)
    px, py, pz = limit_x[1], limit_y[1], limit_z[1]

    # --- منطق الحالات الهندسيّة وصناعة العمق المنظوري ---
    
    # 1. حالة المجسم الكامل (3 متغيرات) - رسم هيكل المكعب التوضيحي ثلاثي الأبعاد
    if variable_count == 3:
        for i in [limit_x[0], limit_x[1]]:
            for j in [limit_y[0], limit_y[1]]:
                ax.plot([limit_x[0], limit_x[1]], [j, j], [i, i], 'gray', ls='--', lw=0.9, alpha=0.6)
                ax.plot([j, j], [limit_y[0], limit_y[1]], [i, i], 'gray', ls='--', lw=0.9, alpha=0.6)
                ax.plot([i, i], [j, j], [limit_z[0], limit_z[1]], 'gray', ls='--', lw=0.9, alpha=0.6)

    # 2. حالة السطح (متغيرين)
    elif variable_count == 2:
        if diff_x and diff_y: # مستوى XY
            u, v = np.meshgrid(np.linspace(limit_x[0], limit_x[1], 10), np.linspace(limit_y[0], limit_y[1], 10))
            ax.plot_surface(u, v, np.full_like(u, limit_z[0]), alpha=0.3, color='skyblue', edgecolor='navy', lw=0.5)
        elif diff_x and diff_z: # مستوى XZ
            u, v = np.meshgrid(np.linspace(limit_x[0], limit_x[1], 10), np.linspace(limit_z[0], limit_z[1], 10))
            ax.plot_surface(u, np.full_like(u, limit_y[0]), v, alpha=0.3, color='skyblue', edgecolor='navy', lw=0.5)
        elif diff_y and diff_z: # مستوى YZ
            u, v = np.meshgrid(np.linspace(limit_y[0], limit_y[1], 10), np.linspace(limit_z[0], limit_z[1], 10))
            ax.plot_surface(np.full_like(u, limit_x[0]), u, v, alpha=0.3, color='skyblue', edgecolor='navy', lw=0.5)

    # 3. حالة الخط المستقيم (متغير واحد)
    elif variable_count == 1:
        ax.plot([limit_x[0], limit_x[1]], [limit_y[0], limit_y[1]], [limit_z[0], limit_z[1]], color='blue', lw=2.5)

    # --- خطوط إسقاط الدقة (لتوضيح أبعاد النقطة ومنع التداخل البصري) ---
    if variable_count <= 1: # تفعيل الإسقاط في حالة النقطة والخط لإظهار مكانها الحقيقي
        ax.plot([px, px], [py, py], [0, pz], 'red', linestyle=':', lw=1.2, alpha=0.7) # خط عمودي إلى مستوى XY
        ax.plot([px, px], [0, py], [0, 0], 'green', linestyle=':', lw=1.2, alpha=0.7) # إسقاط إلى محور X
        ax.plot([0, px], [py, py], [0, 0], 'purple', linestyle=':', lw=1.2, alpha=0.7) # إسقاط إلى محور Y

    # رسم المتجه الأساسي (Vector) من نقطة الأصل للنقطة المستهدفة
    ax.quiver(0, 0, 0, px, py, pz, color='blue', lw=2.5, arrow_length_ratio=0.08, zorder=5)
    
    # رسم النقطة المرجعية الدائرية
    ax.scatter(px, py, pz, color='red', s=150, edgecolors='black', zorder=10)
    ax.text(px, py, pz, f"  P({px}, {py}, {pz})", fontsize=10, fontweight='bold', color='black')

    # === إجبار الكاميرا على زاوية رؤية هندسية واضحة تمنع انطباق الخطوط ===
    ax.view_init(elev=25, azim=45)

    plt.title("Cartesian Coordinate System Geometry", pad=20, fontsize=12)
    plt.savefig('cartesian_output.png', bbox_inches='tight', dpi=150)
    print(f"\n✅ Render Complete. Image saved as: 'cartesian_output.png'")

if __name__ == "__main__":
    render_cartesian_system()