# Enhanced Maze Solving Logic with Improved Wall Following Algorithm
# Features: Better sensor handling, smoother movements, debugging output

from controller import Robot
import time

class MazeSolver:
    def __init__(self, robot):
        self.robot = robot
        self.timestep = 32
        self.max_speed = 6.28
        self.setup_motors()
        self.setup_sensors()
        self.debug = True
        
    def setup_motors(self):
        """Initialize and configure the robot's motors"""
        self.left_motor = self.robot.getDevice("left wheel motor")
        self.right_motor = self.robot.getDevice("right wheel motor")
        
        # Set motors to velocity control mode
        self.left_motor.setPosition(float('inf'))
        self.left_motor.setVelocity(0)
        self.right_motor.setPosition(float('inf'))
        self.right_motor.setVelocity(0)
        
    def setup_sensors(self):
        """Initialize and enable proximity sensors"""
        self.proximity_sensors = []
        for i in range(8):
            sensor_name = f'ps{i}'
            sensor = self.robot.getDevice(sensor_name)
            sensor.enable(self.timestep)
            self.proximity_sensors.append(sensor)
            
    def get_sensor_values(self):
        """Read and return all sensor values"""
        return [sensor.getValue() for sensor in self.proximity_sensors]
        
    def analyze_surroundings(self):
        """Analyze sensor data to determine robot's surroundings"""
        sensor_values = self.get_sensor_values()
        
        # Define thresholds for wall detection
        wall_threshold = 80
        corner_threshold = 80
        
        # Analyze key sensors
        front_wall = sensor_values[7] > wall_threshold or sensor_values[0] > wall_threshold
        front_right_wall = sensor_values[1] > wall_threshold
        right_wall = sensor_values[2] > wall_threshold
        back_right_wall = sensor_values[3] > wall_threshold
        back_wall = sensor_values[4] > wall_threshold
        back_left_wall = sensor_values[5] > wall_threshold
        left_wall = sensor_values[6] > wall_threshold
        front_left_wall = sensor_values[7] > wall_threshold
        
        # More sophisticated analysis
        strong_left_wall = sensor_values[5] > wall_threshold
        weak_left_wall = sensor_values[6] > corner_threshold
        
        return {
            'front_wall': front_wall,
            'left_wall': left_wall,
            'right_wall': right_wall,
            'strong_left_wall': strong_left_wall,
            'weak_left_wall': weak_left_wall,
            'sensor_values': sensor_values
        }
        
    def set_motor_speeds(self, left_speed, right_speed):
        """Set motor speeds with bounds checking"""
        left_speed = max(-self.max_speed, min(self.max_speed, left_speed))
        right_speed = max(-self.max_speed, min(self.max_speed, right_speed))
        
        self.left_motor.setVelocity(left_speed)
        self.right_motor.setVelocity(right_speed)
        
    def wall_following_logic(self, surroundings):
        """Enhanced wall following algorithm"""
        left_speed = self.max_speed
        right_speed = self.max_speed
        action = "Forward"
        
        # Priority-based decision making
        if surroundings['front_wall']:
            # If there's a wall in front, turn right
            left_speed = self.max_speed * 0.8
            right_speed = -self.max_speed * 0.8
            action = "Turn Right (Front Wall)"
            
        elif surroundings['strong_left_wall']:
            # If there's a strong left wall, go forward
            left_speed = self.max_speed
            right_speed = self.max_speed
            action = "Forward (Following Left Wall)"
            
        elif surroundings['weak_left_wall']:
            # If there's a weak left wall, slightly adjust right
            left_speed = self.max_speed
            right_speed = self.max_speed * 0.7
            action = "Slight Right (Weak Left Wall)"
            
        else:
            # No left wall detected, turn left to find wall
            left_speed = self.max_speed * 0.5
            right_speed = self.max_speed
            action = "Turn Left (Finding Wall)"
            
        return left_speed, right_speed, action
        
    def run(self):
        """Main control loop"""
        print("Starting Enhanced Maze Solver...")
        step_count = 0
        
        while self.robot.step(self.timestep) != -1:
            step_count += 1
            
            # Analyze surroundings
            surroundings = self.analyze_surroundings()
            
            # Determine action based on wall following logic
            left_speed, right_speed, action = self.wall_following_logic(surroundings)
            
            # Apply motor speeds
            self.set_motor_speeds(left_speed, right_speed)
            
            # Debug output (every 10 steps to avoid spam)
            if self.debug and step_count % 10 == 0:
                print(f"Step {step_count}: {action}")
                print(f"  Sensor values: {[f'{val:.1f}' for val in surroundings['sensor_values']]}")
                print(f"  Motor speeds: L={left_speed:.2f}, R={right_speed:.2f}")
                print("-" * 50)

def main():
    # Create robot instance
    robot = Robot()
    
    # Create and run maze solver
    maze_solver = MazeSolver(robot)
    maze_solver.run()

if __name__ == "__main__":
    main()