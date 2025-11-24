# BMI Calculator - Project Statement

## Problem Statement

Many individuals struggle to track and assess their weight status in relation to their height, which is crucial for maintaining good health. Manual BMI calculations using the formula weight/height² are prone to errors and time-consuming. Additionally, people often don't understand what their calculated BMI value means in terms of health risk categories.

There is a need for a simple, accessible tool that:
- Accurately calculates Body Mass Index from user inputs
- Provides immediate health risk classification
- Displays reference information for BMI categories
- Requires no internet connection or complex setup
- Can be used repeatedly for tracking purposes

This project addresses these challenges by creating an automated, user-friendly BMI calculator that provides instant results with proper health categorization based on WHO standards.

## Scope of the Project

### In Scope

**Core Functionality:**
- BMI calculation using metric units (meters for height, kilograms for weight)
- Classification into six WHO-standard categories: Underweight, Normal weight, Overweight, and three Obese classes
- Display of comprehensive reference chart showing BMI ranges, categories, and associated health risks
- Input validation to prevent calculation errors from invalid data
- Error handling for non-numeric inputs and zero/negative height values

**User Interface:**
- Command-line interface with formatted text output
- Clear prompts for user input
- Structured table display using ASCII characters
- Readable result presentation with visual separators

**Technical Implementation:**
- Modular function-based design for maintainability
- Standard Python 3.x implementation without external dependencies
- Cross-platform compatibility (Windows, macOS, Linux)

### Out of Scope

The following features are **not included** in the current version but may be considered for future enhancements:
- Imperial unit support (pounds and feet/inches)
- Graphical User Interface (GUI)
- Data persistence (saving calculation history)
- Multiple user profiles
- BMI trend tracking over time
- Integration with fitness apps or wearables
- Age and gender-specific BMI recommendations
- Additional health metrics (BMR, body fat percentage)

## Target Users

### Primary Target Audience

**1. Health-Conscious Individuals**
- People monitoring their weight for general wellness
- Individuals on weight loss or weight gain journeys
- Fitness enthusiasts tracking body composition changes
- Age group: 18-65 years old

**2. Students and Educational Institutions**
- Computer science students learning Python programming
- Health science students studying body metrics
- Educational projects demonstrating basic algorithms
- Programming beginners working on practical applications

**3. Healthcare Support Personnel**
- Gym trainers and fitness coaches for quick client assessments
- Nutritionists requiring rapid BMI calculations during consultations
- Wellness program coordinators tracking participant metrics
- Community health workers conducting health screenings

### Secondary Target Audience

**4. Developers and Programmers**
- Beginners learning function-based programming concepts
- Developers seeking simple project templates
- Programmers interested in health-related applications
- Open-source contributors looking for enhancement opportunities

### User Characteristics

- **Technical Proficiency**: Basic computer literacy; ability to run command-line programs
- **Health Awareness**: Understanding that BMI is a screening tool, not diagnostic
- **Access**: Users with Python installed on their systems
- **Language**: English-speaking users comfortable with metric units
- **Usage Pattern**: Occasional use for periodic health checks (weekly/monthly)

## High-Level Features

### Feature 1: BMI Calculation Engine
**Description**: Accurate calculation of Body Mass Index using the standard formula (weight/height²)

**Capabilities**:
- Accepts height in meters and weight in kilograms
- Performs mathematical computation with decimal precision
- Rounds result to two decimal places for readability
- Returns calculated BMI value for display

**User Benefit**: Eliminates manual calculation errors and provides instant results

---

### Feature 2: Health Risk Classification System
**Description**: Automatic categorization of BMI results into WHO-defined health categories

**Capabilities**:
- Classifies BMI into six distinct categories:
  - Underweight (< 18.5)
  - Normal weight (18.5 - 24.9)
  - Overweight (25.0 - 29.9)
  - Obese Class I (30.0 - 34.9)
  - Obese Class II (35.0 - 39.9)
  - Obese Class III (≥ 40)
- Provides clear, actionable health status message
- Uses conditional logic for accurate categorization

**User Benefit**: Helps users understand the health implications of their BMI immediately

---

### Feature 3: Interactive Reference Chart
**Description**: Visual display of complete BMI classification table before calculation

**Capabilities**:
- Shows all BMI ranges with corresponding categories
- Displays associated health risk levels for each category
- Formatted as ASCII table with proper alignment
- Auto-adjusts column widths based on content length

**User Benefit**: Educates users about BMI standards and helps them interpret results

---

### Feature 4: Input Validation and Error Handling
**Description**: Robust checking of user inputs to prevent calculation errors

**Capabilities**:
- Validates that inputs are numeric values
- Checks for zero or negative height values
- Catches ValueError exceptions for non-numeric entries
- Provides clear error messages guiding users to correct input

**User Benefit**: Prevents crashes and ensures smooth user experience

---

### Feature 5: User-Friendly Console Interface
**Description**: Clean, intuitive command-line interface for easy interaction

**Capabilities**:
- Welcome banner with visual separators
- Clear input prompts specifying required units
- Formatted output with emphasis on results
- Structured flow from reference chart to calculation to results
- Professional appearance using box-drawing characters

**User Benefit**: Makes the tool accessible to users with minimal technical expertise

---

### Feature 6: Modular Code Architecture
**Description**: Well-organized code structure using separate functions for different tasks

**Capabilities**:
- `reference_chart()`: Handles display of BMI reference table
- `calculate_bmi()`: Performs BMI calculation logic
- `interpret_bmi()`: Manages health categorization
- `main()`: Orchestrates program flow and user interaction

**User Benefit**: Facilitates code understanding, testing, and future enhancements

---

## Technical Specifications Summary

| Aspect | Details |
|--------|---------|
| **Programming Language** | Python 3.6+ |
| **Dependencies** | None (uses standard library only) |
| **Input Format** | Height (meters), Weight (kilograms) |
| **Output Format** | Numeric BMI + Text category |
| **Platform** | Cross-platform (Windows, Linux, macOS) |
| **Interface Type** | Command-line (CLI) |
| **Execution Mode** | Single-run calculation |

## Success Metrics

The project will be considered successful if it:
1. Calculates BMI accurately according to the standard formula
2. Correctly categorizes all BMI values into appropriate health ranges
3. Runs without errors on Python 3.6+ environments
4. Handles invalid inputs gracefully without crashing
5. Provides clear, understandable output to users
6. Receives positive feedback from target users for ease of use
