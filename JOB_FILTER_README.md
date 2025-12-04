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

### Table View Features
- **Sortable Table**: Results displayed in a professional table with sortable columns
- **Click to Sort**: Click any column header to sort by that field (similarity, title, company, location, etc.)
- **Toggle Sort Order**: Click the same column again to reverse sort order
- **Detailed View Panel**: Click any job to see full details in the panel below
- **Quick Apply**: Double-click a job to open the application link in your browser
- **Open Link Button**: Select a job and click "Open Job Link" to view the posting

### Application Tracking Features
- **Mark as Applied**: Track which jobs you've applied to with a single click
- **Application Status**: Track application status (Applied, Interview Scheduled, Rejected, Offer Received)
- **Application Notes**: Add custom notes for each application
- **Applied Column**: Visual indicator showing which jobs you've applied to
- **Filter by Status**: Filter to show only applied or not-applied jobs
- **Application Tracker**: Dedicated window to view all your applications in one place
- **Color Coding**: Applied jobs are highlighted in green for easy identification
- **Auto-save**: All application data is automatically saved and persists between sessions

### Resume Parsing Features ✨ NEW
- **Upload Resume**: Parse PDF, DOCX, or TXT resume files to extract your skills and experience
- **Skill Extraction**: Automatically detect 100+ technical skills from your resume
- **Experience Estimation**: Calculate years of experience from your work history
- **Job Role Suggestions**: Get AI-powered job role recommendations based on your skills
- **Enhanced Matching**: Boost job similarity scores based on your resume skills (up to 30% boost)
- **Skill Highlighting**: See which of your skills match each job in the details panel
- **Auto-fill Job Function**: Automatically populate the job search field with suggested roles
- **Multiple Format Support**: Works with PDF, DOCX (Word), and TXT resume files
- **Categorized Skills Display**: View your skills organized by category (Programming, Cloud, Engineering, etc.)

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

