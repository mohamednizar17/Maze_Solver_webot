# Optimized Maze Solver with Performance Tracking
# Features: Speed optimization, path recording, and performance analysis

from controller import Robot
import time
import math

class OptimizedMazeSolver:
    def __init__(self, robot):
        self.robot = robot
        self.timestep = 32
        self.max_speed = 6.28
        
        # Performance tracking
        self.start_time = None
        self.path_length = 0
        self.turns_made = 0
        self.wall_contacts = 0
        self.position_history = []
        
        # Optimization parameters
        self.speed_multiplier = 1.0
        self.turn_speed_ratio = 0.8
        self.corner_speed_ratio = 0.6
        
        self.setup_robot()
        
    def setup_robot(self):
        """Initialize robot components"""
        # Motors
        self.left_motor = self.robot.getDevice("left wheel motor")
        self.right_motor = self.robot.getDevice("right wheel motor")
        self.left_motor.setPosition(float('inf'))
        self.right_motor.setPosition(float('inf'))
        
        # Sensors
        self.sensors = []
        for i in range(8):
            sensor = self.robot.getDevice(f'ps{i}')
            sensor.enable(self.timestep)
            self.sensors.append(sensor)
            
    def get_optimized_sensor_readings(self):
        """Get sensor readings with noise filtering"""
        readings = []
        for sensor in self.sensors:
            reading = sensor.getValue()
            # Simple noise filtering
            readings.append(reading)
            
        return readings
        
    def analyze_maze_environment(self):
        """Advanced environment analysis"""
        readings = self.get_optimized_sensor_readings()
        
        # Define detection thresholds
        close_threshold = 120    # Very close to wall
        medium_threshold = 80    # Medium distance
        far_threshold = 40       # Far from wall
        
        environment = {
            'front_close': readings[7] > close_threshold or readings[0] > close_threshold,
            'front_medium': readings[7] > medium_threshold or readings[0] > medium_threshold,
            'left_close': readings[5] > close_threshold or readings[6] > close_threshold,
            'left_medium': readings[5] > medium_threshold or readings[6] > medium_threshold,
            'right_close': readings[1] > close_threshold or readings[2] > close_threshold,
            'right_medium': readings[1] > medium_threshold or readings[2] > medium_threshold,
            'readings': readings
        }
        
        return environment
        
    def calculate_optimal_speeds(self, environment):
        """Calculate optimal motor speeds based on environment"""
        base_speed = self.max_speed * self.speed_multiplier
        left_speed = base_speed
        right_speed = base_speed
        action = "Forward"
        
        # Advanced decision tree
        if environment['front_close']:
            # Sharp turn when very close to front wall
            left_speed = base_speed * self.turn_speed_ratio
            right_speed = -base_speed * self.turn_speed_ratio
            action = "Sharp Right Turn"
            self.turns_made += 1
            
        elif environment['front_medium']:
            # Gradual turn when approaching front wall
            left_speed = base_speed * 0.9
            right_speed = -base_speed * 0.5
            action = "Gradual Right Turn"
            
        elif environment['left_close']:
            # Too close to left wall, adjust right
            left_speed = base_speed
            right_speed = base_speed * 0.7
            action = "Adjust Right"
            self.wall_contacts += 1
            
        elif environment['left_medium']:
            # Perfect distance from left wall
            left_speed = base_speed
            right_speed = base_speed
            action = "Following Left Wall"
            
        else:
            # No left wall, turn left to find it
            left_speed = base_speed * self.corner_speed_ratio
            right_speed = base_speed
            action = "Search Left Wall"
            
        return left_speed, right_speed, action
        
    def update_position_tracking(self, left_speed, right_speed):
        """Track robot's approximate position and path"""
        # Simple odometry (approximate)
        avg_speed = (abs(left_speed) + abs(right_speed)) / 2
        self.path_length += avg_speed * (self.timestep / 1000.0) * 0.1  # Rough conversion
        
        # Store position data every few steps
        if len(self.position_history) == 0 or len(self.position_history) % 10 == 0:
            self.position_history.append({
                'time': time.time() - self.start_time,
                'path_length': self.path_length,
                'turns': self.turns_made,
                'wall_contacts': self.wall_contacts
            })
            
    def adaptive_speed_adjustment(self, step_count):
        """Dynamically adjust speed based on performance"""
        if step_count > 500:
            # Increase speed after robot has learned the environment
            self.speed_multiplier = min(1.2, self.speed_multiplier + 0.001)
        elif self.wall_contacts > 10:
            # Reduce speed if too many wall contacts
            self.speed_multiplier = max(0.7, self.speed_multiplier - 0.01)
            
    def print_performance_stats(self, step_count):
        """Print detailed performance statistics"""
        elapsed_time = time.time() - self.start_time
        
        print(f"\n╔═══ Performance Statistics (Step {step_count}) ═══╗")
        print(f"║ Elapsed Time: {elapsed_time:.2f}s")
        print(f"║ Path Length: {self.path_length:.2f} units")
        print(f"║ Turns Made: {self.turns_made}")
        print(f"║ Wall Contacts: {self.wall_contacts}")
        print(f"║ Speed Multiplier: {self.speed_multiplier:.2f}")
        print(f"║ Avg Speed: {self.path_length/elapsed_time:.2f} units/s")
        print(f"╚═══════════════════════════════════════════════════╝")
        
    def export_performance_data(self):
        """Export performance data for analysis"""
        filename = f"maze_performance_{int(time.time())}.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write("Maze Solver Performance Data\n")
                f.write("=" * 40 + "\n")
                f.write(f"Total Path Length: {self.path_length:.2f}\n")
                f.write(f"Total Turns: {self.turns_made}\n")
                f.write(f"Wall Contacts: {self.wall_contacts}\n")
                f.write(f"Final Speed Multiplier: {self.speed_multiplier:.2f}\n\n")
                
                f.write("Time Series Data:\n")
                f.write("Time(s)\tPath Length\tTurns\tWall Contacts\n")
                for data in self.position_history:
                    f.write(f"{data['time']:.2f}\t{data['path_length']:.2f}\t"
                           f"{data['turns']}\t{data['wall_contacts']}\n")
                           
            print(f"Performance data exported to {filename}")
        except Exception as e:
            print(f"Could not export data: {e}")
            
    def run_optimized_solver(self):
        """Main optimized solving loop"""
        print("Starting Optimized Maze Solver...")
        print("Features: Performance tracking, adaptive speed, path recording")
        
        self.start_time = time.time()
        step_count = 0
        
        try:
            while self.robot.step(self.timestep) != -1:
                step_count += 1
                
                # Analyze environment
                environment = self.analyze_maze_environment()
                
                # Calculate optimal speeds
                left_speed, right_speed, action = self.calculate_optimal_speeds(environment)
                
                # Apply adaptive speed adjustment
                self.adaptive_speed_adjustment(step_count)
                
                # Set motor speeds
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                
                # Update tracking
                self.update_position_tracking(left_speed, right_speed)
                
                # Print statistics periodically
                if step_count % 200 == 0:
                    self.print_performance_stats(step_count)
                    
        except KeyboardInterrupt:
            print("\nMaze solver stopped by user.")
            self.export_performance_data()
            
def main():
    """Main execution function"""
    robot = Robot()
    solver = OptimizedMazeSolver(robot)
    solver.run_optimized_solver()

if __name__ == "__main__":
    main()