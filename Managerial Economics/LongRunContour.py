import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


# -------------------------------
# Production function
# Q = 5 * K^0.34 * L^0.66
# -------------------------------
def production_q(K, L):
    return 5 * (K ** 0.34) * (L ** 0.66)


# Input ranges (continuous)
K = np.linspace(1, 5, 200)      # Capital
L = np.linspace(1, 10, 200)     # Labor

# Mesh + output
L_grid, K_grid = np.meshgrid(L, K)
q_grid = production_q(K_grid, L_grid)   # keep q_grid explicitly defined


# -------------------------------
# 3D Surface + filled floor contours
# with matching colors
# -------------------------------
fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(111, projection='3d')

# Shared colormap normalization so surface + floor match
norm = colors.Normalize(vmin=q_grid.min(), vmax=q_grid.max())
levels = np.linspace(q_grid.min(), q_grid.max(), 25)

# Surface ("dome") colored by q_grid
surface = ax.plot_surface(
    L_grid, K_grid, q_grid,
    cmap='viridis',
    norm=norm,
    linewidth=0,
    antialiased=True,
    edgecolor='none',
    alpha=0.95
)

# Filled contours on the floor (z = min q)
q_floor = q_grid.min()
floor_contours = ax.contourf(
    L_grid, K_grid, q_grid,
    zdir='z',
    offset=q_floor,
    levels=levels,
    cmap='viridis',
    norm=norm,
    alpha=0.95
)

# Axes labels/title
ax.set_xlabel('Labor (L)')
ax.set_ylabel('Capital (K)')
ax.set_zlabel('Output (Q)')
ax.set_title('Production Function: Q = 5·K^0.34·L^0.66\nwith Filled Floor Contours (Matching Surface Colors)')

# Limits/view
ax.set_zlim(q_floor, q_grid.max())
ax.view_init(elev=28, azim=-55)

# One shared colorbar
mappable = plt.cm.ScalarMappable(norm=norm, cmap='viridis')
mappable.set_array([])
cbar = fig.colorbar(mappable, ax=ax, shrink=0.65, pad=0.10)
cbar.set_label('Output (Q)')

plt.tight_layout()
plt.show()


# -------------------------------
# 2D Filled contour map (isoquants)
# -------------------------------
fig2, ax2 = plt.subplots(figsize=(8, 6))

cf = ax2.contourf(
    L_grid, K_grid, q_grid,
    levels=levels,
    cmap='viridis',
    norm=norm
)

cl = ax2.contour(
    L_grid, K_grid, q_grid,
    levels=levels,
    colors='k',
    linewidths=0.5
)
ax2.clabel(cl, inline=True, fontsize=8)

ax2.set_xlabel('Labor (L)')
ax2.set_ylabel('Capital (K)')
ax2.set_title('Filled Isoquants (Contours): Q = 5·K^0.34·L^0.66')

cbar2 = fig2.colorbar(cf, ax=ax2)
cbar2.set_label('Output (Q)')

plt.tight_layout()
plt.show()
