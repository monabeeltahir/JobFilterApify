# Job Filter Application

A simple GUI-based Python application that filters job listings from JSON files based on similarity to user-provided job functions or types.

## Features

### Core Features
- **GUI Interface**: Easy-to-use graphical interface built with tkinter
- **Flexible Job Matching**: Filters jobs based on similarity to job titles, descriptions, and requirements
- **Multiple Role Support**: Recognizes that users can apply for multiple related roles (e.g., "Electrical Engineer" matches "Electrical Engineering", "Electronics Engineer", "Computer Engineering", etc.)
- **History Tracking**: Remembers previously searched job functions for quick reuse
- **Adjustable Threshold**: Control how strict or lenient the matching should be
- **Export Functionality**: Save filtered results to new JSON files
- **Quick Load**: Easy access to files in the scrappedjobs folder

### Table View Features ✨ NEW
- **Sortable Table**: Results displayed in a professional table with sortable columns
- **Click to Sort**: Click any column header to sort by that field (similarity, title, company, location, etc.)
- **Toggle Sort Order**: Click the same column again to reverse sort order
- **Detailed View Panel**: Click any job to see full details in the panel below
- **Quick Apply**: Double-click a job to open the application link in your browser
- **Open Link Button**: Select a job and click "Open Job Link" to view the posting

## Installation

### Prerequisites

- Python 3.6 or higher
- tkinter (usually comes with Python installation)

### Setup

1. Ensure Python 3 is installed:
```bash
python3 --version
```

2. Clone or navigate to the project directory:
```bash
cd /home/user/JobFilterApify
```

3. No additional packages needed! All dependencies are part of Python's standard library.

## Usage

### Running the Application

```bash
python3 job_filter_app.py
```

Or make it executable:
```bash
chmod +x job_filter_app.py
./job_filter_app.py
```

### Step-by-Step Guide

1. **Launch the Application**
   - Run `python3 job_filter_app.py`
   - The GUI window will open

2. **Load a Jobs File**
   - Click "Browse" to select a JSON file manually, OR
   - Click "Load File from scrappedjobs" to quickly select from the scrappedjobs folder
   - The application will display how many jobs were loaded

3. **Enter Job Function/Type**
   - Type your desired job function in the "Job Function/Type" field
   - Examples:
     - "Electrical Engineer"
     - "Software Developer"
     - "Data Scientist"
     - "Mechanical Engineering"
     - "Computer Science"

4. **Adjust Similarity Threshold (Optional)**
   - Default: 0.3 (30% similarity)
   - Lower values (0.1-0.3): More lenient, finds more jobs
   - Higher values (0.5-0.8): More strict, finds only close matches

5. **Filter Jobs**
   - Click "Filter Jobs" button
   - Results will appear in a sortable table
   - Jobs are initially sorted by similarity score (highest first)

6. **View Results in Table**
   - The table displays columns:
     - **Similarity**: Match percentage
     - **Job Title**: Position name
     - **Company**: Employer name
     - **Location**: Job location
     - **Type**: Employment type (Full-time, Part-time, etc.)
     - **Function**: Job category
     - **Level**: Seniority level

7. **Sort Results**
   - **Click any column header** to sort by that column
   - Click the same header again to reverse the sort order
   - Examples:
     - Click "Similarity" to sort by match percentage
     - Click "Company" to see jobs alphabetically by company
     - Click "Location" to group jobs by location

8. **View Job Details**
   - **Single-click** any row to see full details in the panel below
   - Details include:
     - Complete job description
     - Salary information (if available)
     - Job link
     - All other job metadata

9. **Open Job Links**
   - **Double-click** any job row to open the application link in your browser
   - OR select a job and click the "Open Job Link" button
   - Your default browser will open the job posting

10. **Export Results (Optional)**
    - Click "Export Filtered Jobs" to save results
    - Choose a location and filename
    - Results are saved as a JSON file

11. **Use Previous Searches**
    - Previously searched job functions appear in the dropdown
    - Select one and click "Use Selected" to quickly reuse it

## How the Filtering Works

The application uses multiple strategies to match jobs:

