"""
Electromagnetic subject:  Vector summation
Author: Farah M Khaldi
...
"""

import numpy as np
import matplotlib.pyplot as plt    
# --- (main) ---
if __name__ == "__main__" :
    # Laws
    print("ELECTROMAGNETICS: VECTOR SUMMATION")
    print("Laws:")
    print(" Summation: R = A + B = (Ax+Bx)i + (Ay+By)j + (Az+Bz)k")
    print(" Magnitude: |R| = sqrt(Rx² + Ry² + Rz²)")
# --- function of vector corordinates ---
    def get_vec_coords(vec_id):
        print(f"\n [+500] Input Phase: {vec_id}")
        try:
                ac_x = float(input(f"  Enter {vec_id}_x: "))
                ac_y = float(input(f"  Enter {vec_id}_y: "))
                ac_z = float(input(f"  Enter {vec_id}_z: "))
                return np.array([ac_x, ac_y, ac_z])
        
        except ValueError:
                print("sorry invalid please return with numeric val")
                return get_vec_coords(vec_id)
    # Getting vectors A and B 
    A = get_vec_coords("vec_A")
    B = get_vec_coords("vec_B")

    # calculation
    res = A + B 
    mag = np.linalg.norm(res)

    # Printing the analysis
    print("\n" + "*"*20 + " Analaysis " + "*"*20)
    print(f"Vector A      : {A}")
    print(f"Vector B      : {B}")
    print(f"Result : {res}")
    print(f"Magnitude : {mag:.3f}")
    print("*"*50)
    
    # --- Vector drawing ---
    fig = plt.figure(figsize=(10, 10))
    ac = fig.add_subplot(111, projection='3d')

    # Drawing Vector A 
    ac.quiver(0,0,0, A[0], A[1], A[2], color='Black', 
              label='Vector A', arrow_length_ratio=0.4, linewidth=3)
    
    # Drawing Vector B
    ac.quiver(A[0], A[1], A[2], B[0], B[1], B[2], color='#2ecc71', 
              label='Vector B', arrow_length_ratio=0.4, linewidth=3)

    # Drawing the Result
    ac.quiver(0,0,0, res[0], res[1], res[2], 
              color='#e74c3c', label='Resultant R', linestyle='--', linewidth=3)

    # Graph
    ac.set_title("Vector Addition (Head-to-Tail Rule)", fontsize=14)
    ac.set_xlabel('X Axis'); ac.set_ylabel('Y Axis'); ac.set_zlabel('Z Axis')

   # Setting limits dynamically
    limit = max(np.abs(np.concatenate([A, B, res]))) + 1 
    ac.set_xlim([-limit, limit]); ac.set_ylim([-limit, limit]); ac.set_zlim([-limit, limit]) 
    ac.legend()
    plt.grid(True)
    print("Plot")
    plt.show()