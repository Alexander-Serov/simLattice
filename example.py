"""
For more details on this simulation, see https://arxiv.org/abs/1903.03048 , Appendix A7.
To launch this example go to the parent folder in the terminal and type

`python3 -m simLattice.example`

You can modify the following parameters (with units) in the file below:

N   -   number of jumps
L (um) - side of the simulated region,
Rmin, Rmax (um) - the minimal and maximal radii of the beads (peaked in middle of L along x; no changes along y),
D (um^2/s) - uniform microscopic diffusivity,
dt (s)  -   time step,
beads_dx, beads_dy (um) - beads lattice step along x and y (distance between the beads),
internal_steps_number   -   number of internal time steps simulated internally in-between dt.

By default, this example plots the beads and the trajectory. You can modify the parameters or save figures in files by uncomenting the lines.
"""


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from .plot import plot_beads
from .simulate import simulate

# matplotlib.use('Agg')

# Change these parameters
N = 100
L = 10
D = 1
Rmin = 1e-3
Rmax = 15e-3
dt = 1e-4
beads_dx = 0.04
beads_dy = 0.04
internal_steps_number = 1

# Other parameters
pagewidth_in = 6.85
page_width_frac = 1 / 3
dpi = 100
font_size = 8

# Simulate a trajectory
np.random.seed()
ts, rs, drs, beads, all_internal_trajectory = simulate(
    N=N, L=L, Rmin=Rmin, Rmax=Rmax, D=D, dt=dt, beads_dx=beads_dx, beads_dy=beads_dy, internal_steps_number=internal_steps_number)
all_internal_trajectory = np.array(all_internal_trajectory)

# Plot the results
matplotlib.rcParams.update({'font.size': font_size})
fig, ax = plt.subplots(num=1, clear=True)
figsize = np.asarray([3.0, 1.0]) * page_width_frac * pagewidth_in  # in inches

plot_beads(beads, figure=fig)
plt.scatter(rs[0, 0], rs[0, 1], color='g', s=4)  # plot jump points
for i in range(rs.shape[0] - 1):
    plt.plot([rs[i, 0], rs[i, 0] + drs[i, 0]], [rs[i, 1], rs[i, 1] + drs[i, 1]], '-r', lw=0.5)
    # plt.plot([rs[i, 0], rs[i + 1, 0]], [rs[i, 1], rs[i + 1, 1]], 'r')
# plt.plot(all_internal_trajectory[:, 0], all_internal_trajectory[:, 1], 'b')   # can show full internal trajectory

plt.xlabel(r'$x, \mu\mathrm{m}$')
plt.ylabel(r'$y, \mu\mathrm{m}$')

# r0 = [0.4, 0.8]
# dw = 1.0
# plt.xlim([r0[0], r0[0] + dw])
# plt.ylim([r0[1], r0[1] + dw])
ax.set_aspect('equal')

fig.set_dpi(dpi)
fig.set_figwidth(figsize[0])
fig.set_figheight(figsize[1])

plt.show()
figname = 'simulation_setup'

# fig.savefig(figname + '.pdf', bbox_inches='tight', pad_inches=0)

plt.xlim([0, L])
plt.ylim([0, L])
ax.set_aspect('equal')
# fig.savefig(figname + '-full.pdf', bbox_inches='tight', pad_inches=0)
