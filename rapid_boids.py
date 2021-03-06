import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

boids_x = np.array([random.uniform(-450,50.0) for x in range(50)])
boids_y = np.array([random.uniform(300.0,600.0) for x in range(50)])
boid_x_velocities = np.array([random.uniform(0,10.0) for x in range(50)])
boid_y_velocities = np.array([random.uniform(-20.0,20.0) for x in range(50)])
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	xvs+=(np.sum(xs)-xs)*0.01/50
	yvs+=(np.sum(ys)-ys)*0.01/50
	# Fly away from nearby boids
	for i in range(50):
		for j in range(50):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
				xvs[i]+=(xs[i]-xs[j])
				yvs[i]+=(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(50):
		for j in range(50):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
				xvs[i]+=(xvs[j]-xvs[i])*0.125/50
				yvs[i]+=(yvs[j]-yvs[i])*0.125/50
	# Move according to velocities
	xs+=xvs
	ys+=yvs


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()