# Maze Solver with Sensor Calibration and Testing Utilities
# This script helps calibrate sensors and test different movement patterns

from controller import Robot
import math

class MazeSolverTester:
    def __init__(self, robot):
        self.robot = robot
        self.timestep = 32
        self.max_speed = 6.28
        self.setup_motors()
        self.setup_sensors()
        
    def setup_motors(self):
        """Initialize motors"""
        self.left_motor = self.robot.getDevice("left wheel motor")
        self.right_motor = self.robot.getDevice("right wheel motor")
        
        self.left_motor.setPosition(float('inf'))
        self.right_motor.setPosition(float('inf'))
        self.left_motor.setVelocity(0)
        self.right_motor.setVelocity(0)
        
    def setup_sensors(self):
        """Initialize sensors"""
        self.sensors = []
        for i in range(8):
            sensor = self.robot.getDevice(f'ps{i}')
            sensor.enable(self.timestep)
            self.sensors.append(sensor)
            
    def calibrate_sensors(self, duration_steps=100):
        """Calibrate sensors by recording min/max values"""
        print("Starting sensor calibration...")
        print("Move the robot around manually to get different sensor readings")
        
        min_values = [float('inf')] * 8
        max_values = [0] * 8
        
        for step in range(duration_steps):
            self.robot.step(self.timestep)
            
            for i, sensor in enumerate(self.sensors):
                value = sensor.getValue()
                min_values[i] = min(min_values[i], value)
                max_values[i] = max(max_values[i], value)
                
            if step % 20 == 0:
                print(f"Calibration step {step}/{duration_steps}")
                
        print("\nCalibration Results:")
        print("Sensor | Min Value | Max Value | Range")
        print("-" * 40)
        for i in range(8):
            range_val = max_values[i] - min_values[i]
            print(f"  {i}    |  {min_values[i]:7.1f} |  {max_values[i]:7.1f} | {range_val:5.1f}")
            
        return min_values, max_values
        
    def test_movements(self):
        """Test basic movement patterns"""
        movements = [
            ("Forward", self.max_speed, self.max_speed, 50),
            ("Turn Left", self.max_speed * 0.5, self.max_speed, 30),
            ("Turn Right", self.max_speed, self.max_speed * 0.5, 30),
            ("Spin Right", self.max_speed, -self.max_speed, 20),
            ("Spin Left", -self.max_speed, self.max_speed, 20),
            ("Stop", 0, 0, 20)
        ]
        
        print("Testing movement patterns...")
        
        for name, left_speed, right_speed, steps in movements:
            print(f"Testing: {name}")
            
            for _ in range(steps):
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                self.robot.step(self.timestep)
                
            # Stop briefly between movements
            self.left_motor.setVelocity(0)
            self.right_motor.setVelocity(0)
            for _ in range(10):
                self.robot.step(self.timestep)
                
    def sensor_monitor(self):
        """Continuous sensor monitoring"""
        print("Starting sensor monitor mode...")
        print("Press Ctrl+C to stop monitoring")
        
        step_count = 0
        
        try:
            while self.robot.step(self.timestep) != -1:
                step_count += 1
                
                if step_count % 10 == 0:  # Print every 10 steps
                    sensor_values = [sensor.getValue() for sensor in self.sensors]
                    
                    print(f"\nStep {step_count}:")
                    print("Sensor readings:")
                    for i, value in enumerate(sensor_values):
                        direction = ["FR", "R", "BR", "B", "BL", "L", "FL", "F"][i]
                        print(f"  {direction:2}: {value:6.1f}", end="  ")
                        if (i + 1) % 4 == 0:
                            print()  # New line every 4 sensors
                            
        except KeyboardInterrupt:
            print("\nSensor monitoring stopped.")
            
    def simple_maze_solver(self):
        """Simple maze solving with detailed output"""
        print("Starting simple maze solver with detailed logging...")
        
        step_count = 0
        
        while self.robot.step(self.timestep) != -1:
            step_count += 1
            
            # Read sensors
            sensor_values = [sensor.getValue() for sensor in self.sensors]
            
            # Simple wall following logic
            front_sensor = sensor_values[7]  # Front-left sensor
            left_sensor = sensor_values[5]   # Back-left sensor
            
            wall_threshold = 80
            
            front_wall = front_sensor > wall_threshold
            left_wall = left_sensor > wall_threshold
            
            # Decision making
            if front_wall:
                # Turn right
                left_speed = self.max_speed * 0.7
                right_speed = -self.max_speed * 0.7
                action = "TURN RIGHT"
            elif left_wall:
                # Go forward
                left_speed = self.max_speed
                right_speed = self.max_speed
                action = "GO FORWARD"
            else:
                # Turn left
                left_speed = self.max_speed * 0.3
                right_speed = self.max_speed
                action = "TURN LEFT"
                
            # Apply speeds
            self.left_motor.setVelocity(left_speed)
            self.right_motor.setVelocity(right_speed)
            
            # Detailed logging every 20 steps
            if step_count % 20 == 0:
                print(f"\n--- Step {step_count} ---")
                print(f"Action: {action}")
                print(f"Front sensor: {front_sensor:.1f} ({'WALL' if front_wall else 'CLEAR'})")
                print(f"Left sensor: {left_sensor:.1f} ({'WALL' if left_wall else 'CLEAR'})")
                print(f"Motor speeds: L={left_speed:.2f}, R={right_speed:.2f}")

def main():
    """Main function with different modes"""
    robot = Robot()
    tester = MazeSolverTester(robot)
    
    # Choose mode:
    # 1. Sensor calibration
    # 2. Movement testing  
    # 3. Sensor monitoring
    # 4. Simple maze solving
    
    mode = 4  # Change this to select different modes
    
    if mode == 1:
        tester.calibrate_sensors()
    elif mode == 2:
        tester.test_movements()
    elif mode == 3:
        tester.sensor_monitor()
    elif mode == 4:
        tester.simple_maze_solver()
    else:
        print("Invalid mode selected!")

if __name__ == "__main__":
    main()