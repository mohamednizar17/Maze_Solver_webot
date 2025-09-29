# Advanced Maze Solver with Multiple Algorithms
# Includes: Right-hand rule, Left-hand rule, and Flood fill preparation

from controller import Robot
import math
import time
from enum import Enum

class Algorithm(Enum):
    LEFT_WALL = "left_wall"
    RIGHT_WALL = "right_wall"
    PLEDGE = "pledge"

class AdvancedMazeSolver:
    def __init__(self, robot, algorithm=Algorithm.LEFT_WALL):
        self.robot = robot
        self.algorithm = algorithm
        self.timestep = 32
        self.max_speed = 6.28
        self.setup_motors()
        self.setup_sensors()
        
        # Algorithm-specific variables
        self.pledge_angle = 0  # For Pledge algorithm
        self.total_rotation = 0
        
        # Performance tracking
        self.start_time = time.time()
        self.steps_taken = 0
        self.walls_followed = 0
        
    def setup_motors(self):
        """Initialize motors"""
        self.left_motor = self.robot.getDevice("left wheel motor")
        self.right_motor = self.robot.getDevice("right wheel motor")
        
        self.left_motor.setPosition(float('inf'))
        self.right_motor.setPosition(float('inf'))
        self.left_motor.setVelocity(0)
        self.right_motor.setVelocity(0)
        
    def setup_sensors(self):
        """Initialize proximity sensors"""
        self.sensors = []
        for i in range(8):
            sensor = self.robot.getDevice(f'ps{i}')
            sensor.enable(self.timestep)
            self.sensors.append(sensor)
            
    def get_sensor_readings(self):
        """Get normalized sensor readings"""
        readings = [sensor.getValue() for sensor in self.sensors]
        # Normalize readings to 0-1 range
        normalized = [min(reading / 1000.0, 1.0) for reading in readings]
        return normalized
        
    def detect_walls(self):
        """Detect walls around the robot"""
        readings = self.get_sensor_readings()
        threshold = 0.08  # Adjust based on your sensor calibration
        
        return {
            'front_right': readings[0] > threshold or readings[1] > threshold,
            'right': readings[2] > threshold,
            'back_right': readings[3] > threshold,
            'back': readings[4] > threshold,
            'back_left': readings[5] > threshold,
            'left': readings[6] > threshold,
            'front_left': readings[7] > threshold,
            'front': readings[7] > threshold or readings[0] > threshold
        }
        
    def left_wall_following(self, walls):
        """Left-hand rule implementation"""
        left_speed = self.max_speed
        right_speed = self.max_speed
        
        if walls['front']:
            # Turn right when blocked
            left_speed = self.max_speed * 0.8
            right_speed = -self.max_speed * 0.8
            self.total_rotation += 90
            
        elif walls['left']:
            # Go forward when wall on left
            left_speed = self.max_speed
            right_speed = self.max_speed
            self.walls_followed += 1
            
        elif walls['front_left']:
            # Slight right turn to maintain distance from wall
            left_speed = self.max_speed
            right_speed = self.max_speed * 0.6
            
        else:
            # Turn left to find wall
            left_speed = self.max_speed * 0.4
            right_speed = self.max_speed
            self.total_rotation -= 45
            
        return left_speed, right_speed
        
    def right_wall_following(self, walls):
        """Right-hand rule implementation"""
        left_speed = self.max_speed
        right_speed = self.max_speed
        
        if walls['front']:
            # Turn left when blocked
            left_speed = -self.max_speed * 0.8
            right_speed = self.max_speed * 0.8
            self.total_rotation -= 90
            
        elif walls['right']:
            # Go forward when wall on right
            left_speed = self.max_speed
            right_speed = self.max_speed
            self.walls_followed += 1
            
        elif walls['front_right']:
            # Slight left turn to maintain distance from wall
            left_speed = self.max_speed * 0.6
            right_speed = self.max_speed
            
        else:
            # Turn right to find wall
            left_speed = self.max_speed
            right_speed = self.max_speed * 0.4
            self.total_rotation += 45
            
        return left_speed, right_speed
        
    def pledge_algorithm(self, walls):
        """Pledge algorithm - combination of wall following and angle tracking"""
        if abs(self.total_rotation) < 10:  # Close to original heading
            # Move straight when possible
            if not walls['front']:
                return self.max_speed, self.max_speed
                
        # Use left wall following when not at original heading
        return self.left_wall_following(walls)
        
    def set_motor_velocities(self, left_speed, right_speed):
        """Set motor velocities with safety bounds"""
        left_speed = max(-self.max_speed, min(self.max_speed, left_speed))
        right_speed = max(-self.max_speed, min(self.max_speed, right_speed))
        
        self.left_motor.setVelocity(left_speed)
        self.right_motor.setVelocity(right_speed)
        
    def get_algorithm_name(self):
        """Get human-readable algorithm name"""
        names = {
            Algorithm.LEFT_WALL: "Left Wall Following",
            Algorithm.RIGHT_WALL: "Right Wall Following", 
            Algorithm.PLEDGE: "Pledge Algorithm"
        }
        return names.get(self.algorithm, "Unknown")
        
    def print_status(self):
        """Print current status and performance metrics"""
        elapsed_time = time.time() - self.start_time
        print(f"\n=== Maze Solver Status ===")
        print(f"Algorithm: {self.get_algorithm_name()}")
        print(f"Steps taken: {self.steps_taken}")
        print(f"Walls followed: {self.walls_followed}")
        print(f"Total rotation: {self.total_rotation:.1f}°")
        print(f"Elapsed time: {elapsed_time:.2f}s")
        print(f"========================\n")
        
    def run(self):
        """Main execution loop"""
        print(f"Starting Advanced Maze Solver with {self.get_algorithm_name()}")
        
        while self.robot.step(self.timestep) != -1:
            self.steps_taken += 1
            
            # Detect surrounding walls
            walls = self.detect_walls()
            
            # Choose algorithm
            if self.algorithm == Algorithm.LEFT_WALL:
                left_speed, right_speed = self.left_wall_following(walls)
            elif self.algorithm == Algorithm.RIGHT_WALL:
                left_speed, right_speed = self.right_wall_following(walls)
            elif self.algorithm == Algorithm.PLEDGE:
                left_speed, right_speed = self.pledge_algorithm(walls)
                
            # Apply motor speeds
            self.set_motor_velocities(left_speed, right_speed)
            
            # Print status every 100 steps
            if self.steps_taken % 100 == 0:
                self.print_status()

def main():
    """Main function - choose your algorithm here"""
    robot = Robot()
    
    # Choose algorithm: LEFT_WALL, RIGHT_WALL, or PLEDGE
    chosen_algorithm = Algorithm.LEFT_WALL
    
    maze_solver = AdvancedMazeSolver(robot, chosen_algorithm)
    maze_solver.run()

if __name__ == "__main__":
    main()