# Maze Solver Configuration and Utilities
# Configuration file for different maze solving strategies

class MazeConfig:
    """Configuration class for maze solver parameters"""
    
    # Basic robot parameters
    TIMESTEP = 32
    MAX_SPEED = 6.28
    
    # Sensor thresholds (adjust based on your maze)
    WALL_THRESHOLD_CLOSE = 120
    WALL_THRESHOLD_MEDIUM = 80
    WALL_THRESHOLD_FAR = 40
    
    # Speed ratios for different maneuvers
    TURN_SPEED_RATIO = 0.8
    CORNER_SPEED_RATIO = 0.6
    WALL_FOLLOWING_SPEED = 1.0
    SEARCH_SPEED_RATIO = 0.5
    
    # Performance parameters
    DEBUG_PRINT_INTERVAL = 50  # Print debug info every N steps
    PERFORMANCE_LOG_INTERVAL = 200  # Log performance every N steps
    
    # Algorithm selection
    ALGORITHMS = {
        'LEFT_WALL': 'Left wall following (default)',
        'RIGHT_WALL': 'Right wall following',
        'PLEDGE': 'Pledge algorithm',
        'OPTIMIZED': 'Optimized adaptive algorithm'
    }
    
    # Sensor mapping (e-puck robot)
    SENSOR_POSITIONS = {
        0: 'Front-Right',
        1: 'Right',
        2: 'Back-Right', 
        3: 'Back',
        4: 'Back-Left',
        5: 'Left',
        6: 'Front-Left',
        7: 'Front'
    }

class MazeUtils:
    """Utility functions for maze solving"""
    
    @staticmethod
    def normalize_sensor_value(value, max_range=1000):
        """Normalize sensor value to 0-1 range"""
        return min(value / max_range, 1.0)
    
    @staticmethod
    def calculate_wall_distance(sensor_value):
        """Convert sensor value to approximate distance"""
        # This is a rough approximation - calibrate for your specific setup
        if sensor_value < 50:
            return "FAR"
        elif sensor_value < 100:
            return "MEDIUM" 
        else:
            return "CLOSE"
    
    @staticmethod
    def print_sensor_status(sensor_values):
        """Print formatted sensor status"""
        print("\n" + "="*50)
        print("SENSOR STATUS:")
        for i, value in enumerate(sensor_values):
            position = MazeConfig.SENSOR_POSITIONS[i]
            distance = MazeUtils.calculate_wall_distance(value)
            print(f"  {position:12}: {value:6.1f} ({distance})")
        print("="*50)
    
    @staticmethod
    def log_performance(step, action, left_speed, right_speed, elapsed_time):
        """Log performance data"""
        print(f"Step {step:4d} | {action:20} | L:{left_speed:5.2f} R:{right_speed:5.2f} | Time:{elapsed_time:6.2f}s")

# Example usage and testing
if __name__ == "__main__":
    print("Maze Solver Configuration")
    print("=" * 30)
    print(f"Timestep: {MazeConfig.TIMESTEP}ms")
    print(f"Max Speed: {MazeConfig.MAX_SPEED}")
    print(f"Available Algorithms:")
    for key, desc in MazeConfig.ALGORITHMS.items():
        print(f"  {key}: {desc}")
    
    print("\nSensor Positions:")
    for i, pos in MazeConfig.SENSOR_POSITIONS.items():
        print(f"  Sensor {i}: {pos}")
    
    # Test utility functions
    print("\nTesting utility functions:")
    test_values = [25, 75, 150, 500]
    for val in test_values:
        normalized = MazeUtils.normalize_sensor_value(val)
        distance = MazeUtils.calculate_wall_distance(val)
        print(f"  Value {val:3d} -> Normalized: {normalized:.3f}, Distance: {distance}")