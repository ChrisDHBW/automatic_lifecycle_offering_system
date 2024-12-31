window.onload = function() {
    fetchCustomers();
}

// Funktion zum Abrufen der Kunden vom API Endpunkt
function fetchCustomers() {
    fetch('/customers')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('customerTableBody');
            tableBody.innerHTML = ''; // Tabelle leeren
            data.forEach(customer => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${customer.id}</td>
                    <td>${customer.name}</td>
                    <td>${customer.industry}</td>
                    <td>${customer.devices}</td>
                    <td>${customer.offers}</td>
                    <td>
                        <button class="btn btn-info" onclick="viewCustomer(${customer.id})">Details</button>
                        <button class="btn btn-warning" onclick="editCustomer(${customer.id})">Change</button>
                        <button class="btn btn-danger" onclick="deleteCustomer(${customer.id})">Delete</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Fehler beim Laden der Kunden:', error));
}

// Funktion zur Detailansicht eines Kunden
function viewCustomer(id) {
    window.location.href = `/customerDetails/${id}`;
}

// Funktion zur Bearbeitungsansicht eines Kunden
function editCustomer(id) {
    window.location.href = `/editCustomer/${id}`;
}

// Funktion zum Löschen eines Kunden
function deleteCustomer(id) {
    fetch(`/customers/${id}`, { method: 'DELETE' })
        .then(response => {
            if (response.ok) {
                alert('Kunde erfolgreich gelöscht');
                fetchCustomers(); // Tabelle neu laden
            } else {
                alert('Fehler beim Löschen des Kunden');
            }
        })
        .catch(error => console.error('Fehler beim Löschen:', error));
}

// Funktion zur Filterung der Kunden basierend auf der Eingabe im Suchfeld
function filterCustomers() {
    const searchValue = document.getElementById('search').value.toLowerCase();
    const rows = document.querySelectorAll('#customerTableBody tr');
    rows.forEach(row => {
        const nameCell = row.cells[1];
        const name = nameCell ? nameCell.textContent.toLowerCase() : '';
        if (name.includes(searchValue)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

let originalData = {};

async function fetchCustomerData(customerId) {
    try {
        const response = await fetch(`/customers/${customerId}`);
        if (response.ok) {
            const data = await response.json();
            originalData = data;
            populateForm(data);
        } else {
            console.error('Failed to fetch customer data:', response.statusText);
        }
    } catch (error) {
        console.error('Error fetching customer data:', error);
    }
}

function populateForm(data) {
    Object.keys(data).forEach(key => {
        const input = document.getElementById(key);
        if (input) {
            input.value = data[key];
        }
    });
}

function resetForm() {
    populateForm(originalData);
}

async function updateCustomer(customerId) {
    try {
        const updatedData = {};
        Object.keys(originalData).forEach(key => {
            const input = document.getElementById(key);
            if (input) {
                updatedData[key] = input.value;
            }
        });

        const response = await fetch(`/customers/${customerId}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedData)
        });

        if (response.ok) {
            window.location.href = '/customers';
        } else {
            console.error('Failed to update customer:', response.statusText);
        }
    } catch (error) {
        console.error('Error updating customer:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const customerId = '123'; // Replace with dynamic customer ID if needed
    fetchCustomerData(customerId);

    document.getElementById('reset-button').addEventListener('click', resetForm);
    document.getElementById('update-button').addEventListener('click', () => updateCustomer(customerId));
});

document.getElementById('addCustomerBtn').addEventListener('click', function () {
    const customerData = {
        name: document.getElementById('customerName').value,
        email: document.getElementById('customerEmail').value,
        phone: document.getElementById('customerPhone').value,
        address: document.getElementById('customerAddress').value,
        city: document.getElementById('customerCity').value,
        zip: document.getElementById('customerZip').value
    };

    fetch('/customer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(customerData)
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/customers';
        } else {
            alert('Failed to add customer.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while adding the customer.');
    });
});

// Fetch customer details on page load
document.addEventListener('DOMContentLoaded', () => {
    const customerId = '123';
    fetch(`/customer/${customerId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('customerName').value = data.name;
            document.getElementById('customerEmail').value = data.email;
            document.getElementById('customerPhone').value = data.phone;

            const purchasedProductsList = document.getElementById('purchased-products-list');
            data.purchasedProducts.forEach(product => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${product.productId}</td>
                    <td>${product.productName}</td>
                    <td>${product.productType}</td>
                    <td>${product.manufacturerName}</td>
                    <td>${product.purchasedQuantity}</td>
                `;
                purchasedProductsList.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching customer details:', error));
});

// Handle Create Offering button click
document.getElementById('create-offering-btn').addEventListener('click', () => {
    alert('Create Offering functionality not yet implemented.');
});
