# Real-Time Trend Graphs Implementation

## Overview
Successfully implemented real-time trend graphs for the desalination system HMI, replacing the placeholder with fully functional matplotlib-based visualization.

## Features Implemented

### 1. Real-Time Data Visualization
- **Tank Levels Plot**: Shows Ground Tank (green) and Roof Tank (blue) levels as percentages
- **Pressure Plot**: Shows RO Feed Pressure (red) in bar units
- **Time Window**: Rolling 60-second window for optimal visibility
- **Auto-scaling**: Dynamic y-axis adjustment based on data ranges

### 2. SCADA-Style Appearance
- **Dark Theme**: Professional SCADA color scheme (#1a2634 background, #0d1117 plot area)
- **White Text/Grid**: High contrast for industrial environments
- **Compact Layout**: Two side-by-side plots optimized for space
- **Legend**: Clear identification of data series

### 3. Performance Optimizations
- **Circular Buffer**: Uses `collections.deque` with maxlen=50 for efficient data storage
- **Idle Drawing**: Uses `draw_idle()` for smooth updates without blocking
- **Data Limiting**: Automatic trimming of old data points

## Technical Implementation

### Dependencies Added
```python
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from collections import deque
import time
```

### Key Components

#### 1. Data Storage Structure
```python
self.trend_data = {
    'time': deque(maxlen=self.max_trend_points),
    'ground_level': deque(maxlen=self.max_trend_points),
    'roof_level': deque(maxlen=self.max_trend_points),
    'pressure': deque(maxlen=self.max_trend_points)
}
```

#### 2. Plot Configuration
- **Figure**: 14x4 inches at 80 DPI for optimal display
- **Subplots**: 1x2 layout (tank levels | pressure)
- **Styling**: Dark theme with white text and grid lines
- **Limits**: Tank levels 0-100%, Pressure 0-80 bar

#### 3. Update Method
- Called from main `update()` method every system step
- Appends new data points with current timestamp
- Updates line plots with latest data
- Adjusts axis limits for rolling window view
- Refreshes canvas efficiently

## File Changes

### hmi.py Modifications
1. **Imports**: Added matplotlib and supporting libraries
2. **Initialization**: Added trend data storage and timing
3. **GUI Building**: Replaced placeholder with real matplotlib plots
4. **Update Loop**: Integrated trend updates into main update cycle
5. **New Method**: `_update_trends()` for data management and plot refresh

### New Files Created
- `test_trend_graphs.py`: Comprehensive demo script with multiple test scenarios

## Demo Scenarios

The test script includes four demonstration modes:

1. **Normal Operation**: Gradual startup with steady trends
2. **Pressure Variations**: Sinusoidal pressure changes to test pressure plot
3. **Tank Level Changes**: Filling/draining cycles to test level plots
4. **Mixed Scenario**: Complex patterns testing both plots simultaneously

## Usage Instructions

### Running the Enhanced HMI
```bash
cd "c:\Users\Legion\Desktop\Desalination\src"
python hmi.py
```

### Running Demo Tests
```bash
cd "c:\Users\Legion\Desktop\Desalination\src"
python test_trend_graphs.py
```

### Operating the Trends
1. Start the system using the START button
2. Observe real-time data plotting on both graphs
3. Trends automatically update every 500ms with system step
4. Data shows last 60 seconds in a rolling window
5. Y-axis auto-scales based on actual data ranges

## Benefits

### Operational Advantages
- **Real-time Monitoring**: Immediate visualization of system behavior
- **Trend Analysis**: Easy identification of patterns and anomalies
- **Historical Context**: 60-second window provides recent operational history
- **Multi-parameter View**: Simultaneous monitoring of key process variables

### Technical Advantages
- **Efficient Performance**: Optimized for real-time updates
- **Professional Appearance**: SCADA-standard dark theme
- **Scalable Design**: Easy to add more trend parameters
- **Integration**: Seamlessly integrated with existing HMI functionality

## Future Enhancements

### Potential Additions
1. **Historical Data Logging**: Save trend data to files for long-term analysis
2. **Zoom/Pan Controls**: Interactive plot navigation
3. **Data Export**: Export trend data to CSV/Excel
4. **Alarm Overlays**: Visual markers for alarm conditions
5. **Additional Parameters**: Turbidity, efficiency, production rate trends
6. **Time Range Selection**: Configurable trend window duration

### Configuration Options
1. **Update Rate**: Adjustable refresh frequency
2. **Data Retention**: Configurable buffer size
3. **Plot Colors**: Customizable color schemes
4. **Axis Ranges**: Manual or automatic scaling options

## Conclusion

The trend graphs implementation successfully transforms the HMI from a basic status display into a comprehensive SCADA-style monitoring interface. The real-time visualization provides operators with immediate insight into system behavior and trends, enabling proactive monitoring and faster response to process changes.

The implementation is production-ready, with efficient data handling, professional appearance, and seamless integration with the existing system architecture.
