document.addEventListener('DOMContentLoaded', () => {
    const productId = '12345'; // Replace with dynamic product ID
    fetch(`/product/${productId}`)
        .then(response => response.json())
        .then(data => renderForm(data))
        .catch(error => console.error('Error fetching product data:', error));
});

function renderForm(data) {
    const form = document.getElementById('product-form');
    form.innerHTML = '';

    Object.keys(data.features).forEach((key) => {
        const featureGroup = data.features[key];

        const groupDiv = document.createElement('div');
        groupDiv.classList.add('mb-3');

        const label = document.createElement('label');
        label.classList.add('form-label');
        label.textContent = key;

        groupDiv.appendChild(label);

        featureGroup.forEach((feature) => {
            const input = document.createElement('input');
            input.classList.add('form-control', 'mb-2');
            input.value = feature.value;
            input.placeholder = feature.name;
            input.dataset.feature = feature.name; // Store feature name
            groupDiv.appendChild(input);
        });

        form.appendChild(groupDiv);
    });
}

function resetForm() {
    const form = document.getElementById('product-form');
    form.querySelectorAll('input').forEach(input => {
        input.value = input.defaultValue;
    });
}

function updateProduct() {
    const productId = '12345'; // Replace with dynamic product ID
    const form = document.getElementById('product-form');
    const features = {};

    form.querySelectorAll('input').forEach(input => {
        const featureName = input.dataset.feature;
        if (!features[featureName]) {
            features[featureName] = [];
        }
        features[featureName].push(input.value);
    });

    fetch(`/product/${productId}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ features }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to update product');
            }
            alert('Product updated successfully!');
        })
        .catch(error => {
            console.error('Error updating product:', error);
            alert('Failed to update product.');
        });
}

function loadFormFields() {
    const productType = document.getElementById('product-type').value;
    const dynamicFields = document.getElementById('dynamic-fields');

    // Clear previous fields
    dynamicFields.innerHTML = '';

    if (productType === 'type1') {
        dynamicFields.innerHTML = `
            <div class="mb-3">
                <label for="field1" class="form-label">Field 1</label>
                <input type="text" id="field1" class="form-control" placeholder="Enter Field 1">
            </div>
            <div class="mb-3">
                <label for="field2" class="form-label">Field 2</label>
                <input type="text" id="field2" class="form-control" placeholder="Enter Field 2">
            </div>
        `;
    } else if (productType === 'type2') {
        dynamicFields.innerHTML = `
            <div class="mb-3">
                <label for="field3" class="form-label">Field 3</label>
                <input type="text" id="field3" class="form-control" placeholder="Enter Field 3">
            </div>
            <div class="mb-3">
                <label for="field4" class="form-label">Field 4</label>
                <input type="number" id="field4" class="form-control" placeholder="Enter Field 4">
            </div>
        `;
    }
}

function addProduct() {
    const productType = document.getElementById('product-type').value;
    const dynamicFields = document.getElementById('dynamic-fields');

    // Collect data from dynamic fields
    const formData = {};
    Array.from(dynamicFields.querySelectorAll('input')).forEach(input => {
        formData[input.id] = input.value;
    });

    // Add the product type to the form data
    formData['productType'] = productType;

    // Send data to the API
    fetch('/product', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => {
        if (response.ok) {
            alert('Product added successfully!');
        } else {
            alert('Failed to add product.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred.');
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const searchField = document.getElementById('searchField');
    const productTableBody = document.getElementById('productTableBody');

    // Event listener for search functionality
    searchField.addEventListener('input', () => {
        const searchValue = searchField.value.toLowerCase();
        Array.from(productTableBody.rows).forEach(row => {
            const productName = row.cells[2].textContent.toLowerCase();
            row.style.display = productName.includes(searchValue) ? '' : 'none';
        });
    });

    // Example for dynamically setting button visibility
    Array.from(productTableBody.rows).forEach(row => {
        const status = row.cells[5].textContent;
        const endOfSaleButton = row.querySelector('.btn-danger');
        if (status === 'End of Sale' || status === 'End of Life') {
            endOfSaleButton.style.display = 'none';
        }
    });
});