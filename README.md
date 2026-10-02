# Smart Ultrasonic NDT System

A Python and Streamlit based software prototype for ultrasonic A-scan signal analysis and possible defect indication.

## Features

- Ultrasonic A-scan signal generation
- Automatic peak detection
- Signal feature extraction
- Normal and possible defect analysis
- Defect position estimation
- Echo amplitude analysis
- A-scan graph visualization
- Inspection report generation
#screenshots
[possible defect.pdf](https://github.com/user-attachments/files/32969749/possible.defect.pdf)
[normal.pdf](https://github.com/user-attachments/files/32969744/normal.pdf)
[normal with peak.pdf](https://github.com/user-attachments/files/32969734/normal.with.peak.pdf)


## Technologies Used

- Python
- Streamlit
- NumPy
- SciPy
- Matplotlib

## Project Status
## Software Output

### Normal Condition

![Normal Output](screenshots/normal-output.png)

The system analyzes the normal ultrasonic A-scan and identifies the main echo peaks.

**Result:** No significant defect indication detected.

### Possible Defect Condition

![Possible Defect Output](screenshots/possible-defect-output.png)

The system analyzes the simulated defect signal and identifies an additional echo.

**Result:** Possible defect indication detected.
Software prototype using simulated ultrasonic signals.

## Future Scope

- Real ultrasonic data integration
- Real specimen testing
- Machine-learning-based classification
- Improved defect localization