1. **Title Matching**: Checks if job titles contain similar words to your search
2. **Description Analysis**: Searches job descriptions for related terms
3. **Keyword Extraction**: Identifies key terms (like "electrical", "engineer")
4. **Degree Requirements**: Matches educational requirements (e.g., "electrical engineering degree")
5. **Fuzzy Matching**: Uses similarity algorithms to find related terms

### Examples

If you search for **"Electrical Engineer"**, it will match:
- "Electrical Engineer"
- "Electronics Engineer"
- "Electrical Engineering Intern"
- "Senior Electrical Design Engineer"
- Jobs requiring "BS in Electrical Engineering"
- "Computer Engineering" (related field)
- "Hardware Engineer" (related role)

## File Structure

```
JobFilterApify/
├── job_filter_app.py          # Main application file
├── requirements.txt            # Python dependencies (mostly built-in)
├── JOB_FILTER_README.md       # This file
├── job_filter_config.json     # Auto-generated: stores search history
├── scrappedjobs/              # Folder containing job JSON files
│   └── dataset_linkedin-jobs-scraper_2025-12-03_21-25-37-181
└── filtered_jobs_*.json       # Exported filtered results (optional)
```

## Configuration File

The application automatically creates `job_filter_config.json` to store:
- Previously searched job functions
- User preferences (coming in future versions)

Example:
```json
{
  "job_functions": [
    "Electrical Engineer",
    "Software Developer",
    "Data Scientist"
  ]
}
```

## Tips for Best Results

### Search Tips
1. **Start with Broader Terms**: Try "Software" before "Senior React Developer"
2. **Use Core Keywords**: "Electrical Engineer" works better than "EE looking for jobs"
3. **Adjust Threshold**: If too few results, lower the threshold; if too many irrelevant results, raise it
4. **Multiple Searches**: Remember you can search for multiple related terms and export each separately
5. **Check Related Fields**: "Computer Engineering" and "Electrical Engineering" often overlap

### Using the Table Interface
1. **Sort by Similarity First**: Start with similarity sorting to see best matches
2. **Group by Company**: Click "Company" column to see all jobs from the same employer
3. **Filter by Location**: Sort by location to focus on specific geographic areas
4. **Quick Preview**: Single-click to preview, double-click to apply
5. **Multiple Sorts**: Try different sort orders to discover opportunities you might miss

## JSON File Format

The application expects JSON files with this structure:

```json
[
  {
    "id": "12345",
    "title": "Electrical Engineer",
    "companyName": "Tech Corp",
    "location": "Seattle, WA",
    "descriptionText": "We are looking for an electrical engineer...",
    "jobFunction": "Engineering",
    "industries": "Technology",
    "employmentType": "Full-time",
    "seniorityLevel": "Mid-Senior level",
    "link": "https://..."
  }
]
```

## Troubleshooting

### Issue: No jobs found
- **Solution**: Lower the similarity threshold or use more general terms

### Issue: Too many irrelevant jobs
- **Solution**: Raise the similarity threshold or use more specific terms

### Issue: Can't load file
- **Solution**: Ensure the file is valid JSON format

### Issue: GUI doesn't appear
- **Solution**: Ensure tkinter is installed (`python3 -m tkinter`)

## Future Enhancements

The current version is basic. Future versions could include:

- Advanced filtering (location, salary, experience level)
- Machine learning-based job matching
- Skills extraction and matching
- Company preferences and blacklisting
- Application tracking
- Email notifications for new matching jobs
- Resume parsing to auto-detect suitable roles
- Integration with job boards APIs

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your JSON file format is correct
3. Try with different threshold values

## License

This is a basic utility application for personal use.

---

## Version History

### Version 2.0 - Enhanced Table Interface (Current)
**Released**: December 2025

**New Features**:
- ✨ Sortable table view for job results
- 📊 Click column headers to sort by any field
- 🔍 Detailed job view panel
- 🖱️ Double-click to open job links
- 🎨 Improved UI layout and organization

**Improvements**:
- Better visualization of results
- Easier navigation through jobs
- Quick access to job details
- Enhanced sorting capabilities

### Version 1.0 - Initial Release
**Released**: December 2025

**Features**:
- Basic job filtering by function/type
- Fuzzy matching algorithm
- Text-based results display
- Export functionality
- Job function history

---

**Current Version**: 2.0
**Last Updated**: December 2025
**Author**: Created for job search filtering and management
