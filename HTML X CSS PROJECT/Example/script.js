// document.addEventListener('DOMContentLoaded', () => {
//     const addEmployeeForm = document.getElementById('add-employee-form');
//     const updateEmployeeForm = document.getElementById('update-employee-form');
//     const updateEmployeeIdInput = document.getElementById('update-employee-id');
//     const updateNameInput = document.getElementById('update-name');
//     const updateAgeInput = document.getElementById('update-age');
//     const updateRoleInput = document.getElementById('update-role');
//     const userList = document.getElementById('user-list');
//     const updateFormContainer = document.getElementById('update-form-container');
//     const addFormContainer = document.getElementById('add-form-container');
//     const cancelUpdateButton = document.getElementById('cancel-update');

//     // Fetch and display employees
//     function fetchEmployees() {
//         fetch('/api/users')
//             .then(response => response.json())
//             .then(data => {
//                 userList.innerHTML = data.map(user => `
//                     <div class="user-item" data-id="${user._id}">
//                         <p>${user.name} - ${user.age} - ${user.role}</p>
//                         <button class="edit-button">Edit</button>
//                         <button class="delete-button">Delete</button>
//                     </div>
//                 `).join('');

//                 // Attach event listeners to edit and delete buttons
//                 document.querySelectorAll('.edit-button').forEach(button => {
//                     button.addEventListener('click', handleEdit);
//                 });

//                 document.querySelectorAll('.delete-button').forEach(button => {
//                     button.addEventListener('click', handleDelete);
//                 });
//             })
//             .catch(error => console.error('Error fetching user data:', error));
//     }

//     // Handle form submission for adding employees
//     addEmployeeForm.addEventListener('submit', (e) => {
//         e.preventDefault();

//         const employeeData = {
//             name: document.getElementById('add-name').value,
//             age: document.getElementById('add-age').value,
//             course: document.getElementById('add-course').value,
//             address: document.getElementById('add-address').value,
//             gender: document.getElementById('add-gender').value,
//             mobile_no: document.getElementById('add-mobile').value
//         };

//         fetch('/api/users', {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify(employeeData)
//         })
//             .then(response => response.json())
//             .then(() => {
//                 // Clear the form and refresh the list
//                 addEmployeeForm.reset();
//                 fetchEmployees();
//             })
//             .catch(error => console.error('Error adding employee:', error));
//     });

//     // Handle form submission for updating employees
//     updateEmployeeForm.addEventListener('submit', (e) => {
//         e.preventDefault();

//         const id = updateEmployeeIdInput.value;
//         const employeeData = {
//             name: updateNameInput.value,
//             age: updateAgeInput.value,
//             role: updateRoleInput.value
//         };

//         fetch(`/api/users/${id}`, {
//             method: 'PUT',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify(employeeData)
//         })
//             .then(response => response.json())
//             .then(() => {
//                 // Clear the update form and refresh the list
//                 updateEmployeeForm.reset();
//                 updateFormContainer.style.display = 'none';
//                 addFormContainer.style.display = 'block';
//                 fetchEmployees();
//             })
//             .catch(error => console.error('Error updating employee:', error));
//     });

//     // Handle editing an employee
//     function handleEdit(e) {
//         const userItem = e.target.closest('.user-item');
//         console.log(userItem.firstChild.textContent);
//         const id = userItem.getAttribute('data-id');
//         const [name, age, role] = userItem.textContent.split(' - ');
//         const userParts = userItem.textContent.split(' - ').map(part=>part.trim())
//         console.log( 
//             {name: userParts[0],
//             age: userParts[1],
//             role: userParts[2]}
//         )

//         updateEmployeeIdInput.value = id;
//         updateNameInput.value = name;
//         updateAgeInput.value = age;
//         updateRoleInput.value = role;

//         // Show the update form and hide the add form
//         updateFormContainer.style.display = 'block';
//         addFormContainer.style.display = 'none';
//     }

//     // Handle canceling the update
//     cancelUpdateButton.addEventListener('click', () => {
//         updateEmployeeForm.reset();
//         updateFormContainer.style.display = 'none';
//         addFormContainer.style.display = 'block';
//     });

//     // Handle deleting an employee
//     function handleDelete(e) {
//         const userItem = e.target.closest('.user-item');
//         const id = userItem.getAttribute('data-id');

//         if (confirm('Are you sure you want to delete this employee?')) {
//             fetch(`/api/users/${id}`, { method: 'DELETE' })
//                 .then(response => response.json())
//                 .then(() => fetchEmployees())
//                 .catch(error => console.error('Error deleting employee:', error));
//         }
//     }

//     // Initial fetch of employees
//     fetchEmployees();
// });
