**Student Management System**
The Student Management System is a web-based application designed to efficiently manage student details, track issued items, and organize courses and timetables. 
It provides a comprehensive platform for administrators to handle administrative tasks related to student records and academic management.

**Features**
**Student Management:** 
Capture and maintain detailed student profiles.
**Issue Tracking:** Track items issued to students (e.g., library books, equipment).
**Course Management:** Organize courses and manage course-related information.
**Timetable Management:** Schedule and display class timetables.
**Data Visualization:** Utilize Chart.js for graphical representations of student-related data.
**PDF Generation:** Generate PDF reports using Reportlab.

**Technologies Used**
**Backend:** Python, Django
**Frontend:** HTML, CSS, Bootstrap, Bulma
**Database:** SQLite
**Data Visualization:** Chart.js
**PDF Generation:** Reportlab

**Installation**
**Clone the repository:**
git clone https://github.com/Tindae2022/student_manager.git

**Navigate into the project directory:**
cd student_manager

**Create a virtual environment:**
python -m venv venv

**Activate the virtual environment:**
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

**Install dependencies:**
pip install -r requirements.txt

**Apply database migrations:**
python manage.py migrate

**Start the development server:**
python manage.py runserver
Open your web browser and go to http://localhost:8000 to view the application.

**Usage**
Admin Panel: http://localhost:8000/admin
Username: admin
Password: [admin_password]

**Contributing**
Contributions are welcome. Please fork the repository and create a pull request.

License
This project is licensed under the MIT License.
