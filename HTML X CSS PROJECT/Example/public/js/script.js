document.addEventListener('DOMContentLoaded',() =>{
const addFormContainer = document.getElementById('add-form-container');
const addStudentForm = document.getElementById('add-student-form');
const studentList = document.getElementById('student-list');

 // Fetch and display students
 function fetchStudents() {
    fetch('/api/students')
        .then(response => response.json())
        .then(data => {
            studentList.innerHTML = data.map(student => `   
                <div class="student-item" data-id="${student._id}">
                    <p>${student.name} - ${student.age} - ${student.gender} - ${student.email} - ${student.phone} - ${student.address} - ${student.course}</p>
                    <button class="edit-button">Edit</button>
                    <button class="delete-button">Delete</button>
                </div>
            `).join('');

            // Attach event listeners to edit and delete buttons
            document.querySelectorAll('.edit-button').forEach(button => {
                button.addEventListener('click', handleEdit);
            });

            document.querySelectorAll('.delete-button').forEach(button => {
                button.addEventListener('click', handleDelete);
            });
        })
        .catch(error => console.error('Error fetching student data:', error));
}

// Handle form submission for adding students
addStudentForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const studentData = {
        name: document.getElementById('add-name').value,
        age: document.getElementById('add-age').value,
        gender: document.getElementById('add-gender').value,
        email: document.getElementById('add-email').value,
        phone:document.getElementById('add-phone').value,
        address:document.getElementById('add-address').value,
        course: document.getElementById('add-course').value
    };

    fetch('/api/students', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(studentData)
    })
        .then(response => response.json())
        .then(() => {
            // Clear the form and refresh the list
            addStudentForm.reset();
            fetchStudents();
        })
        .catch(error => console.error('Error adding students:', error));
});

fetchStudents();
});