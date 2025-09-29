# Maze Solver Webot 🤖

**Project Overview:** Advanced maze-solving robot implementation using multiple algorithms and enhanced wall-following techniques. This project features an e-puck robot navigating through complex mazes using proximity sensors in the Webots simulation environment.

![Robotics](https://img.shields.io/badge/Robotics-Simulation-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![Webots](https://img.shields.io/badge/Webots-Simulation-orange)
![Algorithm](https://img.shields.io/badge/Algorithm-Wall%20Following-red)

## 🚀 Features

- **Multiple Maze-Solving Algorithms**: Left-wall, Right-wall, Pledge algorithm
- **Enhanced Sensor Processing**: Advanced proximity sensor analysis with noise filtering
- **Performance Optimization**: Adaptive speed control and path optimization
- **Real-time Monitoring**: Debug tools and sensor calibration utilities
- **Analytics & Tracking**: Path length, performance metrics, and data export
- **Modular Design**: Easy to extend and customize for different maze types

## 🛠️ Technologies Used

- **Simulation Platform**: Webots Robot Simulator
- **Robot Model**: e-puck Robot with 8 proximity sensors
- **Programming Language**: Python 3.x
- **Algorithms**: Wall Following, Pledge Algorithm, Adaptive Optimization
- **Skills**: Robotics Simulation, Sensor Processing, Path Planning

## 📁 Project Structure

```
Maze_Solver_webot/
├── controllers/
│   └── maze_solver/
│       ├── maze_solver.py              # Original implementation
│       ├── enhanced_maze_solver.py     # Improved OOP version
│       ├── advanced_maze_solver.py     # Multiple algorithms
│       ├── maze_tester.py             # Testing & calibration tools
│       ├── optimized_maze_solver.py   # Performance optimized
│       ├── maze_config.py             # Configuration management
│       └── README_SCRIPTS.md          # Detailed script documentation
├── worlds/
│   └── The_Maze.wbt                   # Webots world file
├── Maze_topview.jpg                   # Maze visualization
└── README.md                          # This file
```

## 🎯 Algorithm Details

### 1. **Sensor Processing**
- Continuous monitoring of 8 proximity sensors
- Multi-threshold wall detection (close, medium, far)
- Noise filtering and sensor calibration tools

### 2. **Decision Making**
- Priority-based decision tree for complex scenarios
- Adaptive speed control based on environment
- Dynamic parameter adjustment for optimization

### 3. **Navigation Strategies**
- **Left Wall Following**: Classic left-hand rule implementation
- **Right Wall Following**: Right-hand rule for comparison
- **Pledge Algorithm**: Advanced algorithm with angle tracking
- **Optimized Approach**: Performance-focused with analytics

### 4. **Performance Features**
- Path length tracking and optimization
- Turn counting and efficiency metrics
- Real-time performance analytics
- Data export for analysis

## 🚀 Quick Start

### Prerequisites
- Webots Robot Simulator (R2023a or later)
- Python 3.x

### Running the Simulation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohamednizar17/Maze_Solver_webot.git
   cd Maze_Solver_webot
   ```

2. **Open Webots and load the world**
   - Open `worlds/The_Maze.wbt` in Webots

3. **Select your preferred algorithm**
   - **Basic**: Use `maze_solver.py` (original)
   - **Enhanced**: Use `enhanced_maze_solver.py` (recommended)
   - **Advanced**: Use `advanced_maze_solver.py` (multiple algorithms)
   - **Testing**: Use `maze_tester.py` (debugging tools)
   - **Optimized**: Use `optimized_maze_solver.py` (best performance)

4. **Run the simulation**
   - Set the controller in Webots to your chosen script
   - Click the play button to start

## 📊 Performance Comparison

| Algorithm | Efficiency | Features | Best For |
|-----------|------------|----------|----------|
| Original | Basic | Simple wall following | Learning |
| Enhanced | Good | Clean OOP design | Production |
| Advanced | Very Good | Multiple algorithms | Research |
| Optimized | Excellent | Performance analytics | Competition |

## 🔧 Configuration

Adjust parameters in `maze_config.py`:

```python
# Sensor thresholds
WALL_THRESHOLD_CLOSE = 120
WALL_THRESHOLD_MEDIUM = 80

# Speed settings
MAX_SPEED = 6.28
TURN_SPEED_RATIO = 0.8
```

## 📈 Features Showcase

- ✅ **Multi-Algorithm Support**: Compare different maze-solving strategies
- ✅ **Performance Analytics**: Track efficiency and optimization metrics
- ✅ **Debug Tools**: Sensor calibration and testing utilities
- ✅ **Adaptive Control**: Dynamic speed adjustment based on performance
- ✅ **Data Export**: Performance data export for analysis
- ✅ **Modular Design**: Easy to extend and customize

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgements

- **Webots Simulation Software** for providing a robust robotics simulation platform
- **e-puck Robot Community** for excellent documentation and support
- **Robotics Research Community** for algorithm development and best practices

## 📞 Contact

**Mohamed Nizar** - [@mohamednizar17](https://github.com/mohamednizar17)

Project Link: [https://github.com/mohamednizar17/Maze_Solver_webot](https://github.com/mohamednizar17/Maze_Solver_webot)

---
⭐ **Star this repository if you find it helpful!** ⭐