3. Install resume parsing dependencies (for v4.0+ features):
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install PyPDF2 python-docx pdfplumber
```

**Note**: The application will still work without these libraries, but resume parsing features will be disabled.

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

### Resume Parsing (v4.0+)

12. **Upload Your Resume**
    - Click the "📄 Upload Resume" button
    - Select your resume file (PDF, DOCX, or TXT format)
    - The app will parse and extract:
      - Skills (100+ technical skills database)
      - Years of experience
      - Job titles from your work history
      - Education information
      - Suggested job roles based on your profile
    - View the parsing results in a tabbed dialog showing:
      - Summary tab: Overview of extracted information
      - Skills tab: Categorized skills (Programming, Cloud, Engineering, etc.)
      - Full Text tab: Complete extracted text from your resume

13. **Auto-fill Job Function**
    - After parsing your resume, you'll be asked if you want to use the top suggested role
    - Click "Yes" to auto-fill the job function field with the AI-recommended role
    - Or manually select from the suggested roles in the results dialog

14. **Enhanced Job Matching**
    - Once your resume is uploaded, job matching is automatically enhanced
    - Jobs that match your resume skills get a similarity boost (up to 30%)
    - More relevant jobs will appear higher in your results

15. **View Matching Skills**
    - When you click on a job, the details panel shows:
      - "YOUR MATCHING SKILLS" section
      - Lists which of your resume skills match the job requirements
      - Helps you tailor your application to highlight relevant skills

### Application Tracking

16. **Mark Jobs as Applied**
    - Select a job from the table
    - Click the "Mark as Applied" button
    - A dialog will open where you can:
      - Set the application date (defaults to today)
      - Select application status (Applied, Interview Scheduled, Rejected, Offer Received)
      - Add notes about the application
    - Click "Save" to track the application

17. **View Applied Jobs**
    - Use the "Show Jobs" dropdown above the table
    - Select "Applied Jobs Only" to see only jobs you've applied to
    - Select "Not Applied Jobs Only" to see jobs you haven't applied to
    - Applied jobs are highlighted in light green

18. **View All Applications**
    - Click the "View All Applications" button
    - A dedicated Application Tracker window opens
    - View all your applications sorted by date
    - Click any application to see details including notes
    - Open job links directly from the tracker

19. **Update Application Status**
    - Select an applied job from the table
    - Click "Mark as Applied" again
    - Update the status or add new notes
    - Click "Save" to update

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
├── resume_parser.py           # Resume parsing module (v4.0+)
├── requirements.txt            # Python dependencies
├── JOB_FILTER_README.md       # This file
├── job_filter_config.json     # Auto-generated: stores search history
├── job_applications.json      # Auto-generated: stores application tracking data
├── resume_data.json           # Auto-generated: stores parsed resume data (v4.0+)
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

## Application Tracking File

The application automatically creates `job_applications.json` to store your application tracking data:
- Application dates
- Application status
- Personal notes
- Job details

Example:
```json
{
  "4341564356": {
    "job_title": "Electrical Engineer, Lithium Refinery",
    "company": "Tesla",
    "applied_date": "2025-12-04",
    "status": "Applied",
    "notes": "Applied through company website. Highlighted battery experience.",
    "job_link": "https://...",
    "last_updated": "2025-12-04 10:30:00"
  }
}
```

**Important**: This file contains your personal application data and is automatically excluded from version control.

## Resume Data File (v4.0+)

The application automatically creates `resume_data.json` to store parsed resume information:
- Extracted skills
- Years of experience
- Job titles from work history
- Education information
- Suggested job roles
- Full resume text

Example:
```json
{
  "skills": ["python", "java", "aws", "docker", "machine learning"],
  "experience_years": 5,
  "job_titles": ["software engineer", "senior developer"],
  "education": ["bachelor computer science university"],
  "suggested_roles": ["Software Engineer", "Backend Developer", "Cloud Engineer"],
  "word_count": 450
}
```

**Important**: This file contains your personal resume data and is automatically excluded from version control.

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

### Resume Parsing Tips (v4.0+)
1. **Upload Once**: Your resume data is saved and used for all future job searches
2. **Use Clean Resumes**: PDFs and DOCX with clear text work best
3. **Include Keywords**: Make sure your resume lists technical skills explicitly
4. **Update Regularly**: Re-upload your resume when you gain new skills or experience
5. **Review Extracted Skills**: Check the Skills tab to ensure important skills were detected
6. **Use Suggested Roles**: The AI suggestions are based on your actual skill profile
7. **Check Matching Skills**: Use the matching skills section to tailor your applications

### Application Tracking Tips
1. **Mark Immediately**: Mark jobs as applied right after you submit to avoid duplicates
2. **Add Detailed Notes**: Include info like resume version used, cover letter points, referrals
3. **Update Status Regularly**: Keep status current to track your pipeline effectively
4. **Use the Tracker**: Review "View All Applications" weekly to follow up on pending applications
5. **Sort by Applied**: Click "Applied" column to see application dates at a glance
6. **Filter Strategically**: Use "Not Applied" filter to focus on new opportunities

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

Future versions could include:

- Advanced filtering (location, salary, experience level)
- Machine learning-based job matching (enhanced beyond current keyword matching)
- Company preferences and blacklisting
- Email notifications for new matching jobs
- Integration with job boards APIs (LinkedIn, Indeed, etc.)
- Calendar integration for interview scheduling
- Export applications to CSV/Excel
- Cover letter generation based on resume and job description
- Interview preparation recommendations
- Salary negotiation insights

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your JSON file format is correct
3. Try with different threshold values

## License

This is a basic utility application for personal use.

---

## Version History

### Version 4.0 - Resume Parsing & AI Matching (Current) ✨
**Released**: December 2025

**New Features**:
- 📄 Resume parsing for PDF, DOCX, and TXT files
- 🔍 Automatic skill extraction (100+ technical skills database)
- 🎯 AI-powered job role suggestions based on resume
- 📈 Enhanced job matching with resume-based scoring (up to 30% boost)
- ✅ Skill highlighting showing which resume skills match each job
- 🤖 Auto-fill job function with suggested roles
- 📊 Categorized skills display (Programming, Cloud, Engineering, etc.)
- 💼 Experience estimation from work history
- 🎓 Education information extraction
- 💾 Persistent resume data storage

**Technical Additions**:
- New `resume_parser.py` module with ResumeParser class
- PyPDF2, python-docx, pdfplumber dependencies
- `resume_data.json` for storing parsed resume
- Tabbed resume results dialog with Summary/Skills/Full Text views
- Enhanced `matches_job_function()` with resume-based boosting

**Improvements**:
- Smarter job matching based on actual candidate skills
- Reduced time to find relevant jobs
- Better visibility into skill-job alignment
- Data-driven job search recommendations

### Version 3.0 - Application Tracking
**Released**: December 2025

**New Features**:
- 📝 Mark jobs as applied with detailed tracking
- 📊 Application status management (Applied, Interview, Rejected, Offer)
- 📅 Track application dates automatically
- 📌 Add custom notes for each application
- ✅ Applied column with visual indicators
- 🎯 Filter by application status (All/Applied/Not Applied)
- 📋 Dedicated Application Tracker window
- 🎨 Color-coded applied jobs (green highlighting)
- 💾 Persistent storage of all application data

**Improvements**:
- Better job search workflow
- Organized application management
- Avoid duplicate applications
- Track follow-up actions
- Historical application data

### Version 2.0 - Enhanced Table Interface
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

**Current Version**: 4.0
**Last Updated**: December 2025
**Author**: Created for job search filtering and management
