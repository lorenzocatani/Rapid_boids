import numpy as np
import timeit

setup_string_bad = '''from bad_boids import update_boids
import random
boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
'''


setup_string_rapid = '''from rapid_boids import update_boids
import random
import numpy as np
boids_x = np.array([random.uniform(-450,50.0) for x in range(50)])
boids_y = np.array([random.uniform(300.0,600.0) for x in range(50)])
boid_x_velocities = np.array([random.uniform(0,10.0) for x in range(50)])
boid_y_velocities = np.array([random.uniform(-20.0,20.0) for x in range(50)])
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
'''

# Time evaluation in each strategy (bad_boids,rapid_boids ):
duration_bad_boids = timeit.timeit('update_boids(boids)',setup_string_bad,number=100)
duration_rapid_boids = timeit.timeit('update_boids(boids)',setup_string_rapid,number=100)


print 'bad_boids time is : '+str(duration_bad_boids)
print 'rapid_boids time is : '+str(duration_rapid_boids)