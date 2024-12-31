function openAddProductModal() {
    const modal = new bootstrap.Modal(document.getElementById('addProductModal'));
    modal.show();
}

function addProductToOffering() {
    const name = document.getElementById('productName').value;
    const quantity = document.getElementById('productQuantity').value;
    const price = document.getElementById('productPrice').value;

    if (name && quantity && price) {
        const table = document.getElementById('productList');
        const row = table.insertRow();

        row.innerHTML = `
            <td>${Date.now()}</td>
            <td>${name}</td>
            <td>${quantity}</td>
            <td>${price}</td>
            <td><button class="btn btn-danger btn-sm" onclick="deleteProductListItem(this)">Delete</button></td>
        `;

        const modal = bootstrap.Modal.getInstance(document.getElementById('addProductModal'));
        modal.hide();
        document.getElementById('addProductForm').reset();
    }
}

function deleteProductListItem(button) {
    const row = button.parentElement.parentElement;
    row.remove();
}

function saveOffering() {
    const data = {
        title: document.getElementById('offerTitle').value,
        customer: document.getElementById('targetCustomer').value,
        deliveryDate: document.getElementById('deliveryDate').value,
        email: document.getElementById('customerEmail').value,
        totalPrice: document.getElementById('totalPrice').value,
        products: Array.from(document.getElementById('productList').rows).map(row => ({
            id: row.cells[0].innerText,
            name: row.cells[1].innerText,
            quantity: row.cells[2].innerText,
            price: row.cells[3].innerText,
        }))
    };

    fetch('/offering', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }).then(response => {
        if (response.ok) {
            alert('Angebot erfolgreich gespeichert!');
            window.location.href = '/angebote';
        } else {
            alert('Fehler beim Speichern des Angebots.');
        }
    });
}

function changeReplacementProduct(rowId) {
    // Logic to open the modal and handle product replacement
    console.log("Change product for row: " + rowId);
}

function commitOfferingChanges() {
    // Logic to commit changes
    console.log("Committing changes to the offering...");
}

document.addEventListener('DOMContentLoaded', () => {
    fetch('/offerings')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('offerings-table-body');
            data.forEach(offer => {
                const row = document.createElement('tr');

                row.innerHTML = `
                    <td>${offer.id}</td>
                    <td>${offer.customerName}</td>
                    <td>${offer.deliveryDate}</td>
                    <td>${offer.status}</td>
                    <td>
                        ${offer.status !== 'Sent' ? `<button class="btn btn-primary btn-sm me-2" onclick="navigateToChange(${offer.id})">Change</button>` : ''}
                        <button class="btn btn-danger btn-sm" onclick="deleteOffering(${offer.id})">Delete</button>
                    </td>
                `;

                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Fehler beim Laden der Angebote:', error));
});

function navigateToChange(offerId) {
    window.location.href = `/edit-offering/${offerId}`;
}