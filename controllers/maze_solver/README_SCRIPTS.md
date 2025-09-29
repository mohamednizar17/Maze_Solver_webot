# Maze Solving Robot Scripts Collection

This collection provides multiple enhanced versions of your original maze-solving robot, each with different features and capabilities.

## 📁 File Overview

### Original Script
- `maze_solver.py` - Your original wall-following implementation

### Enhanced Scripts

#### 1. `enhanced_maze_solver.py` 
**Features:**
- Object-oriented design with clean code structure
- Improved sensor analysis with multiple thresholds
- Better motor control with bounds checking
- Debug output with detailed logging
- Smoother wall-following behavior

**Use when:** You want a cleaner, more maintainable version of your original script.

#### 2. `advanced_maze_solver.py`
**Features:**
- Multiple algorithms: Left-wall, Right-wall, Pledge algorithm
- Performance tracking (steps, rotations, walls followed)
- Algorithm switching capability
- Advanced wall detection with 8-sensor analysis
- Status reporting every 100 steps

**Use when:** You want to experiment with different maze-solving algorithms.

#### 3. `maze_tester.py`
**Features:**
- Sensor calibration mode
- Movement pattern testing
- Real-time sensor monitoring
- Debugging utilities
- Multiple operation modes (calibration, testing, monitoring, solving)

**Use when:** You need to test, calibrate, or debug your robot's sensors and movements.

#### 4. `optimized_maze_solver.py`
**Features:**
- Performance optimization with adaptive speed control
- Path length and performance tracking
- Data export functionality
- Advanced environment analysis
- Dynamic speed adjustment based on performance
- Detailed statistics and logging

**Use when:** You want maximum performance and detailed analytics.

#### 5. `maze_config.py`
**Features:**
- Configuration management for all parameters
- Utility functions for sensor processing
- Constants and thresholds in one place
- Easy parameter tuning

**Use when:** You want to easily adjust robot parameters without modifying main code.

## 🚀 How to Use

### Quick Start
1. Replace your current `maze_solver.py` with any of the enhanced versions
2. In Webots, make sure your controller is set to the correct file
3. Run the simulation

### For Testing and Calibration
```python
# Use maze_tester.py with different modes:
mode = 1  # Sensor calibration
mode = 2  # Movement testing
mode = 3  # Sensor monitoring  
mode = 4  # Simple maze solving with logs
```

### For Algorithm Comparison
```python
# In advanced_maze_solver.py, change the algorithm:
chosen_algorithm = Algorithm.LEFT_WALL   # Left wall following
chosen_algorithm = Algorithm.RIGHT_WALL  # Right wall following  
chosen_algorithm = Algorithm.PLEDGE      # Pledge algorithm
```

### For Performance Optimization
```python
# optimized_maze_solver.py automatically:
# - Adapts speed based on performance
# - Tracks path length and efficiency
# - Exports data for analysis
```

## 🔧 Configuration Options

### Sensor Thresholds
```python
WALL_THRESHOLD_CLOSE = 120    # Very close to wall
WALL_THRESHOLD_MEDIUM = 80    # Medium distance
WALL_THRESHOLD_FAR = 40       # Far from wall
```

### Speed Settings
```python
MAX_SPEED = 6.28              # Maximum motor speed
TURN_SPEED_RATIO = 0.8        # Speed ratio for turns
CORNER_SPEED_RATIO = 0.6      # Speed ratio for corners
```

## 📊 Performance Features

### What Gets Tracked:
- **Path Length**: Total distance traveled
- **Turns Made**: Number of direction changes
- **Wall Contacts**: How often robot gets too close to walls
- **Execution Time**: Total time to solve maze
- **Speed Efficiency**: Adaptive speed optimization

### Debug Information:
- Real-time sensor readings
- Current action being performed
- Motor speeds (left/right)
- Algorithm decision reasoning

## 🎯 Recommended Usage

1. **Start with `enhanced_maze_solver.py`** - It's your original algorithm but cleaner and more reliable
2. **Use `maze_tester.py`** if you need to debug sensor issues or calibrate thresholds
3. **Try `advanced_maze_solver.py`** to compare different algorithms
4. **Use `optimized_maze_solver.py`** for best performance and detailed analytics

## 🛠️ Customization Tips

### Adjust for Your Maze:
- Modify `WALL_THRESHOLD_*` values in `maze_config.py`
- Change `MAX_SPEED` if robot moves too fast/slow
- Adjust `TIMESTEP` for smoother/faster simulation

### Add Your Own Features:
- All scripts use modular design for easy extension
- Add new algorithms by following the existing patterns
- Implement new sensors by extending the sensor setup functions

## 📈 Performance Comparison

| Script | Complexity | Features | Best For |
|--------|------------|----------|----------|
| Original | Basic | Simple wall following | Learning basics |
| Enhanced | Medium | Clean OOP design | Production use |
| Advanced | High | Multiple algorithms | Algorithm research |
| Tester | Medium | Debugging tools | Development/testing |
| Optimized | High | Performance analytics | Competition/optimization |

## 🐛 Troubleshooting

### Common Issues:
1. **Robot moves too fast**: Reduce `MAX_SPEED` in config
2. **Sensor not detecting walls**: Lower `WALL_THRESHOLD_*` values
3. **Robot gets stuck in corners**: Adjust `CORNER_SPEED_RATIO`
4. **Erratic behavior**: Use `maze_tester.py` to calibrate sensors

### Debug Mode:
Enable debug output in any script by setting `debug = True` or using the monitoring features in `maze_tester.py`.

## 🎉 Next Steps

- Experiment with different algorithms
- Fine-tune parameters for your specific maze
- Add new features like mapping or shortest path finding
- Try implementing flood-fill or A* algorithms

Happy maze solving! 🤖🌟